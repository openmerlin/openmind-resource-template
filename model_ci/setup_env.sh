#!/bin/bash

echo "Settiing up environment..."

DEFAULT_CONFIG_FILE="/vault/internal/config.yaml"

while [[ "$#" -gt 0 ]]; do
    case $1 in
        --config-file) CONFIG_FILE="$2"; shift ;;
        *) echo "Unknown parameter passed: $1"; exit 1 ;;
    esac
    shift
done

CONFIG_FILE="${CONFIG_FILE:-$DEFAULT_CONFIG_FILE}"

if [ ! -f "$CONFIG_FILE" ]; then
    echo "Config file not found: $CONFIG_FILE"
    exit 1
fi

AK=$(grep 'ak:' $CONFIG_FILE | awk '{print $2}')
SK=$(grep 'sk:' $CONFIG_FILE | awk '{print $2}')

if [ -z "$AK" ] || [ -z "$SK" ]; then
    echo "Failed to read AK or SK from the config file"
    exit 1
fi

echo "Checking CI_ENV_NAME environment variable..."

if [ -z "$CI_ENV_NAME" ]; then
    echo "CI_ENV_NAME environment variable is not set"
    exit 1
fi

echo "Setting SLAVE_NAME and WORK_DIR..."

SLAVE_NAME="$CI_ENV_NAME"
WORK_DIR="/home/openmind/opt/$SLAVE_NAME"

echo "Downloading and installing Octopus Agent..."

export AGENT_INSTALL_URL=https://cloud-octopus-agent.obs.cn-north-4.myhuaweicloud.com/latest/install_octopus_agent.py

if [ -f "$(which curl)" ]; then
    curl -# -O -k ${AGENT_INSTALL_URL}
else
    wget --no-check-certificate ${AGENT_INSTALL_URL}
fi

echo "Running octopus agent installation script..."

python2.7 install_octopus_agent.py  \
    --cluster-id=8760cb5941d249b39a54636f5230dea1 \
    --region-id=cn-north-4 \
    --x-project-id=ffed1a78cc144c84b0069c5174758a01 \
    --obs-domain-name=cloud-octopus-agent.obs.cn-north-4.myhuaweicloud.com \
    --slave-name=$SLAVE_NAME \
    --work-dir=$WORK_DIR \
    --external-global-domain-name=myhuaweicloud.com \
    --access-key=$AK \
    --secret-access-key=$SK

cd /home/openmind

./obsutil config -i=$AK -k=$SK -e=$OBS_ENDPOINT

echo "Installation complete, entering sleep mode..."

while true; do
    sleep 3600
done