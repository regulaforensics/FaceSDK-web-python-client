import os

from regula.facesdk.webclient.ext import FaceSdk
from regula.facesdk.webclient.gen.model.image_fields_image import ImageFieldsImage
from regula.facesdk.webclient.gen.model.person_fields import PersonFields
from regula.facesdk.webclient.gen.model.search_request import SearchRequest
from regula.facesdk.webclient.gen.model.update_group import UpdateGroup

api_base_path = os.getenv("API_BASE_PATH", "http://127.0.0.0:41101")

with open("face1.jpg", "rb") as f:
    face_1_bytes = f.read()

with open("face2.jpg", "rb") as f:
    face_2_bytes = f.read()

sdk = FaceSdk(api_base_path)

person1_id = sdk.person_api.create_person(PersonFields("person1", {})).id
person2_id = sdk.person_api.create_person(PersonFields("person2", {})).id

sdk.person_api.add_image_to_person(person1_id, face_1_bytes)
sdk.person_api.add_image_to_person(person2_id, face_2_bytes)

person1 = sdk.person_api.get_person(person1_id)
person2 = sdk.person_api.get_person(person2_id)

group = sdk.group_api.create_group("group1")

sdk.group_api.update_persons_in_group(group.id, UpdateGroup([int(person1.id), int(person2.id)]))

result = sdk.search_api.search(
    SearchRequest(
        group_ids=[int(group.id)],
        image=ImageFieldsImage(
                content_type="",
                content=face_1_bytes
            )
        )
)

print(f"Person #1 {int(person1.id)} {person1.name}")
print(f"Person #2 {int(person2.id)} {person2.name}")
print(f"Group {int(group.id)} {group.name}")
print(result)



