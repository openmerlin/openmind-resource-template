import os
import sys
import subprocess
from openmind_hub import snapshot_download

OWNER = os.environ.get('owner')
if not OWNER:
    raise Exception('OWNER is not set')
MODEL_NAME = os.environ.get('model_name')
if not MODEL_NAME:
    raise Exception('MODEL_NAME is not set')
TEST_TYPE = os.environ.get('testType')
# if not TEST_TYPE:
#     raise Exception('TEST_TYPE is not set')
COMMIT_ID = os.environ.get('commit_version_id')
if not COMMIT_ID:
    raise Exception('COMMIT_ID is not set')


def main(owner: str, model_name: str, commit_id: str, test_type='customized'):
    print('Start downloading model...')
    repo_id = f'{owner}/{model_name}'
    snapshot_download(
        repo_id=repo_id,
        revision=commit_id,
    )
    print('Download success...')


if __name__ == '__main__':
    try:
        main(OWNER, MODEL_NAME, COMMIT_ID, TEST_TYPE)
    except Exception as e:
        print(e)
        sys.exit(1)