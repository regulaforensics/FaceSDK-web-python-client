import os
import pytest
from regula.facesdk.webclient.ext import FaceSdk

API_BASE_PATH = "http://localhost:41101/"
# API_BASE_PATH = "http://172.20.40.141:41101"
# API_BASE_PATH = "https://faceapi.regulaforensics.com/"
# API_BASE_PATH = "https://test-faceapi.regulaforensics.com/"

project_dir = os.path.dirname(os.path.abspath(__file__))
files_path = os.path.join(project_dir, 'files')

FACE_1_PATH = os.path.join(files_path, "face1.jpg")
FACE_2_PATH = os.path.join(files_path, "face2.jpg")
LIVE_PHOTO_PATH = os.path.join(files_path, "me.png")
PRINTED_DOCUMENT_PATH = os.path.join(files_path, "printedDoc.png")
DOCUMENT_WITH_LIVE_PATH = os.path.join(files_path, "me_and_id.png")
SEVERAL_FACES_IMAGE_PATH = os.path.join(files_path, "severalFaces.jpg")


def read_image_bytes(image_path):
    with open(image_path, "rb") as f:
        return f.read()


def create_dictionary(response):
    # We need this function because a response object is not subscriptable
    response_dict = response.to_dict() if hasattr(response, 'to_dict') else response
    return response_dict


@pytest.fixture
def facesdk():
    return FaceSdk(host=API_BASE_PATH)