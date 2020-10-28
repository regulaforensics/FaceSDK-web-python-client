import os

from regula.facerecognition.webclient import *

api_base_patch = os.getenv("API_BASE_PATH", "http://0.0.0.0:41101")

with open("face1.jpg", "rb") as f:
    face_1_bytes = f.read()

with open("face2.jpg", "rb") as f:
    face_2_bytes = f.read()

with Sdk(host=api_base_patch) as sdk:
    images = [
        CompareImage(index=1, data=face_1_bytes, type=ImageSource.LIVE),
        CompareImage(index=2, data=face_1_bytes, type=ImageSource.DOCUMENT_RFID),
        CompareImage(index=3, data=face_2_bytes),
    ]
    compare_request = CompareRequest(images=images)
    compare_response = sdk.matching_api.compare(compare_request)

    print("-----------------------------------------------------------------")
    print("                         Compare Results                         ")
    print("-----------------------------------------------------------------")
    for i in compare_response.results:
        print(f"pair({i.first_index}, {i.second_index}) similarity: {i.similarity}")
    print("-----------------------------------------------------------------")

    detect_request = DetectRequest(face_1_bytes)
    detect_response = sdk.matching_api.detect(detect_request)
    detect_results = detect_response.results

    print("                         Detect Results                          ")
    print("-----------------------------------------------------------------")
    print(f"detector_type: {detect_results.detector_type}")
    print(f"landmark_type: {detect_results.landmarks_type}")
    for i in detect_results.detections:
        print(f"landmarks: {i.landmarks}")
        print(f"roi: {i.roi}")
    print("-----------------------------------------------------------------")

