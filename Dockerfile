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

# Install Python 3 packages
# Remove pyqt and qt pulled in for matplotlib since we're only ever going to
# use notebook-friendly backends in these images
RUN conda install -c conda-forge --quiet --yes \
    'nb_conda_kernels' \
    'ipykernel' && \
    conda create -n odm2client -c odm2 -c conda-forge --quiet --yes \
    'odm2api' \
    'yodatools' \
    'requests' \
    'folium' \
    'geopandas' \
    'ulmo' \
    'owslib' \
    'scipy' \
    'xarray' \
    'ipykernel' && \
    conda clean -tipsy && \
    # Activate ipywidgets extension in the environment that runs the notebook server
    jupyter nbextension enable --py widgetsnbextension --sys-prefix && \
    fix-permissions $CONDA_DIR

USER $NB_USER