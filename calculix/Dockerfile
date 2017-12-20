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
    time \
    git &&   \
    # Compile spooles   
    cd /opt/ccx-212-patch-PW/spooles.2.2/    && \
	make lib    && \
	cd MT/src/   && \
	make   && \
	# Compile ARPACK   
	cd /opt/ccx-212-patch-PW/ARPACK/   && \
	make lib   && \
	# removes the object files, but keep the library  
	make clean && \
	# Compile ccx_2.12_MT   
    cd /opt/ccx-212-patch-PW/src  && \
    make  && \
    cp /opt/ccx-212-patch-PW/src/ccx_2.12_MT /opt/CalculiX-2.12-executables/  && \
    cd /opt && \
    # Perform cleanup 
    rm -r  ccx-212-patch-PW   && \
    rm -rf /var/lib/apt/lists/* 

# Add the calculix executable path  to PATH
ENV PATH="/opt/CalculiX-2.12-executables:${PATH}"

RUN useradd -ms /bin/bash  ccxuser

USER ccxuser

# Add the calculix executable path  to PATH of ccxuser 
ENV PATH="/opt/CalculiX-2.12-executables:${PATH}"

CMD ["/bin/bash"]
