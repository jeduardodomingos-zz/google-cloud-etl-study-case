#!/bin/bash -e

echo "Starting Files Deploy ..."

BASE_DIR="$(dirname $0)"
BUILD_BUCKET="gcp-data-load-build"

gsutil -m rm -R "gs://gcp-data-load-build/br" "gs://gcp-data-load-build/scripts" "gs://gcp-data-load-build/setup.py" "gs://gcp-data-load-build/requirements.txt"

gsutil -m cp -R "$BASE_DIR/../br" "gs://$BUILD_BUCKET/br"
gsutil -m cp -R "$BASE_DIR/../scripts/" "gs://$BUILD_BUCKET/scripts"
gsutil -m cp -R "$BASE_DIR/../requirements.txt" "gs://$BUILD_BUCKET/requirements.txt"
gsutil -m cp -R "$BASE_DIR/../setup.py" "gs://$BUILD_BUCKET/setup.py"

echo "Finishing Files Deploy ..."
echo "Files Deploy Finished"