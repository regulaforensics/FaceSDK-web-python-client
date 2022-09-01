#!/bin/sh

docker run --rm --user "$(id -u):$(id -g)" -v "${PWD}:/client" -v "${PWD}/../FaceSDK-web-openapi:/definitions" \
openapitools/openapi-generator-cli:v5.4.0 generate -g python \
-i /definitions/index.yml -o /client -c /client/generator-config.json \
-t /client/generator-templates
