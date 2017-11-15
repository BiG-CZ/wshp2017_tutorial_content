
### What is Conda?
Similar to [pip](https://pypi.python.org/pypi/pip), [**conda**](http://conda.pydata.org/docs/) is an **open source package and environment management system** for installing multiple versions of software packages, their dependencies and switching easily between them. While it originally was developed to support Python, it now supports multiple languages. It works on Linux, OS X and Windows. This [Aug. 2016 blog post](https://jakevdp.github.io/blog/2016/08/25/conda-myths-and-misconceptions/) from Jake Vanderplas provides nice clarifications about conda and where it fits in the ecosystem of Python packaging and environments. See also [this Continuum Analytics blog post for a great, comprehensive introduction to conda](http://www.continuum.io/blog/conda-data-science) targeted to data scientists; it also has links to a presentation (Youtube and slides) on the same material.

For additional help you can consult the [UW GeoHack conda introduction](https://geohackweek.github.io/Introductory/01-conda-tutorial/).

### Anaconda or Miniconda
[Anaconda](https://www.anaconda.com/what-is-anaconda/) is a data science platform that comes with a lot of packages. At the core, Anaconda uses the conda package management system. A list of packages included can be found [*here*](https://docs.anaconda.com/anaconda/packages/pkg-docs). If you don't have time or disk space -- or the inclination -- to install the entire distribution, try [Miniconda](https://conda.io/miniconda.html), a bootstrap version of Anaconda, which contains only Python, essential packages, and conda. Other packages have to be installed individually.

**NOTE: We will be using Python 2.7 for this workshop.**

### Installing Anaconda

1. To install Anaconda, please click on the link below for your operating system, and follow the instructions on the site:
  **NOTE: FOR Windows and OSX Graphical installation, make sure to do a custom install and uncheck the box `modify PATH`**
  
  ![OSX Custom Install](https://docs.continuum.io/_images/pathoption.png)
  
  - [Windows](https://docs.anaconda.com/anaconda/install/windows.html)
  - [OSX](https://docs.anaconda.com/anaconda/install/mac-os)
  - Linux: see below
  
  ```bash
  url=https://repo.continuum.io/archive/Anaconda3-5.0.1-MacOSX-x86_64.sh
  curl $url -o anaconda.sh
  bash anaconda.sh -b
  export PATH=$HOME/anaconda/bin:$PATH
  conda update --yes --all
  ```
2. Once Anaconda installation step is finished run `python` in the command line to test if Anaconda is installed correctly. **Note: For windows, please use Windows powershell as the command line. It should be preinstalled, if not click [here](https://msdn.microsoft.com/en-us/powershell/scripting/setup/installing-windows-powershell).**
If Anaconda is installed correctly, you should have this prompt, which emphasizes **Anaconda**:

```bash
$ python
Python 3.6.2 |Anaconda custom (x86_64)| (default, Dec  6 2016, 18:57:58)
[GCC 4.2.1 (Apple Inc. build 5577)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
Anaconda is brought to you by Continuum Analytics.
Please check out: http://continuum.io/thanks and https://anaconda.org
>>>
```

### Installing Miniconda

#### Windows
Navigate to https://conda.io/miniconda.html and download the proper installer for you Windows platform (32 or 64 bits).
We recommend to download the Python 3 version of Miniconda. You can still create Python 2 environments using the Python 3 verson of Miniconda, so you are not limiting yourself.

When installing you will be asked if you wish to make the Anaconda Python your default Python for Windows.
If you do not have any other installation that may be a good option.  If you want to keep multiple versions of python on your machine (e.g. ESRI-supplied python, or both 32 and 64 bit versions of Anaconda), then don't select the option to modify your path or modify your Windows registry settings.

#### Linux and OSX
You may follow manual steps from https://conda.io/miniconda.html similar to the instructions on Windows (see above). Alternatively, you can execute these commands on a terminal shell (in this case, the bash shell):

```bash
url=https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh  # On MacOSX, replace Linux with MacOSX
curl $url -o miniconda.sh
bash miniconda.sh -b
export PATH=$HOME/miniconda/bin:$PATH
conda update --yes --all
```

### Creating the `odm2client` conda environment

Download the `clientenvironment.yml` file by going to [this link](clientenvironment.yml), right clicking with the mouse and choosing `Save as...`

Open a terminal window where you saved the file and type the commands to create the environment and "activate" it.

```bash
conda env create -f clientenvironment.yml  # Will create an environment called "odm2client"
source activate odm2client  # OSX and Linux
activate odm2client # Windows
```

The `odm2client` conda environment includes `odm2api`, `yodatools`, and other python packages that are useful to interact and work with the data and metadata from odm2 ecosystem, which include `geopandas`, `scipy`, `xarray`, `folium`, `ulmo`, `requests`, and `owslib`. The dependencies of each package will be handled automatically by the conda environment. Additional conda packages available in the environment include `jupyter`, `ipykernel`, and `nb_conda_kernels`. These three packages allows for the ability to run jupyter notebook and being able to switch between conda environments within the notebook.

### Starting Jupyter notebooks

On Windows and MacOSX you may have a conda GUI application already installed, specially if you installed Anaconda. That application should let you select the `odm2client` environment, then launch Jupyter notebook with that environment.

Otherwise, on the command shell, you can launch Jupyter notebooks (after activating the environment) like this:
```bash
jupyter notebook
```

### Removing and recreating the `odm2client` conda environment

To delete the conda environment, first "deactivate" it if you've activated it in your shell session:

```bash
source deactivate  # OSX and Linux
deactivate  # Windows
```

Then remove the environment:

```bash
conda env remove -n odm2client
```

You can create it again, from scratch, using the command described earlier.
