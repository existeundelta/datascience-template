#!/bin/bash

rm dist/{{cookiecutter.project_slug}}.tar
docker build -t {{cookiecutter.project_slug}}:latest -f docker/Dockerfile .
docker save -o dist/{{cookiecutter.project_slug}}.tar {{cookiecutter.project_slug}}
