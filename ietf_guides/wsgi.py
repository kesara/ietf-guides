"""
WSGI config for ietf_guides project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application
from django.conf import settings

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Virtualenv support
virtualenv_activation = os.path.join(path, "env", "bin", "activate_this.py")
if os.path.exists(virtualenv_activation):
    execfile(virtualenv_activation, dict(__file__=virtualenv_activation))

if not path in sys.path:
    sys.path.insert(0, path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings.DJANGO_SETTINGS_MODULE or "ietf_guides.settings.prod")

application = get_wsgi_application()
