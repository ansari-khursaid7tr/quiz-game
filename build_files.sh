#!/bin/bash

echo "Building project packages..."
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

echo "Collecting static files..."
python3 manage.py collectstatic --no-input

echo "Making necessary migrations..."
python3 manage.py makemigrations
python3 manage.py migrate

echo "Loading Questions..."
python3 manage.py load_questions

echo "Build script completed successfully"