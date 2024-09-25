# Pull the official base image
FROM python:3.11
# Set environment variables

#prevent Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE 1

#ensure Python output is sent directly to the terminal without buffering 
ENV PYTHONUNBUFFERED 1

# Install different Linux packages.
RUN apt-get update  && apt-get install gcc postgresql postgresql-contrib libpq-dev python3-dev netcat-traditional -y  && apt-get clean

# set working directory and install packages using pip.
WORKDIR /app
COPY ./requirements /app/requirements

RUN pip install --upgrade pip -r requirements/requirements-base.txt

# Copy the Application code
COPY . /app/
COPY ./entrypoint.sh /app/entrypoint.sh

# Give permission to entrypoint.sh file as executable.
RUN chmod +x /app/entrypoint.sh
# run entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]