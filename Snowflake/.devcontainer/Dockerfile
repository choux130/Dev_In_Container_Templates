FROM python:3.10-slim-bullseye AS base

# install required linux packages
RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y wget git curl

# install miniconda
RUN wget --no-check-certificate \
    https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
    && mkdir /root/.conda \
    && bash Miniconda3-latest-Linux-x86_64.sh -b \
    && rm -f Miniconda3-latest-Linux-x86_64.sh

ENV PATH=/root/miniconda3/bin:${PATH}

# create the conda environment
COPY environment.yml .
RUN conda env create \
    && conda init \
    && rm environment.yml

# connection configure for snowcli
RUN mkdir /root/.snowflake
# COPY ../config.toml /root/.snowflake/config.toml
# RUN chmod 0600 /root/.snowflake/config.toml