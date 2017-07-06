Paraview Docker file
====================

This repository contains Dockerfile of Ubuntu + Paraview + imagemagick

Current configuration
---------------------

-   Based on marmarm/xvfb which has xvfb installed on [ubuntu:14.04](https://hub.docker.com/r/library/ubuntu/)
-   Installed using ParaView-5.4.0
-   I have only tested to run pvpython via xvfb run
-   The current version is tagged as marmarm/paraview:v5\_4u\_imgmagick on docker hub.

Usage
-----

### Building the docker:

-   Building the docker using the Dockerfile requires downloading the Paraview binary from <https://www.paraview.org/download/> and unpacking the archive. Then remove the .tar.gz file from the directory to make the building process a bit faster.
-   Build the docker image by running this command:

    ``` example
    docker build -t paraview-v5-4 . 
    ```

### Running the docker

-   This command starts the docker and mounts the current directory to docker

    ``` example
    docker run --rm -i -t -v `pwd`:`pwd` -w `pwd` -u $(id -u):$(id -g) marmarm/paraview:v5_4u_imgmagick   /bin/bash 
    ```

-   Example command for running pvpython

    ``` example
    xvfb-run -a --server-args="-screen 0 1024x768x24" pvpython --mesa-llvm saveSphere.py 
    ```
