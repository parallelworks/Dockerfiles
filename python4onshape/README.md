python4OnShape Dockerfile
=========================

This repository contains Dockerfile of Ubuntu + minimal Python (python2) + pip + some modules required for running OnShape Python scripts

Notes on installing modules:
----------------------------

Installing the `stl` package may lead to an error when running onshape scripts that use the `stl` package. To resolve this issue `numpy-stl` module should be updated[1]

Current configuration
---------------------

-   Based on [ubuntu:16.04](https://hub.docker.com/r/library/ubuntu/)
-   Python version: 2.7
-   I have only tested to run genshape from CASE workflow
-   The current version is tagged as marmarm/python4onshape:v0 on docker hub.

Usage
-----

### Building the docker:

-   Build the docker image by running this command:

    ``` example
    docker build -t python4OnShape . 
    ```

### Running the docker

-   This command starts the docker and mounts the current directory to docker

    ``` example
    docker run --rm -i -t -v `pwd`:`pwd` -w `pwd` -u $(id -u):$(id -g) marmarm/python4onshape:v0    /bin/bash 
    ```

Footnotes
=========

[1] See [Importing of 3D STL Image in Python (ImportError: No module named ascii) (on stackoverflow)](https://stackoverflow.com/questions/29661823/importing-of-3d-stl-image-in-python-importerror-no-module-named-ascii)
