from regula.facesdk.webclient.gen.model.output_image_params import OutputImageParams
from regula.facesdk.webclient.gen.model.image_fields_image import ImageFieldsImage
from regula.facesdk.webclient.gen.model.resize_options import ResizeOptions
from regula.facesdk.webclient.gen.model.search_request import SearchRequest
from regula.facesdk.webclient.gen.model.person_fields import PersonFields
from regula.facesdk.webclient.gen.model.crop import Crop
from tests.misc.paths_and_urls import *
import pytest

base_metadata = {'description': 'This is a test group'}
test_group_name = "test"
name_a = "Person A"


def standard_assertions(response, person_id):
    # We need this function because every test should check this first, and we don't want to repeat
    # these assertions for every test
    person = next((p for p in response['persons'] if p['id'] == person_id), None)
    assert person is not None, f"person_id {person_id} not found in the persons list"
    assert person['images'][0]['path'] != "", f"The image path for person_id {person_id} is empty"


@pytest.fixture(scope="function")
def facesdk_setup(facesdk):
    # Remember to choose API_BASE_PATH in paths_and_urls.py
    # We need to set up a group and person with image, so we'll have where to search
    group_id = create_dictionary(facesdk.group_api.create_group(test_group_name))['id']
    person_fields = PersonFields(name=name_a, groups=[group_id], metadata=base_metadata)
    person_id = create_dictionary(facesdk.person_api.create_person(person_fields))['id']
    face = read_image_bytes(FACE_1_PATH)
    facesdk.person_api.add_image_to_person(person_id=person_id, content=face)
    # Yield passes variables right to the tests
    yield facesdk, group_id, person_id, face
    # Everything written after yield will be done after every test
    facesdk.group_api.delete_group(group_id)
    facesdk.person_api.delete_person(person_id)


def test_search_limit_and_threshold(facesdk_setup):
    # Getting all the info from set-up function
    facesdk, group_id, person_id, face = facesdk_setup
    response = create_dictionary(facesdk.search_api.search(
        SearchRequest(
            group_ids=[group_id],
            image=ImageFieldsImage(
                content_type="image/jpeg",
                content=face
            ),
            limit=10,
            threshold=0.8
        ),
    ))
    standard_assertions(response, person_id)


def test_search_background_and_crop(facesdk_setup):
    # Getting all the info from set-up function
    facesdk, group_id, person_id, face = facesdk_setup
    background_color = [128, 128, 128]
    crop_params = Crop(type=0, pad_color=[0, 0, 0], size=[300, 400], )
    oi_params = OutputImageParams(background_color=background_color, crop=crop_params)
    response = create_dictionary(facesdk.search_api.search(
        SearchRequest(
            group_ids=[group_id],
            image=ImageFieldsImage(
                content_type="image/jpeg",
                content=face
            ),
            output_image_params=oi_params,
        ),
    ))
    standard_assertions(response, person_id)
    person = next((p for p in response['persons'] if p['id'] == person_id), None)
    assert 'crop' in person['detection'], "Crop data not found in person's detection"
    assert person['detection']['crop'] != "", "Crop data is empty"


def test_search_resize(facesdk_setup):
    # Getting all the info from set-up function
    facesdk, group_id, person_id, face = facesdk_setup
    res_opt = ResizeOptions(height=867, width=1300, quality=99)
    response = create_dictionary(facesdk.search_api.search(
        SearchRequest(
            group_ids=[group_id],
            image=ImageFieldsImage(
                content_type="image/jpeg",
                content=face,
                resize_options=res_opt
            ),
        ),
    ))
    standard_assertions(response, person_id)


def test_search_url(facesdk_setup):
    # Getting all the info from set-up function
    facesdk, group_id, person_id, face = facesdk_setup
    response = create_dictionary(facesdk.search_api.search(
        SearchRequest(
            group_ids=[group_id],
            image=ImageFieldsImage(image_url='https://i.imgur.com/u9gEjx7.jpeg'),
        ),
    ))
    standard_assertions(response, person_id)
