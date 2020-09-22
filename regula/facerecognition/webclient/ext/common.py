import base64

Base64String = str


def bytes_to_base64(payload: bytes):
    return base64.b64encode(payload).decode("utf-8")
