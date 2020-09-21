# Development

To regenerate models, clone [latest OpenAPI definitions](https://github.com/regulaforensics/FaceRecognition-web-openapi)
and set `FACER_DEFINITION_FOLDER` as path to cloned directory, for example:
```bash
FACER_DEFINITION_FOLDER="/home/user/projects/FaceRecognition-web-openapi"
```
Then use next command from the project root:
```bash
docker run --rm -v "${PWD}:/client" -v "${FACER_DEFINITION_FOLDER}:/definitions" \
openapitools/openapi-generator-cli generate -g python \
-i /definitions/index.yml -o /client -c /client/generator-config.json \
-t /client/generator-templates
```
