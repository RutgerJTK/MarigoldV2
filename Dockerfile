# Dockerfile

FROM public.ecr.aws/lambda/python:3.13

# Install system dependencies required for lxml and other packages
RUN yum update -y && \
    yum install -y libxml2-devel libxslt-devel gcc gcc-c++ make && \
    yum clean all

# Copy your application code
COPY . ${LAMBDA_TASK_ROOT}

# Install Python dependencies
RUN pip install -r requirements.txt

