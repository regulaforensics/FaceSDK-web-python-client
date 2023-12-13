from regula.facesdk.webclient.gen.model.detect_request_attributes import DetectRequestAttributes
from regula.facesdk.webclient.gen.model.output_image_params import OutputImageParams
from regula.facesdk.webclient.gen.model.quality_request import QualityRequest
from regula.facesdk.webclient.gen.model.detect_request import DetectRequest
from regula.facesdk.webclient.gen.model.process_param import ProcessParam
from regula.facesdk.webclient.gen.model.crop import Crop
from tests.misc.paths_and_urls import *
import pytest
import base64


@pytest.fixture
def detect_setup():
    face1 = read_image_bytes(FACE_1_PATH)
    face1_b64 = base64.b64encode(face1).decode('utf-8')
    sev_faces = read_image_bytes(SEVERAL_FACES_IMAGE_PATH)
    sev_faces_b64 = base64.b64encode(sev_faces).decode('utf-8')
    yield [face1_b64, sev_faces_b64]


def basic_assertions(response):
    # We use this function to avoid repeating code in every test
    assert response['code'] == 0
    assert 'results' in response, "'results' field not found in response"
    assert 'detections' in response['results'], "'detections' field not found in 'results'"
    assert response['results']['detections'], "No detections found"


def test_detect_api(facesdk, detect_setup):
    request = DetectRequest(image=detect_setup[0])
    response = create_dictionary(facesdk.matching_api.detect(request))
    basic_assertions(response)


def test_scenario(facesdk, detect_setup):
    scenario = 'QUALITY_FULL'
    params = ProcessParam(scenario=scenario)
    request = DetectRequest(image=detect_setup[0], process_param=params)
    response = create_dictionary(facesdk.matching_api.detect(request))
    basic_assertions(response)
    scenario = 'QUALITY_FULL'
    assert response['results'][
               'scenario'] == scenario, f"Expected "+scenario+" but got "+response['results']['scenario']


def test_cropAllFaces_scenario(facesdk, detect_setup):
    params = ProcessParam(scenario='cropAllFaces', only_central_face=False)
    request = DetectRequest(image=detect_setup[1], process_param=params)
    response = create_dictionary(facesdk.matching_api.detect(request))
    basic_assertions(response)
    detections = response['results']['detections']
    assert len(detections) == 5, f"Expected 5 detections, but got {len(detections)} detections"


def test_only_central_face(facesdk, detect_setup):
    params = ProcessParam(only_central_face=True)
    request = DetectRequest(image=detect_setup[1], process_param=params)
    response = create_dictionary(facesdk.matching_api.detect(request))
    basic_assertions(response)
    detections = response['results']['detections']
    assert len(detections) == 1, f"Expected 1 detection, but got {len(detections)} detections"


def test_outputImageParams(facesdk, detect_setup):
    background_color = [128, 128, 128]
    crop_params = Crop(type=0, pad_color=[0, 0, 0], size=[300, 400], )
    oi_params = OutputImageParams(background_color=background_color, crop=crop_params)
    params = ProcessParam(output_image_params=oi_params)
    request = DetectRequest(image=detect_setup[1], process_param=params)
    response = create_dictionary(facesdk.matching_api.detect(request))
    basic_assertions(response)
    detections = response['results']['detections']
    assert len(detections) > 0, "No detections found in response"
    assert detections[0]['crop'] != '', "'crop' field is empty"


def test_quality(facesdk, detect_setup):
    quality_request = QualityRequest(
        background_match_color=[128, 128, 128],
        config=[{"name": "Roll", "range": [-5, 5]}]
    )
    params = ProcessParam(quality=quality_request)
    request = DetectRequest(image=detect_setup[1], process_param=params)
    response = create_dictionary(facesdk.matching_api.detect(request))
    basic_assertions(response)
    detection = response['results']['detections'][0]
    assert len(detection) > 0, "No detections found in response"
    assert detection['quality']['details'][0]['name'] == 'Roll'
    assert detection['quality']['details'][0]['range'] == [-5.0, 5.0]


def test_attributes(facesdk, detect_setup):
    attributes = DetectRequestAttributes(config=[{'name': 'Age', 'range': [5, 45]}])
    request = DetectRequest(image=detect_setup[1], process_param=ProcessParam(attributes=attributes))
    response = create_dictionary(facesdk.matching_api.detect(request))
    basic_assertions(response)
    detection = response['results']['detections'][0]
    assert len(detection) > 0, "No detections found in response"
    attribute_details = detection['attributes']['details']
    assert attribute_details[0]['name'] == 'Age'
    assert 5 <= attribute_details[0]['value'][0] <= 45
    assert 5 <= attribute_details[0]['value'][1] <= 45
