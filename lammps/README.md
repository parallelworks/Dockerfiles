lammps Dockerfile
=================

This repository contains Dockerfile for LAMMPS

Current configuration
---------------------

-   Based on [ubuntu:16.04](https://hub.docker.com/r/library/ubuntu/)
-   Installs LAMMPS from gladky-anton/lammps ppa (<https://launchpad.net/~gladky-anton/+archive/ubuntu/lammps>)
-   Default user is lammpsuser (the docker file *Dockerfile.rootUser* sets the default user to `root`)

Usage
-----

Start the docker by:

``` example
docker run -it parallelworks/lammps:daily-v23.Oct.17
```
