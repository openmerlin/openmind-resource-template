FROM swr.cn-southwest-2.myhuaweicloud.com/openmind-space-base-test/base-torch-cpu:3.8-2.1.0-linux-amd64-latest-auth

# Python packages
#RUN --mount=target=requirements.txt,source=requirements.txt \
#   pip install --no-cache-dir --upgrade -r requirements.txt

# Copy the current directory contents into the container at $HOME/openMind setting the owner to the user
COPY --chown=openMind requirements.txt /tmp/
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple && pip install --no-cache-dir --upgrade -r /tmp/requirements.txt

COPY --chown=openMind . /home/openMind
#COPY --chown=openMind "." "/home/openMind"


RUN chmod +x start_server.sh

#COPY --chown=openMind login.html /home/openMind/miniconda/lib/python3.9/site-packages/jupyter_server/templates/login.html

ENV PYTHONUNBUFFERED=1 \
    GRADIO_ALLOW_FLAGGING=never \
    GRADIO_NUM_PORTS=1 \
    GRADIO_SERVER_NAME=0.0.0.0 \
    GRADIO_THEME=huggingface \
    SYSTEM=spaces \
    SHELL=/bin/bash

CMD ["./start_server.sh"]