"""
Bot settings module.
"""
from decouple import config

__version__ = '0.0.0'

TOKEN = config('TOKEN', '')
BACKEND_URL = config('BACKEND_URL')
