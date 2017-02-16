FROM ubuntu:16.04
MAINTAINER DataScienceUB <admin@datascience.barcelona>

## APT dependencies
RUN apt-get update && apt-get install -y curl bzip2


## CONDA
RUN curl -O -L https://repo.continuum.io/archive/Anaconda2-4.3.0-Linux-x86_64.sh
RUN bash Anaconda2-4.3.0-Linux-x86_64.sh -b -p /opt/anaconda
RUN rm Anaconda2-4.3.0-Linux-x86_64.sh

# Export path
ENV PATH=/opt/anaconda/bin:/root/bin:/usr/local/bin:$PATH
ENV LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH


## Fetch project from repo
RUN mkdir /opt/{{cookiecutter.project_slug}}
COPY ./ /opt/{{cookiecutter.project_slug}}/


## Python libraries
WORKDIR /opt/{{cookiecutter.project_slug}}
RUN pip install -r requirements.txt


## Expose port 80
EXPOSE 80

ENTRYPOINT ["python", "src/service.py"]
