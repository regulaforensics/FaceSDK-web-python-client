import base64

from regula.facesdk.webclient import PersonApi as GenPersonApi, ApiClient, InlineObject, Image, PersonsPage, ImagePage, \
    PersonFields, Person, ImageFields


class PersonApi(GenPersonApi):
    def __init__(self, api_client: ApiClient):
        super().__init__(api_client)

    def add_image_to_person(self, person_id: int, content: bytes, content_type: str = None, **kwargs) -> Image:
        base_image = base64.b64encode(content).decode("UTF-8")
        image = InlineObject(ImageFields(content_type, base_image))
        return super().add_image_to_person(person_id, image, **kwargs)

    def create_person(self, person_fields: PersonFields, **kwargs) -> Person:
        return super().create_person(person_fields, **kwargs)

    def delete_image_of_person(self, image_id: int, person_id: int, **kwargs) -> None:
        return super().delete_image_of_person(image_id, person_id, **kwargs)

    def delete_person(self, person_id: int, **kwargs) -> None:
        return super().delete_person(person_id, **kwargs)

    def get_all_groups_by_person_id(self, page: int, size: int, person_id: int, **kwargs):
        return super().get_all_groups_by_person_id(page, size, person_id)

    def get_all_images_by_person_id(self, page: int, size: int, person_id: int, **kwargs) -> ImagePage:
        return super().get_all_images_by_person_id(page, size, person_id, **kwargs)

    def get_all_persons(self, page: int, size: int, **kwargs) -> PersonsPage:
        return super().get_all_persons(page, size, **kwargs)

    def get_image_of_person(self, image_id: int, person_id: int, **kwargs):
        return super().get_image_of_person(image_id, person_id, **kwargs)

    def get_person(self, person_id: int, **kwargs) -> Person:
        return super().get_person(person_id, **kwargs)

    def update_person(self, person_id: int, person_fields: PersonFields, **kwargs) -> None:
        return super().update_person(person_id, person_fields, **kwargs)
