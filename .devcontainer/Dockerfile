ARG BASE_IMAGE=lcas.lincoln.ac.uk/devcontainer/ros2-teaching:4
FROM ${BASE_IMAGE}

WORKDIR $HOME

RUN sudo apt-get update && sudo apt-get install -y \
    python3-venv

RUN python3 -m venv ~/.venv

COPY requirements.txt .
RUN bash -c "source ~/.venv/bin/activate; pip install -U -r requirements.txt"




