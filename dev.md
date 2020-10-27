# Development

Client is written using python, mainly generated from [OpenAPI spec](https://github.com/regulaforensics/FaceRecognition-web-openapi). 
Openapi-generator output used as implementation base(see packages `regula/facerecognition/webclient/gen`). 
All custom logic, on top of generated files, should be places in `regula/facerecognition/webclient/ext` folder.

To regenerate models, clone [latest OpenAPI definitions](https://github.com/regulaforensics/FaceRecognition-web-openapi)
and use next command from the project root:
```bash
./update-models.sh
```
