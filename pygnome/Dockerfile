# This dockerfile installs pygnome, post_gnome and geopy on ubuntu 16.04 

# Use Ubuntu 16.04 as a base image
FROM ubuntu:16.04

RUN apt-get update && \
    apt-get install -y  \
    wget    \
    git	    \
	bzip2   \
	gcc		\
	g++		\
	python-setuptools  \
	libhdf5-serial-dev \
	libnetcdf-dev  &&  \
    # Download and install miniconda \
    wget https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh &&  \
    bash   Miniconda2-latest-Linux-x86_64.sh  -b -p /miniconda  && \
    rm   Miniconda2-latest-Linux-x86_64.sh && \
    export PATH="/miniconda/bin:$PATH"  && \
    # add the NOAA-ORR-ERD channel \
    conda update -y conda && \
    conda config --add channels NOAA-ORR-ERD && \
    conda config --add channels conda-forge && \
    # install pygnome \
    mkdir /gnome && \
    cd /gnome/   && \
    # clone the repo \
    git clone https://github.com/NOAA-ORR-ERD/PyGnome && \
    cd PyGnome/   && \
    # Some of the files don't exist under the master branch and make the tests to fail.  \
    # Get them from the develop branch  \
    git checkout develop && \
    git checkout master  && \
    git checkout develop -- py_gnome/gnome/utilities/geometry/poly_clockwise.py && \
    git checkout develop -- py_gnome/gnome/utilities/surface_concentration.py  && \
    git checkout develop -- py_gnome/gnome/utilities/serializable_demo_objects.py && \
    git checkout develop -- py_gnome/gnome/environment/timeseries_objects_base.py  && \
    git checkout develop -- py_gnome/gnome/environment/water.py  && \
    git checkout develop -- py_gnome/tests/unit_tests/sample_data/florida_with_lake_small.bna && \
    git checkout develop -- py_gnome/gnome/scripting/time_utils.py && \
    # install the requirements \
    conda install -y --file conda_requirements.txt && \
    # install the oil_library \
    cd py_gnome/ && \
    pip install --upgrade pip && \
    pip install git+https://github.com/NOAA-ORR-ERD/OilLibrary.git && \
    pip install pyHamcrest && \
    pip install argparse && \
    # install py_gnome \
    python setup.py develop && \
    conda install -y geopy && \
    cd /gnome/ && \
    # install post_gnome \
    git clone https://github.com/NOAA-ORR-ERD/GnomeTools.git && \
    cd GnomeTools/post_gnome/ && \
    conda install -y --file requirements.txt && \
    python setup.py install && \
    echo 'export PATH="/miniconda/bin:$PATH"' >> /root/.bashrc && \
    # Perform cleanup \
    rm -rf /var/lib/apt/lists/* && \
    conda clean -y --tarballs 

RUN useradd -ms /bin/bash  pygnomeuser

USER pygnomeuser

ENV PATH="/miniconda/bin:${PATH}"

CMD ["/bin/bash"]
