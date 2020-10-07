import os

from regula.facerecognition.webclient import *

api_base_patch = os.getenv("API_BASE_PATH", "http://0.0.0.0:41101/api")

with open("face1.jpg", "rb") as f:
    face_1_bytes = f.read()

with open("face2.jpg", "rb") as f:
    face_2_bytes = f.read()

with open("real_video_1.mp4", "rb") as f:
    real_video_1_bytes = f.read()

with open("liveness_real_frame_1.jpg", "rb") as f:
    real_frame_1_bytes = f.read()

with open("liveness_real_depth_1.png", "rb") as f:
    real_depth_1_bytes = f.read()

with open("liveness_real_image_1.png", "rb") as f:
    real_image_1_bytes = f.read()


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

    print("                         Detect Results                          ")
    print("-----------------------------------------------------------------")
    print(f"detector_type: {detect_response.detector_type}")
    print(f"landmark_type: {detect_response.landmarks_type}")
    for i in detect_response.detections:
        print(f"landmarks: {i.landmarks}")
        print(f"roi: {i.roi}")
    print("-----------------------------------------------------------------")

    video_liveness_result = sdk.liveness_api.check_video_liveness(real_video_1_bytes)

    print("                   Check video liveness result                   ")
    print("-----------------------------------------------------------------")
    print(f"liveness_status: {video_liveness_result.liveness_status}")
    print("-----------------------------------------------------------------")

    depth_liveness_real_item = DepthLivenessItem(
        data_scene=real_frame_1_bytes, data_depth=real_depth_1_bytes, depth_scale=0.001
    )
    depth_liveness = DepthLiveness(images=[depth_liveness_real_item])
    depth_liveness_result = sdk.liveness_api.check_depth_liveness(depth_liveness=depth_liveness)

    print("                   Check depth liveness result                   ")
    print("-----------------------------------------------------------------")
    for i in depth_liveness_result:
        print(f"index: {i.index}")
        print(f"code: {i.code}")
        print(f"liveness_status: {i.liveness_status}")
    print("-----------------------------------------------------------------")

    image_liveness_item = ImageLivenessItem(data=real_image_1_bytes)
    image_liveness = ImageLiveness(images=[image_liveness_item])
    sdk.liveness_api.check_image_liveness(image_liveness=image_liveness)

    print("                   Check image liveness result                   ")
    print("-----------------------------------------------------------------")
    for i in depth_liveness_result:
        print(f"index: {i.index}")
        print(f"code: {i.code}")
        print(f"liveness_status: {i.liveness_status}")
    print("-----------------------------------------------------------------")
