import os

API_URL = os.environ.get("PYTHON_API_URL") if os.environ.get("PYTHON_API_URL") else 'https://api.moonshots.cl/benefits'
