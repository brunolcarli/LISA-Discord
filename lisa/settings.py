"""
Bot settings module.
"""
import os

__version__ = '0.0.2'

TOKEN = os.environ.get('TOKEN', '')
BACKEND_URL = os.environ.get('BACKEND_URL')
ENV_REF = os.environ.get('ENV_REF', 'development')
