import base64

import requests


def get_file_as_base64(file_path: str) -> str:
    with open(file_path, "rb") as f:
        file_as_binary = f.read()
    return base64.b64encode(file_as_binary).decode("utf-8")


host_url = "http://0.0.0.0:41101/api"

# create "storage" as folder in filesystem of where service is running
# do it once, and them reuse
#
# Storage is a uri location, where service store images of person.
# Thus, you can split for further processing or other needs your photo catalog.
# Can be multiple storages per application.
# During person creation, you can specify which storage to use for saving photos.
# Main property of storage is __uri__, allowing to use not only local filesystem, but other remote staff, for example aws s3 buckets etc. (Currently on filesystem is supported).
# Each person can have only one storage.
storage_to_create = {
    "uri": "appdata/photo-catalog"
}
storage_id = int(requests.post(host_url + "/storage", json=storage_to_create).json())

# create person
#################################
person_to_create = {
    "name": "Ivan Ivanov",
    "metadata": {
        "customerCustomField": 1
    },
    "storage_id": storage_id
}
person = requests.post(host_url + "/persons", json=person_to_create).json()

# add image to person
#################################
image_to_attach_to_person = {
    "image": {
        "content": get_file_as_base64("face1.jpg")
    }
}
image = requests.post(f'{host_url}/persons/{person["id"]}/images', json=image_to_attach_to_person).json()

# search person by image
#################################
search_data = {
    "image": get_file_as_base64("face1.jpg")
}
search_result = requests.post(host_url + "/search", json=search_data).json()
print(search_result)
