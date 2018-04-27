# Use ubuntu:18.04 as a base image
FROM ubuntu:18.04

# Install some basic tools libraries

RUN apt-get update && \
    apt-get install -y  \
    python-minimal  \
    libgfortran3   \
    bash-completion \
    wget \
    ssh \
    git &&   \
    # Perform cleanup 
    rm -rf /var/lib/apt/lists/* 

RUN useradd -ms /bin/bash  nruser

USER nruser

CMD ["/bin/bash"]

