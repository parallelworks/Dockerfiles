# Use Ubuntu with xvfb installed as a base image
FROM marmarm/xvfb:v2

# Copy the current directory contents into the container at /app
ADD . /opt/

# Install imagemagick to make images and python-dateutil package so that matplotlib.pyplot is loadable from inside pvpython 
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    python-pip \
    imagemagick && \
    # install python-dateutil in paraview \
    pip2 install --target=/opt/ParaView-5.4.0-Qt5-OpenGL2-MPI-Linux-64bit/lib/python2.7/site-packages python-dateutil && \
    # Perform cleanup \
    rm -rf /var/lib/apt/lists/* 


# Add user so that we don't have to run as root
RUN useradd -ms /bin/bash  pvuser 

USER pvuser


# Define environment variable
ENV PATH="/opt/ParaView-5.4.0-Qt5-OpenGL2-MPI-Linux-64bit/bin/:${PATH}"

