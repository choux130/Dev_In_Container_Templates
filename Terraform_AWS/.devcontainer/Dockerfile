FROM python:3.10-slim-bullseye AS base

# install required linux packages
RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y wget git curl gettext-base

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

# install aws cli
RUN apt-get install -y unzip
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && \
    unzip awscliv2.zip && \
	./aws/install

# install terraform
RUN curl "https://releases.hashicorp.com/terraform/1.5.7/terraform_1.5.7_linux_amd64.zip" -o "terraform.zip" && \
    unzip terraform.zip && rm terraform.zip && \
    mv terraform /usr/local/bin/ 
