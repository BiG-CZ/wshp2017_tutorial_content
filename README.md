# Tutorial Contents, BiG CZ user workshop, Nov. 15-16, 2017

This repository contains tutorial (hands-on demos) materials (Jupyter notebooks, supporting code, data files, and conda environment files) for the BiG CZ user workshop, November 15-16, 2017. It is intended for `git` cloning into your personal [JupyterHub](https://jupyterhub.readthedocs.io) user space or your local computer. 

## Access JupyterHub

Go to http://jupyterhub.bigcz.org. You'll need your github `user name` for access and to create your own user space on the server. Access validation will need to be done only once.

Once you're on JupyterHub, click on the "Start My Server" button and wait a bit until the `Jupyter Notebooks` is shown.

## Load tutorial materials from github

1. On the `Jupyter Notebooks` interface, on the upper right click on the "New" button and select `Other: Terminal` to start a terminal (shell) session. A new browser tab or window will be opened, and the terminal will start on your home account directory, `/home/jovyan`.
2. "Clone" the github tutorial repository by entering the following command (you can copy and paste):
    ```bash
    git clone https://github.com/BiG-CZ/wshp2017_tutorial_content.git
    ```
A new directory will be created with the tutorial materials at the directory path `/home/jovyan/wshp2017_tutorial_content`. All tutorial work will be done under this directory.
3. Finally, exit the terminal by typing `exit` and closing the terminal browser tab or window.

On Jupyter Notebook you will now see a `wshp2017_tutorial_content` folder. Click on it, then click on the `notebooks` directory.

## Updating or reloading tutorial materials from github

As you work with notebooks, you may make changes to the notebook or data files that you'd like to undo or can no longer fix. In addition, the tutorial github repository may be updated after you cloned it. To discard your tutorial files and reload from github:
1. Open a terminal from Jupyter Notebooks.
2. Change to the tutorial directory by typing this command:
    ```bash
    cd /home/jovyan/wshp2017_tutorial_content
    ```
3. Update from github with these commands:
    ```bash
    git reset --hard && git clean -f
    git pull
    ```
4. Exit the terminal window (see instructions above)


## Docker (to be ignored by everyone but the JupyterHub admin)
Docker image of the jupyter notebook environment can be found
[here](https://hub.docker.com/r/odm2/bigczworkshop/). This is only used by the JupyterHub admin to create the conda environments for everyone on JupyterHub.
