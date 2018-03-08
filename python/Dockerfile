# Use Ubuntu 16.04 as a base image
FROM python:3.6

# Install pandas and xlrd

RUN pip install pandas  && \
    pip install xlrd

RUN useradd -ms /bin/bash  pyuser

CMD ["/bin/bash"]
