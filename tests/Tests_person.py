from regula.facesdk.webclient.gen.model.image_fields_image import ImageFieldsImage
from regula.facesdk.webclient.gen.model.search_request import SearchRequest
from regula.facesdk.webclient.gen.model.person_fields import PersonFields
import regula

from misc.paths_and_urls import *
import pytest

test_name = "test"
name_a = "Person A"
base_metadata = {'description': 'This is a test group'}


@pytest.fixture
def group_and_person_setup(facesdk):
    # This fixture creates a group and person before test, passes created group_id to the test and removes this
    # group after test
    created_group_response_dict = (
        create_dictionary(facesdk.group_api.create_group(group_name=test_name, metadata=base_metadata)))
    group_id = created_group_response_dict['id']
    person_fields = PersonFields(name=name_a, groups=[group_id], metadata=base_metadata)
    created_person_response_dict = create_dictionary(facesdk.person_api.create_person(person_fields))
    yield facesdk, created_person_response_dict, group_id
    facesdk.group_api.delete_group(group_id)
    try:
        facesdk.person_api.delete_person(created_person_response_dict['id'])
    except regula.facesdk.webclient.gen.exceptions.NotFoundException:
        pass  # Ignore the not found exception and proceed


def test_create_person(group_and_person_setup):
    # We don't need to create person, cause its created in our fixture. We just need to check the response here
    facesdk, person_response_dict, group_id = group_and_person_setup
    assert person_response_dict['name'] == "Person A", "The name of the person is incorrect"
    assert group_id in person_response_dict['groups'], "The group ID is not present in the person's group list"
    assert person_response_dict['metadata']['description'] == base_metadata['description'], \
        "The description of person is incorrect"


def test_get_person(group_and_person_setup):
    facesdk, person_response_dict, group_id = group_and_person_setup
    person_id = person_response_dict['id']
    response = facesdk.person_api.get_person(person_id=person_id)
    response_dict = create_dictionary(response)
    assert response_dict is not None, "No response received"
    assert response_dict['id'] == person_id, f"Expected person_id to be {person_id}, but got {response_dict['id']}"


def test_update_person(group_and_person_setup):
    facesdk, person_response_dict, group_id = group_and_person_setup
    person_id = person_response_dict['id']
    name_b = 'Person B'
    description = 'upd'
    person_fields = PersonFields(name=name_b, metadata={'description': description})
    facesdk.person_api.update_person(person_id=person_id, person_fields=person_fields)
    response = facesdk.person_api.get_person(person_id=person_id)
    response_dict = create_dictionary(response)
    assert response_dict is not None, "No response received"
    assert response_dict['name'] == name_b, f"Expected name to be " + name_b + ", but got {response_dict['name']}"
    assert response_dict['metadata']['description'] == description, f"Expected description to be " + description


def test_delete_person(group_and_person_setup):
    facesdk, person_response_dict, group_id = group_and_person_setup
    person_id = person_response_dict['id']
    facesdk.person_api.delete_person(person_id=person_id)
    response = facesdk.group_api.get_all_persons_by_group_id(page=1, size=1, group_id=group_id)
    response_dict = create_dictionary(response)
    assert response_dict['items'] == [], f"Expected 'items' to be empty, but got {response_dict['items']}"


def test_get_person_images(group_and_person_setup):
    facesdk, person_response_dict, group_id = group_and_person_setup
    person_id = person_response_dict['id']
    face1 = read_image_bytes(FACE_1_PATH)
    facesdk.person_api.add_image_to_person(person_id=person_id, content=face1)
    person_id = person_response_dict['id']
    response = facesdk.person_api.get_all_images_by_person_id(page=1, size=1, person_id=person_id)
    response_dict = create_dictionary(response)
    assert 'items' in response_dict, "'items' key not found in the response dictionary"
    assert "id" in response_dict["items"], 'id of photo not found'
    assert "path" in response_dict["items"], 'path of photo not found'


def test_person_groups(group_and_person_setup):
    facesdk, person_response_dict, group_id = group_and_person_setup
    test_name_2 = 'Second_test'
    created_group_response_dict = (
        create_dictionary(facesdk.group_api.create_group(group_name=test_name_2, metadata=base_metadata)))
    group_id_2 = created_group_response_dict['id']
    person_fields = PersonFields(name=name_a, groups=[group_id, group_id_2], metadata=base_metadata)
    person_id_2 = create_dictionary(facesdk.person_api.create_person(person_fields))['id']
    response_dict = create_dictionary(
        facesdk.person_api.get_all_groups_by_person_id(page=1, size=2, person_id=person_id_2))
    # Asserting on the number of items in the response
    assert len(response_dict['items']) == 2, f"Expected 2 items, but got {len(response_dict['items'])}"
    # Collecting the names of the groups from the response
    group_names = [group['name'] for group in response_dict['items']]
    # Asserting on the names of the groups
    assert test_name in group_names, test_name + " not found in group names"
    assert test_name_2 in group_names, test_name_2 + " not found in group names"
    facesdk.person_api.delete_person(person_id_2)
    facesdk.group_api.delete_group(group_id_2)


def test_add_image_to_person(group_and_person_setup):
    facesdk, person_response_dict, group_id = group_and_person_setup
    person_id = person_response_dict['id']
    face1 = read_image_bytes(FACE_1_PATH)
    facesdk.person_api.add_image_to_person(person_id=person_id, content=face1)
    request = SearchRequest(group_ids=[group_id],
                            image=ImageFieldsImage(content_type="", content=face1),
                            limit=10,
                            threshold=0.8)
    response = create_dictionary(facesdk.search_api.search(request))
    person_ids = [person['id'] for person in response['persons']]
    assert person_id in person_ids, f"person_id {person_id} is not in the search results"
    person = next((p for p in response['persons'] if p['id'] == person_id), None)
    assert person is not None, f"person_id {person_id} not found in the persons list"
    assert person['images'][0]['path'] != "", f"The image path for person_id {person_id} is empty"


def test_create_person_without_metadata(group_and_person_setup):
    facesdk, person_response_dict, group_id = group_and_person_setup
    person_fields = PersonFields(name=name_a, groups=[group_id])
    created_person_response_dict = create_dictionary(facesdk.person_api.create_person(person_fields))
    facesdk.person_api.delete_person(created_person_response_dict['id'])
