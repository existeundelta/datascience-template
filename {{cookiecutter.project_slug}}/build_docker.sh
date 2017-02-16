#!/bin/bash

docker build -t {{cookiecutter.project_slug}}/dataservice:latest -f docker/Dockerfile .
