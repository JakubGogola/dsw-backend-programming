#!/bin/bash

docker pull openapitools/openapi-generator-cli

docker run --rm -v ${PWD}:/local openapitools/openapi-generator-cli generate \
    -i /local/open-api-example-spec.yaml \
    -g python-fastapi \
    -o /local/backend

docker run --rm -v ${PWD}:/local openapitools/openapi-generator-cli generate \
    -i /local/open-api-example-spec.yaml \
    -g python \
    -o /local/client
