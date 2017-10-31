# Retrieved from https://github.com/jupyter/docker-stacks/blob/master/scipy-notebook/Dockerfile

FROM jupyter/minimal-notebook:8e15d329f1e9

MAINTAINER Landung Setiawan <landungs@uw.edu>

USER root

# libav-tools for matplotlib anim
RUN apt-get update && \
    apt-get install -y --no-install-recommends libav-tools && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*;

USER $NB_USER

COPY clientenvironment.yml /home/$NB_USER/clientenvironment.yml

#RUN cd /home/$NB_USER/ && \
#    git clone https://github.com/BiG-CZ/wshp2017_tutorial_content.git tutorial_contents && \
#    rm -rf /home/$NB_USER/work

# Install Python 3 packages and Create R environment
# use notebook-friendly backends in these images
RUN conda install -c conda-forge --quiet --yes \
    'nb_conda_kernels' \
    'ipykernel' \
    'ipywidgets' && \
    conda env create --file /home/$NB_USER/clientenvironment.yml && \
    rm /home/$NB_USER/clientenvironment.yml && \
    conda clean -tipsy && \
    # Activate ipywidgets extension in the environment that runs the notebook server
    jupyter nbextension enable --py widgetsnbextension --sys-prefix;

    # Install R packages
RUN /opt/conda/envs/odm2client/bin/R -e 'options(unzip = "internal"); devtools::install_github("ramnathv/rCharts")' && \
    /opt/conda/envs/odm2client/bin/R -e 'install.packages("WaterML", repos="http://cran.us.r-project.org")';

RUN rm -rf /home/$NB_USER/work;

USER root

RUN echo "$NB_USER ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/notebook

USER $NB_USER