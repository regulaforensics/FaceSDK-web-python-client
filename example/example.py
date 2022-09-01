import os

from regula.facesdk.webclient import MatchImage, MatchRequest
from regula.facesdk.webclient.ext import FaceSdk, DetectRequest
from regula.facesdk.webclient.gen.model.image_source import ImageSource

api_base_path = os.getenv("API_BASE_PATH", "https://faceapi.regulaforensics.com/")

with open("face1.jpg", "rb") as f:
    face_1_bytes = f.read()

with open("face2.jpg", "rb") as f:
    face_2_bytes = f.read()

with FaceSdk(host=api_base_path) as sdk:
    images = [
        MatchImage(index=1, data=face_1_bytes, type=ImageSource.LIVE),
        MatchImage(index=2, data=face_1_bytes, type=ImageSource.DOCUMENT_RFID),
        MatchImage(index=3, data=face_2_bytes),
    ]
    match_request = MatchRequest(images=images, thumbnails=True)
    match_response = sdk.matching_api.match(match_request)

    print("-----------------------------------------------------------------")
    print("                         Matching Results                        ")
    print("-----------------------------------------------------------------")
    for comparison in match_response.results:
        print(f"pair({comparison.first_index}, {comparison.second_index}) similarity: {comparison.similarity}")
    print("-----------------------------------------------------------------")

    detect_request = DetectRequest(image=face_1_bytes, attributes=True)
    detect_response = sdk.matching_api.detect(detect_request)
    detect_results = detect_response.results

    print("                         Detect Results                          ")
    print("-----------------------------------------------------------------")
    print(f"detector_type: {detect_results.detector_type}")
    print(f"landmark_type: {detect_results.landmarks_type}")
    for detection in detect_results.detections:
        print(f"landmarks: {detection.landmarks}")
        print(f"roi: {detection.roi}")
        print(f"attributes: {detection.attributes}")
    print("-----------------------------------------------------------------")
