from regula.facesdk.webclient.gen.model.group_to_create import GroupToCreate
from regula.facesdk.webclient.gen.model.person_fields import PersonFields
from regula.facesdk.webclient.gen.model.update_group import UpdateGroup
from misc.paths_and_urls import *
import pytest

test_group_name = "test"
name_a = "Person A"
base_metadata = {'description': 'This is a test group'}


@pytest.fixture
def groups_setup(facesdk):
    # This fixture creates a group before test, passes created group_id to the test and removes this group_id after test
    created_group_response = (
        create_dictionary(facesdk.group_api.create_group(group_name=test_group_name, metadata=base_metadata)))
    group_id = created_group_response['id']
    yield group_id, created_group_response
    delete_response = facesdk.group_api.delete_group(group_id)
    assert delete_response is None, f"Unexpected response: {delete_response}"


def test_create_and_delete_group(groups_setup):
    # We don't need to create group because it's already created via fixture.
    # We just need to check creation response, deletion response will be checked in groups_setup
    group_id, response_dict = groups_setup
    assert response_dict is not None, "No response received"
    assert response_dict['name'] == test_group_name, "Name of the group is incorrect"
    assert response_dict['metadata']['description'] == base_metadata['description'], ("Metadata of the group is "
                                                                                      "incorrect")


def test_get_all_groups(facesdk):
    # Step 1: Make a list to store the ids of the created groups
    created_group_ids = []
    # Step 2: Creation of groups
    for i in range(4):
        # Create a group and get its id from response
        create_response = create_dictionary(facesdk.group_api.create_group(f"{test_group_name}_{i}"))
        group_id = create_response['id']
        # Store the group_id for later deletion
        created_group_ids.append(group_id)

    # Step 3: Get all groups
    response_dict = create_dictionary(facesdk.group_api.get_all_groups(page=2, size=2))

    # Step 4: Deletion of groups
    for group_id in created_group_ids:
        # Remove the group using its id
        delete_response = facesdk.group_api.delete_group(group_id)
        assert delete_response is None, f"Unexpected response: {delete_response}"

    # Step 5: check that page 2 with 2 items exist
    assert response_dict is not None, "No response received"
    assert len(response_dict['items']) == 2, f"Expected 2 items on page, but got {len(response_dict['items'])} items"
    assert response_dict['page'] == 2, f"Expected page to be 2, but got {response_dict['page']}"


def test_get_all_persons_by_group_id(facesdk, groups_setup):
    # Step 1: Getting created group_id from fixture
    group_id = groups_setup[0]
    # Step 2: Adding person to a created group
    person_fields = PersonFields(name=name_a, groups=[group_id], metadata=base_metadata)
    facesdk.person_api.create_person(person_fields)
    # Step 3: Get persons from created group_id
    persons_response = facesdk.group_api.get_all_persons_by_group_id(page=1, size=1, group_id=group_id)
    persons_response_dict = create_dictionary(persons_response)

    facesdk.person_api.delete_person(persons_response_dict['items'][0]['id'])
    assert persons_response_dict is not None, "No response received"
    assert persons_response_dict['items'][0]['name'] == name_a, "Name of Person is incorrect"
    assert persons_response_dict['items'][0]['metadata']['description'] == base_metadata['description'], \
        "Metadata of the group is incorrect"
    assert persons_response_dict['items'][0]['groups'][0] == group_id, "group_id is incorrect"


def test_get_group(facesdk, groups_setup):
    # Step 1: Get all groups and take the first group_id that appears
    groups_response_dict = create_dictionary(facesdk.group_api.get_all_groups(page=1, size=1))
    assert len(groups_response_dict['items']) > 0, "No groups found"
    group_id = groups_response_dict['items'][0]['id']

    # Step 2: Using obtained id to get chosen group
    group_response_dict = create_dictionary(facesdk.group_api.get_group(group_id))
    assert group_response_dict is not None, "No response received"
    assert group_response_dict['id'] == group_id, "group_id is incorrect"


def test_group_update(facesdk, groups_setup):
    # Step 1: Getting group_id from the fixture
    group_id = groups_setup[0]
    # Step 2: Updating group with new name
    new_name = 'updated_test_group'
    updated_metadata = {'description': 'updated meta'}
    facesdk.group_api.update_group(group_id=group_id,
                                   group_to_create=GroupToCreate(name=new_name, metadata=updated_metadata))
    updated_group_response_dict = create_dictionary(facesdk.group_api.get_group(group_id))

    # Step 3: Checking that name is updated
    assert updated_group_response_dict[
               'name'] == new_name, f"Group name not updated: {updated_group_response_dict['name']}"
    assert updated_group_response_dict['metadata']['description'] == updated_metadata[
        'description'], "Updated group meta is wrong"


def test_update_persons_in_group(facesdk, groups_setup):
    # Step 1: Getting group_id from the fixture
    group_id = groups_setup[0]

    # Step 2: Creating some persons and adding them to the group
    person_fields = PersonFields(name=name_a, groups=[group_id], metadata=base_metadata)
    facesdk.person_api.create_person(person_fields)

    # Step 3: Getting the group's persons
    initial_persons_response = facesdk.group_api.get_all_persons_by_group_id(page=1, size=10, group_id=group_id)
    initial_persons_response_dict = create_dictionary(initial_persons_response)
    initial_person_ids = [person['id'] for person in initial_persons_response_dict['items']]

    # Step 4: Removing them
    update_group_remove = UpdateGroup(remove_items=initial_person_ids)
    facesdk.group_api.update_persons_in_group(group_id=group_id, update_group=update_group_remove)

    # Step 5: Creating new persons and adding them to the group
    new_person_names = ["New Person A", "New Person B"]
    new_person_ids = []
    for name in new_person_names:
        person_fields = PersonFields(name=name, groups=[group_id], metadata=base_metadata)
        created_person_response_dict = create_dictionary(facesdk.person_api.create_person(person_fields))
        new_person_ids.append(created_person_response_dict['id'])

    # Step 6: Testing that they're here
    updated_persons_response_dict = create_dictionary(
        facesdk.group_api.get_all_persons_by_group_id(page=1, size=10, group_id=group_id))
    updated_person_ids = [person['id'] for person in updated_persons_response_dict['items']]
    assert set(updated_person_ids) == set(
        new_person_ids), f"Updated person ids don't match: {updated_person_ids} != {new_person_ids}"
    updated_person_names = [person['name'] for person in updated_persons_response_dict['items']]
    assert set(updated_person_names) == set(
        new_person_names), f"Updated person ids don't match: {updated_person_names} != {new_person_names}"
    assert len(updated_persons_response_dict['items']) == 2, 'Expected 2 persons in updated list'


def test_create_group_without_metadata(facesdk):
    created_group_response_dict = (
        create_dictionary(facesdk.group_api.create_group(group_name=test_group_name)))
    group_id = created_group_response_dict['id']
    facesdk.group_api.delete_group(group_id)
