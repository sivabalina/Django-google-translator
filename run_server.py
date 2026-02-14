#!/usr/bin/env python
"""Run the Django WSGI app with Waitress (no console window required).

Usage (no console):
  C:\path\to\venv\Scripts\pythonw.exe run_server.py

You can set environment variables `DJANGO_HOST` and `DJANGO_PORT` to override defaults.
"""
import os
from waitress import serve

# Import the Django WSGI application
from translator_project.wsgi import application


def main():
    host = os.environ.get('DJANGO_HOST', '127.0.0.1')
    port = int(os.environ.get('DJANGO_PORT', '8000'))
    serve(application, host=host, port=port)


if __name__ == '__main__':
    main()
