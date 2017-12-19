CalculiX Dockerfile
===================

This is a Dockerfile for Ubuntu + CalculiX + python-minimal.

current configuration
---------------------

-   based on [ubuntu:16.04](https://hub.docker.com/r/library/ubuntu/)
-   Installed using [CalculiX](http://www.calculix.de/) version 2.12 (multi-threaded version)
-   `unical` is from <http://www.calculixforwin.com/> (`CalculiXLauncher-03beta2-64bit-linux/bin/`)
-   The current version is tagged as parallelWorks/calculix:v2.12 on [docker hub](https://hub.docker.com/r/parallelworks/calculix).

Usage
-----

### Building the docker:

-   Building the docker requires unpacking the `ccx-212-patch-PW.tgz` file. After

unpacking remove the `ccx-212-patch-PW.tgz` file from the directory to make the docker images a bit smaller.

-   Build the docker image by running this command:

    ``` example
    docker build -t ubuntu16-ccx2p12 . 
    ```

### Running the docker

-   This command starts the docker and mounts the current directory to docker

    ``` example
    docker run --rm -i -t -v `pwd`:`pwd` -w `pwd` -u $(id -u):$(id -g) parallelworks/calculix:v2.12  /bin/bash 
    ```

-   A copy of the CalculiX source files are under `/opt/ccx-212-patch-PW/`
-   The CalculiX and CalculiX GraphiX executables (`ccx_2.12`, and `cgx_2.12`) are added to the path (`/usr/bin`)
-   To run CalculiX using multi-threads set the following variables:

    ``` example
    np=X
    export OMP_NUM_THREADS=$np
    export CCX_NPROC_RESULTS=$np # for subroutine calcs
    export CCX_NPROC_EQUATION_SOLVER=$np
    export NUMBER_OF_CPUS=$np
    ```

    where `X` is the number of threads. By default CalculiX runs with 1 CPU.
