# Regula Face SDK web API Python 3.5+ client

[![OpenAPI](https://img.shields.io/badge/OpenAPI-defs-8c0a56?style=flat-square)](https://github.com/regulaforensics/FaceSDK-web-openapi)
[![documentation](https://img.shields.io/badge/docs-en-f6858d?style=flat-square)](https://support.regulaforensics.com/hc/en-us/articles/115000916306-Documentation)
[![live](https://img.shields.io/badge/live-demo-0a8c42?style=flat-square)](https://faceapi.regulaforensics.com/)

## ⚠️ Warning: Package Name Changed
## Package name has been changed from `regula.facesdk.webclient` to `regula_facesdk_webclient`

Face recognition as easy as reading two bytes.

If you have any problems with or questions about this client, please contact us
through a [GitHub issue](https://github.com/regulaforensics/FaceSDK-web-python-client/issues).
You are invited to contribute [new features, fixes, or updates](https://github.com/regulaforensics/FaceSDK-web-python-client/issues?q=is%3Aissue+is%3Aopen+label%3A%22help+wanted%22), large or small; 
We are always thrilled to receive pull requests, and do our best to process them as fast as we can.
See [dev guide](./dev.md)

## Install package
`regula_facesdk_webclient` is on the Python Package Index (PyPI):

```bash
pip install regula_facesdk_webclient
```

Or using `pipenv`
```bash
pipenv install regula_facesdk_webclient
```

## Example
Performing request:

```python
from regula_facesdk_webclient import *

with open("face1.jpg", "rb") as f:
    face_1_bytes = f.read()

with open("face2.jpg", "rb") as f:
    face_2_bytes = f.read()

with MatchingApi(host="http://0.0.0.0:41101/api") as api:
    images = [
        MatchImage(index=1, data=face_1_bytes, type=ImageSource.LIVE),
        MatchImage(index=2, data=face_1_bytes, type=ImageSource.DOCUMENT_RFID),
        MatchImage(index=3, data=face_2_bytes)
    ]
    match_request = MatchRequest(images=images)
    match_response = api.match(match_request)

    detect_request = DetectRequest(face_1_bytes)
    detect_response = api.detect(detect_request)
```

You can find more detailed guide and run this sample in [example](./example) folder.
