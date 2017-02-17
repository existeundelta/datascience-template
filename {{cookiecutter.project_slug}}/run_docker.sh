#!/bin/bash

docker stop {{cookiecutter.project_slug}}
docker rm {{cookiecutter.project_slug}}
docker run --name {{cookiecutter.project_slug}} -d -p 8080:80 {{cookiecutter.project_slug}}
