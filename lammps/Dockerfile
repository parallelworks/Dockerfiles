# Use Ubuntu 16.04 as a base image
FROM ubuntu:16.04

# Install LAMMPS
# This command installs LAMMPS from gladky-anton/lammps ppa

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    	    apt-transport-https \
	    software-properties-common && \
    # add gladky-anton/lammps ppa 
    add-apt-repository ppa:gladky-anton/lammps	&& \
    apt-get update && \
    apt-get install  -y  lammps-daily && \
    # Perform cleanup \
    apt-get remove --purge -y \
        software-properties-common && \
    rm -rf /var/lib/apt/lists/* 

RUN useradd -ms /bin/bash  lammpsuser

USER lammpsuser

CMD ["/bin/bash"]
