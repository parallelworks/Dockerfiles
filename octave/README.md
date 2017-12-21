Octave Dockerfile
=================

This is a Dockerfile for Ubuntu + GNU Octave

current configuration
---------------------

-   based on [ubuntu:16.04](https://hub.docker.com/r/library/ubuntu/)
-   [GNU Octave](https://www.gnu.org/software/octave/) version 4.0.0
-   The current version is tagged as parallelWorks/octave:v4.0.0 on [docker hub](https://hub.docker.com/r/parallelworks/calculix).

Usage
-----

### Building the docker:

-   Build the docker image by running this command:

    ``` example
    docker build -t ubuntu16-octave . 
    ```

-   To build a docker with `root` as the default login user copy `Dockerfile_rootUser` to `Dockerfile`.

### Running the docker

-   This command starts the docker and mounts the current directory to docker and deletes the docker container after exit:

    ``` example
    docker run --rm -i -t -v `pwd`:`pwd` -w `pwd` -u $(id -u):$(id -g) parallelworks/octave:v4.0.0 /bin/bash 
    ```
