# Retrieved from https://github.com/jupyter/docker-stacks/blob/master/scipy-notebook/Dockerfile

FROM jupyter/minimal-notebook

MAINTAINER Landung Setiawan <landungs@uw.edu>

USER root

# libav-tools for matplotlib anim
RUN apt-get update && \
    apt-get install -y --no-install-recommends libav-tools && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

USER $NB_USER

COPY clientenvironment.yml /tmp/clientenvironment.yml

RUN cd /home/$NB_USER/ && \
    git clone https://github.com/BiG-CZ/wshp2017_tutorial_content.git tutorial_contents && \
    rm -rf /home/$NB_USER/work

# Install Python 3 packages
# use notebook-friendly backends in these images
RUN conda install -c conda-forge --quiet --yes \
    'nb_conda_kernels' \
    'ipykernel' \
    'ipywidgets' && \
    conda env create --file /tmp/clientenvironment.yml && \
    rm /tmp/clientenvironment.yml && \
    conda clean -tipsy && \
    # Activate ipywidgets extension in the environment that runs the notebook server
    jupyter nbextension enable --py widgetsnbextension --sys-prefix && \
    fix-permissions $CONDA_DIR

USER $NB_USER