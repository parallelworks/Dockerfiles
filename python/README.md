python-tools Docker file
========================

This repository contains Dockerfile for python + numpy, pytz, six, python-dateutil, pandas and xlrd modules

Current configuration
---------------------

-   Based on [python:3.6](https://hub.docker.com/_/python/)
-   has these additional modules: numpy, pytz, six, python-dateutil, pandas and xlrd
-   Default user is root (the docker file *Dockerfile.pyuser* sets the default user to `pyuser`)

Usage
-----

Start the docker by:

``` example
docker run -it parallelworks/python-tools:v3.6-pandas_rootuser
```
