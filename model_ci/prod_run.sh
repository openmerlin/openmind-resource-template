#!/bin/bash

echo ${job_id}
echo ${owner}
echo ${model_name}
echo ${commit_version_id}

export HUB_WHITE_LIST_PATHS=/home/
export logfile_path=/home/openmind/${owner}_${model_name}_${job_id}.log
export model_cache_path=/home/openmind/.cache/openmind/hub/models--${owner}--${model_name}

set -e

upload_log() {
    # upload log file to OBS
    /home/openmind/obsutil cp ${logfile_path} obs://openmind-ci/verification_ci/ -r -f 2>> ${logfile_path}
}

trap upload_log EXIT



which python

cd /home/openmind
#wget https://obs-community.obs.cn-north-1.myhuaweicloud.com/obsutil/current/obsutil_linux_arm64.tar.gz

url="https://obs-community.obs.cn-north-1.myhuaweicloud.com/obsutil/current/obsutil_linux_arm64.tar.gz"
max_retries=3
retry_delay=5
retry_count=0

pip install /home/openmind/openmind_hub-0.8.0-py3-none-any.whl

while [ $retry_count -lt $max_retries ]; do
    wget $url -O obsutil_linux_arm64.tar.gz
    if [ $? -eq 0 ]; then
        echo "Download successful!"
        break
    else
        retry_count=$((retry_count + 1))
        echo "Download failed. Retrying $retry_count/$max_retries in $retry_delay seconds..."
        sleep $retry_delay
    fi
done

if [ $retry_count -eq $max_retries ]; then
    echo "Download failed after $max_retries attempts."
    exit 1
fi

tar -xzvf obsutil_linux_arm64.tar.gz
cd obsutil_linux_arm64_*
ln -s /home/openmind/obsutil_linux_arm64_*/obsutil /home/openmind/obsutil

chmod a+rx /home/openmind/obsutil

if [ "$framework" = "PyTorch" ]; then
    export OPENMIND_FRAMEWORK=pt
else
    export OPENMIND_FRAMEWORK=ms
fi

python -u /home/openmind/verification_ci.py >> ${logfile_path} 2>&1

cd ${model_cache_path}/snapshots/${commit_version_id}

if [ -f "examples/requirements.txt" ]; then
    pip install -r examples/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple 2>> ${logfile_path}
else
    echo "requirements.txt NOT FOUND, skip dependency installation" >> ${logfile_path}
fi

if [ -f "examples/inference.py" ]; then
    cat examples/inference.py
    echo "Start inferencing..." >> ${logfile_path}
    python examples/inference.py --model_name_or_path ${model_cache_path}/snapshots/${commit_version_id} >> ${logfile_path} 2>&1
else
    echo "[ERROR] inference.py NOT FOUND" >> ${logfile_path}
    exit 1
fi
