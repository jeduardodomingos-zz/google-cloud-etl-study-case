#!/bin/bash -e

set -exo pipefail

readonly BUILD_BUCKET = "gcp-data-load-build"
readonly ENVIRONMENT_METADATA="$(/usr/share/google/get_metadata_value attributes/environment)"
readonly ROLE="$(/usr/share/google/get_metadata_value attributes/dataproc-role)"
readonly INIT_ACTIONS_REPO="$(/usr/share/google/get_metadata_value attributes/INIT_ACTIONS_REPO || echo 'https://github.com/GoogleCloudPlatform/dataproc-initialization-actions.git')"
readonly INIT_ACTIONS_BRANCH="$(/usr/share/google/get_metadata_value attributes/INIT_ACTIONS_BRANCH || echo 'master')"

export ENVIRONMENT="${ENVIRONMENT_METADATA}"

sudo apt-get install -y build-essential python3 python-dev python3-pip

echo "Cloning fresh dataproc-initialization-actions from repo ${INIT_ACTIONS_REPO} and branch ${INIT_ACTIONS_BRANCH}..."
git clone -b "${INIT_ACTIONS_BRANCH}" --single-branch "${INIT_ACTIONS_REPO}"
(cd ./dataproc-initialization-actions; git checkout f8c7ba60cd49a4c7c031b9ca988e2fe62991d5ee)

./dataproc-initialization-actions/conda/bootstrap-conda.sh

source /etc/profile.d/conda.sh

PYTHON="$(ls /opt/conda/bin/python || which python)"
PYTHON_VERSION="$(${PYTHON} --version 2>&1 | cut -d ' ' -f 2)"

pip install --upgrade pip

gsutil cp - gs://$BUILD_BUCKET/ .

mv ./$BUILD_BUCKET ./build

pip3 install -r requirements.txt
pip3 install -e .

export PYSPARK_PYTHON=python3

cd ..