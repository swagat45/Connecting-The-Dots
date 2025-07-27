#!/usr/bin/env bash
set -e
docker build -t connectdots:latest .
docker run -v $(pwd)/sample_docs:/in -v $(pwd)/out1a:/out connectdots:latest
docker run -v $(pwd)/sample_docs:/app/input -v $(pwd)/out1b:/app/output -v $(pwd)/meta:/app/meta connectdots:latest persona
echo "Smoke OK"
