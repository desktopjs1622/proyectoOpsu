"""
WSGI config for opsu project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

# Librerias Standard
# Standard Library
import os
import sys

# Librerias Django
# Django Library
from django.core.wsgi import get_wsgi_application

sys.path.append("/var/www/envOpsu/opsud")


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "opsu.settings")

application = get_wsgi_application()
