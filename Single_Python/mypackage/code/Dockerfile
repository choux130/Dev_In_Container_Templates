FROM python:3.9-slim-bullseye AS base

# install required pkgs
RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y git curl iputils-ping

# create virtual environment and install python pkgs
RUN python -m venv /venv
ENV PATH=/venv/bin:$PATH
RUN python -m pip install --upgrade pip

RUN python -m pip install build==0.8.0
RUN python -m pip install wheel==0.37.1
RUN python -m pip install twine==4.0.1
RUN python -m pip install pytest==7.1.1

# set up env var
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1

FROM base as final-islocaldevelopment-false

# create a user
RUN useradd -ms /bin/bash pred
WORKDIR /home/pred
COPY . .

# run unit tests
RUN python -m pytest tests/

# build the package
# RUN python setup.py sdist

# install the package from the source code
RUN python -m pip install .

CMD ["sleep", "infinity"]

FROM base as final-islocaldevelopment-true

ENV PATH=/venv/bin:$PATH
RUN python -m pip install ipykernel==5.5.5 
RUN python -m pip install traitlets==5.0.5
