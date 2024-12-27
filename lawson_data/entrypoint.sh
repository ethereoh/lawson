#!/bin/bash

# Load environment variables from .env file
if [ -f ".env" ]; then
    export $(cat .env | xargs)
else
    echo ".env file not found!"
    exit 1
fi

# Check if HOST and PORT are set
if [ -z "$APP_HOST" ] || [ -z "$APP_PORT" ] || [ -z "$ENVIRONMENT" ]; then
    echo "APP_HOST or APP_PORT or ENVIRONMENT is not set in the .env file."
    exit 1
fi

echo "Starting app on $APP_HOST:$APP_PORT"

fastapi $ENVIRONMENT app/main.py --port $APP_PORT --host $APP_HOST
