# Use Ubuntu 14.04 as a base image
FROM ubuntu:14.04

# Install:
#  - python2  for running the workflow
#  - expect for installing the interactive EnergyPlus installer 

# Copy the current directory contents into the container at /tmp
ADD . /tmp

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    python-minimal \
    python-pip \
    zip \
    expect \
    dos2unix && \
    # install EnergyPlus 
    cd /tmp  && \
    chmod +x EnergyPlus-8.8.0-7c3bbe4830-Linux-x86_64.sh && \
    ./install_EnergyPlus.sh  && \
    # Test installation 
    energyplus --version && \
    # Perform cleanup 
    apt-get purge -y --auto-remove expect && \
    rm EnergyPlus-8.8.0-7c3bbe4830-Linux-x86_64.sh  && \
    rm -rf /var/lib/apt/lists/* 

RUN useradd -ms /bin/bash  epuser

USER epuser

CMD ["/bin/bash"]
