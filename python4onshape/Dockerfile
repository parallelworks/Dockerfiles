# Use Ubuntu 16.04 as a base image
FROM ubuntu:16.04

# Install python2 and required module for running onShape python scripts

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    python-minimal \
    python-pip && \
    # upgrade pip and install required modules for onshape \
    pip install --upgrade pip  && \
    pip install setuptools  && \
    pip install requests  bx  numpy  stl  mesh  stl  numpy-stl  &&\
    # Perform cleanup \
    rm -rf /var/lib/apt/lists/* 

RUN useradd -ms /bin/bash  pyuser

USER pyuser

CMD ["/bin/bash"]
