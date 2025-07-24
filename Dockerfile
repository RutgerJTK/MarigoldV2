FROM public.ecr.aws/lambda/python:3.12

# Install system dependencies
RUN yum update -y && yum install -y wget && yum clean all

# Copy project files
COPY . .

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Set Lambda handler
CMD ["scrapers.scraper.handler"]