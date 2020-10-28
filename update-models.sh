#!/bin/sh

docker run --rm -v "${PWD}:/client" -v "${PWD}/../FaceRecognition-web-openapi:/definitions" \
openapitools/openapi-generator-cli generate -g python \
-i /definitions/index.yml -o /client -c /client/generator-config.json \
-t /client/generator-templates
