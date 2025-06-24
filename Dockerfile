# Dockerfile

FROM public.ecr.aws/lambda/python:3.13
FROM public.ecr.aws/lambda/python:3.13

# Copy your application code
COPY . ${LAMBDA_TASK_ROOT}

# Install Python dependencies
RUN pip install -r requirements.txt

