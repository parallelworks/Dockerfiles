ubuntu-plus Dockerfile
======================

This repository contains Dockerfile for ubuntu + some basic tools/libraries

Current configuration
---------------------

-   Based on [ubuntu:18.04](https://hub.docker.com/r/library/ubuntu/)
-   Default user is nruser (the docker file *Dockerfile.rootUser* sets the default user to `root`)

Usage
-----

Start the docker by:

``` example
docker run -it parallelworks/ubuntu-plus:18.04 
```
