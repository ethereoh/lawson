#!/bin/bash

docker compose -f docker-compose.lawson.db.yaml up -d 
docker compose -f docker-compose.lawson.milvus.gpu.yaml up -d