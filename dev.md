# Development

Client is written using python, mainly generated from [OpenAPI spec](https://github.com/regulaforensics/FaceSDK-web-openapi). 
Openapi-generator output used as implementation base(see packages `regula/facesdk/webclient/gen`). 
All custom logic, on top of generated files, should be places in `regula/facesdk/webclient/ext` folder.

To regenerate models from openapi definition, 
clone [latest open api definitions](https://github.com/regulaforensics/FaceSDK-web-openapi) 
to a client's parent folder ./../.
Than,use next command from the project root:
```bash
./update-models.sh
```
