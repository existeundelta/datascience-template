#!/bin/bash

rm dist/invalcor.tar
docker build -t invalcor:latest -f docker/Dockerfile .
docker save -o dist/invalcor.tar invalcor
