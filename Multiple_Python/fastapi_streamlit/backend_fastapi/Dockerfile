FROM python:3.9-slim-bullseye AS base

# install required pkgs
RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y git curl iputils-ping

# create virtual environment and install python pkgs
RUN python -m venv /venv
ENV PATH=/venv/bin:$PATH
RUN python -m pip install --upgrade pip

RUN python -m pip install numpy==1.23.0
RUN python -m pip install pandas==1.4.2
RUN python -m pip install fastapi==0.68.2
RUN python -m pip install pydantic==1.9.1
RUN python -m pip install uvicorn==0.18.1

# set up env var
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1

FROM base as final-islocaldevelopment-false

# create a user
RUN useradd -ms /bin/bash pred
WORKDIR /home/pred
COPY . .

# change owner of a given directory
RUN chown -R pred:pred /home/pred 
RUN chmod 755 /home/pred
USER pred

# Expose port 
EXPOSE 5050
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5050"]

FROM base as final-islocaldevelopment-true

ENV PATH=/venv/bin:$PATH
RUN python -m pip install ipykernel==5.5.5 
RUN python -m pip install traitlets==5.0.5
RUN python -m pip install pytest
