import os

from regula.face.webclient.ext import MatchingApi, CompareRequest, CompareRequestFields
from regula.face.webclient.gen import ImageSource

api_base_patch = os.getenv("API_BASE_PATH", "http://0.0.0.0:8080/api")

with open("face1.jpg", "rb") as f:
    face_1_bytes = f.read()

with open("face2.jpg", "rb") as f:
    face_2_bytes = f.read()


with MatchingApi(host=api_base_patch) as api:
    images = [
        CompareRequestFields(index=1, data=face_1_bytes, type=int(ImageSource.LIVE)),
        CompareRequestFields(index=2, data=face_1_bytes, type=int(ImageSource.DOCUMENT_RFID)),
        CompareRequestFields(index=3, data=face_2_bytes)
    ]
    compare_request = CompareRequest(images=images)

    compare_response = api.compare(compare_request)

    print("                                                                 ")
    print("                         Compare Results                         ")
    print("-----------------------------------------------------------------")
    for i in compare_response.results:
        print(f"pair({i.first_index}, {i.second_index}) similarity: {i.similarity}")
    print("-----------------------------------------------------------------")
