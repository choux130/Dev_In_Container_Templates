FROM rocker/r-ver:4.1.0 AS base

# install required pkgs
RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y git curl iputils-ping

# install R pkgs
RUN Rscript -e "install.packages('remotes', repos='http://cran.rstudio.com/')"
RUN Rscript -e "remotes::install_version('magrittr', version='2.0.1', upgrade='always')"
RUN Rscript -e "remotes::install_version('dplyr', version='1.0.7', upgrade='always')"
RUN Rscript -e "remotes::install_version('tidyr', version='1.1.3', upgrade='always')"
RUN Rscript -e "remotes::install_version('testthat', version='3.0.4', upgrade='always')"
RUN Rscript -e "remotes::install_version('usethis', version='2.0.1', upgrade='always')"
RUN Rscript -e "remotes::install_version('devtools', version='2.4.2', upgrade='always')"

FROM base as final-islocaldevelopment-false

# create a user
RUN useradd -ms /bin/bash pred
WORKDIR /home/pred
COPY . .

# run unit tests
RUN Rscript -e "devtools::test(reporter = c('summary', 'fail'))"

# build the package
RUN Rscript -e "devtools::build(path='./')"
RUN Rscript -e "devtools::install()"

CMD ["sleep", "infinity"]

FROM base as final-islocaldevelopment-true

# install Rstudio Server
EXPOSE 8787
ENV DISABLE_AUTH=True
ENV S6_VERSION=v2.1.0.2
ENV RSTUDIO_VERSION=2022.02.2+485
ENV PASSWORD=rstudio
ENV DEFAULT_USER=rstudio
ENV PANDOC_VERSION=default
ENV PATH=/usr/lib/rstudio-server/bin:$PATH
ENV DISABLE_AUTH=true

RUN /rocker_scripts/install_rstudio.sh
RUN /rocker_scripts/install_pandoc.sh

