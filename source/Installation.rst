Installation
============
1. Prepare Python environment
---------------------
To install `SpaGT`, we recommend using the [Anaconda](https://anaconda.org/) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html) Python Distribution and creating an isolated environment, so that the `SpaGT` and dependencies don't conflict or interfere with other packages or applications. Please install the `conda` in advance. 


Create environment 
First, please download or clone the `SpaGT.zip` file from github `Code` and unzip it. 

.. code-block:: python

    git clone https://github.com/xy428/SpaGT.git


The entire installation process takes place in the `SpaGT` directory, so first go to that directory by:

.. code-block:: python

    cd SpaGT

We recommend using a conda environment to configure SpaGT. To create and activate the environment `SpaGT_ENV`, run the following command in `bash` or `Anaconda Powershell Prompt`:  

.. code-block:: python

    conda create -n SpaGT_ENV python=3.8
    conda activate SpaGT_ENV

2. Prepare R environment
---------------------
The `SpaGT` uses the `mclust` package in the `R` language environment, and links it in a `Python` environment via `rpy2`. You can install the `R` language environment under `SpaGT_ENV` environment by:

.. code-block:: python

    conda install -c conda-forge r-base
    conda install -c conda-forge r-mclust=5.4.10


3. Install dependency packages
---------------------
If you want to install `SpaGT`, you can install the dependency packages using `pip` by:

.. code-block:: python

    pip install -r requirements.txt

4. Install SpaGT
---------------------
Install the `SpaGT` package under `SpaGT_ENV`environment by:

.. code-block:: python

    pip install setuptools==58.2.0
    python setup.py build
    python setup.py install

Here, the environment configuration is completed!

---