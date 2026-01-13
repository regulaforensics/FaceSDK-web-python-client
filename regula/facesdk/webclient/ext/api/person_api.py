import base64

from regula.facesdk.webclient.gen.models.add_image_to_person_request import AddImageToPersonRequest
from regula.facesdk.webclient.gen.models.add_image_to_person_request_image import AddImageToPersonRequestImage
from regula.facesdk.webclient.gen.models.add_image_to_person_response import AddImageToPersonResponse
from regula.facesdk.webclient.gen.api.person_api import PersonApi as GenPersonApi
from regula.facesdk.webclient.gen.models.person import Person
from regula.facesdk.webclient.gen.models.person_fields import PersonFields
from uuid import UUID

class PersonApi(GenPersonApi):
    def add_image_to_person(self, person_id: UUID, content: bytes, content_type: str = None, **kwargs) -> AddImageToPersonResponse:
        base_image = base64.b64encode(content).decode("UTF-8")
        image = AddImageToPersonRequest(image=AddImageToPersonRequestImage(contentType=content_type, content=base_image))
        return super().add_image_to_person(person_id, image, **kwargs)

    def create_person(self, person_fields: PersonFields, **kwargs) -> Person:
        if person_fields.metadata is None:
            person_fields.metadata = {}
        return super().create_person(person_fields, **kwargs)
