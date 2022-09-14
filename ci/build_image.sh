#!/bin/bash
set -x

IMAGE=test-image:$CI_COMMIT_REF_NAME

echo "release image $IMAGE"
echo "xxxx" > Dockerfile
echo "pip install -r requirements.txt --no-cache-dir" >> Dockerfile
cat Dockerfile
/kaniko/executor ....
