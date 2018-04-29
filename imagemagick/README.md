imagemagick Dockerfile
======================

This repository contains Dockerfile for imagemagick

Current configuration
---------------------

-   Based on [ubuntu:18.04](https://hub.docker.com/r/library/ubuntu/)
-   Version: ImageMagick 6.9.7-4 Q16 x86\_64 20170114 <http://www.imagemagick.org>
-   Default user is imguser (the docker file *Dockerfile.rootUser* sets the default user to `root`)

Usage
-----

Start the docker by:

``` example
docker run -it parallelworks/imagemagick:v6.9
```
