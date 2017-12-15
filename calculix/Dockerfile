# Use Ubuntu 16.04 as a base image
FROM ubuntu:16.04

# This dockerfile does the following:
#
#  - Install the required packages for compiling calculix
#  - Put a copy of pre-compiled ccx_2.12 under /opt and add a link  to /usr/bin
#  - Add a link to cgx_2.12 under /usr/bin

# Copy the current directory contents into the container at /opt
ADD . /opt

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gfortran \
	make \
	f2c	\
	liblapack3 \
	liblapack-dev  \
	libexodusii-dev	\
	libgl1-mesa-dev	 \
	libglu1-mesa-dev \
	libxi-dev \
	libxmu-dev \
    git &&   \
    # Add links to ccx and cgx
    ln -s /opt/ccx-212-patch-PW/src/ccx_2.12_MT /usr/bin/ccx_2.12    && \
    ln -s /opt/cgx_2.12  /usr/bin/cgx_2.12   && \
    # Perform cleanup 
    rm -rf /var/lib/apt/lists/* 

RUN useradd -ms /bin/bash  ccxuser

USER ccxuser

CMD ["/bin/bash"]
