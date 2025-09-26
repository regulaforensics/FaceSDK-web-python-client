from regula.facesdk.webclient.gen.api.group_api import GroupApi as GenGroupApi
from regula.facesdk.webclient.gen.models.group import Group
from regula.facesdk.webclient.gen.models.group_to_create import GroupToCreate


class GroupApi(GenGroupApi):
    def create_group(self, group_name: str, metadata=None, **kwargs) -> Group:
        if metadata is None:
            metadata = {}
        group_to_create = GroupToCreate(name=group_name, metadata=metadata)
        return super().create_group(group_to_create, **kwargs)
