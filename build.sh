#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt
python agenda/manage.py collectstatic --no-input
python agenda/manage.py migrate