import base64
import os

from regula.facesdk.webclient.ext import FaceSdk
from regula.facesdk.webclient.gen.models.image_fields_image import ImageFieldsImage
from regula.facesdk.webclient.gen.models.image_source import ImageSource
from regula.facesdk.webclient.gen.models.match_and_search_request_images_item import MatchAndSearchRequestImagesItem
from regula.facesdk.webclient.gen.models.person_fields import PersonFields
from regula.facesdk.webclient.gen.models.search_request import SearchRequest
from regula.facesdk.webclient.gen.models.update_group import UpdateGroup
from regula.facesdk.webclient.gen.models.match_and_search_request import MatchAndSearchRequest

api_base_path = os.getenv("API_BASE_PATH", "http://nightly-faceapi.regula.local")

with open("face1.jpg", "rb") as f:
    face_1_bytes = f.read()

with open("face2.jpg", "rb") as f:
    face_2_bytes = f.read()

sdk = FaceSdk(api_base_path)

person1_id = sdk.person_api.create_person(PersonFields(name="person1", metadata={})).id
person2_id = sdk.person_api.create_person(PersonFields(name="person2", metadata={})).id

sdk.person_api.add_image_to_person(person1_id, face_1_bytes)
sdk.person_api.add_image_to_person(person2_id, face_2_bytes)

person1 = sdk.person_api.get_person(person1_id)
person2 = sdk.person_api.get_person(person2_id)

group = sdk.group_api.create_group("group13233")

sdk.group_api.update_persons_in_group(group.id, UpdateGroup(addItems=[person1.id, person2.id]))

result = sdk.search_api.search(
    SearchRequest(
        groupIds=[],
        image=ImageFieldsImage(
            contentType="",
            content=face_1_bytes
        ),
        limit=10,
        threshold=0.8
    ),
)

print(f"Person #1 {person1.id} {person1.name}")
print(f"Person #2 {person2.id} {person2.name}")
print(f"Group {group.id} {group.name}")
print(result)

match_and_search = sdk.match_api.match_and_search(
    MatchAndSearchRequest(
        images=[MatchAndSearchRequestImagesItem(content=base64.b64encode(face_1_bytes).decode("UTF-8"), type=ImageSource.LIVE),
                MatchAndSearchRequestImagesItem(content=base64.b64encode(face_2_bytes).decode("UTF-8"), type=ImageSource.LIVE)],
        groupIds=[group.id]
    ),
)

print(f"{match_and_search}")
