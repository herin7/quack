#!/bin/bash
# Install Python and pip
python -m ensurepip --upgrade
python -m pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Run Django migrations (if manage.py exists)
if [ -f "manage.py" ]; then
    python manage.py migrate
fi