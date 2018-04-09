# Use python:3.6 xas a base image
FROM python:3.6

# Install pandas and xlrd

RUN pip install pandas  && \
    pip install matplotlib  && \
    pip install xlrd

RUN useradd -ms /bin/bash  pyuser

CMD ["python3"]

