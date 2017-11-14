# Retrieved from https://github.com/jupyter/docker-stacks/blob/master/scipy-notebook/Dockerfile

FROM jupyter/minimal-notebook:8e15d329f1e9

MAINTAINER Landung Setiawan <landungs@uw.edu>

USER root

# libav-tools for matplotlib anim
RUN apt-get update && \
    apt-get install -y --no-install-recommends libav-tools gfortran && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*;

USER $NB_USER

COPY clientenvironment.yml /home/$NB_USER/clientenvironment.yml

#RUN cd /home/$NB_USER/ && \
#    git clone https://github.com/BiG-CZ/wshp2017_tutorial_content.git tutorial_contents && \
#    rm -rf /home/$NB_USER/work

# Install Python 3 packages and Create R environment
# use notebook-friendly backends in these images
RUN conda install -c conda-forge -c r --quiet --yes \
    'nb_conda_kernels' \
    'ipykernel' \
    'ipywidgets' \
    'icu=58.*' \
    'r=3.3.2' \
    'r-xml' \
    'r-rjsonio' \
    'r-rcurl' \
    'r-yaml' \
    'r-irkernel' \
    'r-ggplot2' \
    'r-tidyverse' \
    'r-lubridate' \
    'r-devtools' \
    'r-xml2' \
    'r-rgdal' \
    'r-jsonlite' \
    'r-rodbc' \
    'r-httr' \
    'r-rvest' \
    'r-e1071' \
    'r-acepack' \
    'r-hmisc' \
    'r-mvtnorm' \
    'r-igraph' \
    'r-vegan' \
    'r-aqp' && \
    conda env create --file /home/$NB_USER/clientenvironment.yml && \
    rm /home/$NB_USER/clientenvironment.yml && \
    conda clean -tipsy && \
    # Activate ipywidgets extension in the environment that runs the notebook server
    jupyter nbextension enable --py widgetsnbextension --sys-prefix;

    # Install R packages
RUN /opt/conda/bin/R -e 'options(unzip = "internal"); devtools::install_github("ramnathv/rCharts")' && \
    /opt/conda/bin/R -e 'install.packages("WaterML", repos="http://cran.us.r-project.org")' && \
    /opt/conda/bin/R -e 'install.packages("dismo", repos="http://cran.us.r-project.org")' && \
    /opt/conda/bin/R -e 'install.packages("rgeos", repos="http://cran.us.r-project.org")' && \
    /opt/conda/bin/R -e 'install.packages("ape", repos="http://cran.us.r-project.org")' && \
    /opt/conda/bin/R -e 'install.packages("circular", repos="http://cran.us.r-project.org")' && \
    /opt/conda/bin/R -e 'options(unzip = "internal"); devtools::install_github("ncss-tech/soilDB", dependencies=FALSE, upgrade_dependencies=FALSE)' && \
    /opt/conda/bin/R -e 'options(unzip = "internal"); devtools::install_github("ncss-tech/sharpshootR", dependencies=FALSE, upgrade_dependencies=FALSE)';

RUN rm -rf /home/$NB_USER/work;

USER root

RUN echo "$NB_USER ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/notebook

USER $NB_USER