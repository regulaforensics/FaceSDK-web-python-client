from regula.facesdk.webclient.gen import ApiClient
from regula.facesdk.webclient.gen.api.group_api import GroupApi as GenGroupApi
from regula.facesdk.webclient.gen.model.group import Group
from regula.facesdk.webclient.gen.model.group_page import GroupPage
from regula.facesdk.webclient.gen.model.group_to_create import GroupToCreate
from regula.facesdk.webclient.gen.model.persons_page import PersonsPage
from regula.facesdk.webclient.gen.model.update_group import UpdateGroup


class GroupApi(GenGroupApi):
    def __init__(self, api_client: ApiClient):
        super().__init__(api_client)

    def create_group(self, group_name: str, metadata=None, **kwargs) -> Group:
        if metadata is None:
            metadata = {}
        group_to_create = GroupToCreate(group_name, metadata)
        return super().create_group(group_to_create, **kwargs)

    def delete_group(self, group_id: int, **kwargs) -> None:
        return super().delete_group(group_id, **kwargs)

    def get_all_groups(self, page: int, size: int, **kwargs) -> GroupPage:
        return super().get_all_groups(page, size, **kwargs)

    def get_all_persons_by_group_id(self, page: int, size: int, group_id: int, **kwargs) -> PersonsPage:
        return super().get_all_persons_by_group_id(page, size, group_id, **kwargs)

    def get_group(self, group_id: int, **kwargs) -> Group:
        return super().get_group(group_id, **kwargs)

    def update_group(self, group_id: int, group_to_create: GroupToCreate, **kwargs) -> None:
        return super().update_group(group_id, group_to_create, **kwargs)

    def update_persons_in_group(self, group_id: int, update_group: UpdateGroup, **kwargs) -> None:
        return super().update_persons_in_group(group_id, update_group, **kwargs)
