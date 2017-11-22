EnergyPlus Dockerfile
=====================

This is a Dockerfile for Ubuntu + EnergyPlus + python-minimal.

Current configuration
---------------------

-   Based on [ubuntu:14.04](https://hub.docker.com/r/library/ubuntu/)
-   Installed using [EnergyPlus](https://energyplus.net/) [version 8.6](https://github.com/NREL/EnergyPlus/releases/tag/v8.6.0)
-   The current version is tagged as parallelWorks/energyplus:v8p6 on [docker hub](https://hub.docker.com/r/parallelworks/energyplus/docker).

Usage
-----

### Building the docker:

-   Building the docker using the Dockerfile requires downloading the energy plus installer from <https://github.com/NREL/EnergyPlus/releases/tag/v8.6.0>
-   Build the docker image by running this command:

    ``` example
    docker build -t ep-8p6 . 
    ```

### Running the docker

-   This command starts the docker and mounts the current directory to docker

    ``` example
    docker run --rm -i -t -v `pwd`:`pwd` -w `pwd` -u $(id -u):$(id -g) parallelworks/energyplus:v8p6  /bin/bash 
    ```
