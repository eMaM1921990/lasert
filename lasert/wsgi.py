"""
WSGI config for lasert project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""
#
# import os
#
# from django.core.wsgi import get_wsgi_application
#
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lasert.settings")
#
# application = get_wsgi_application()

import os
import sys

sys.path.append('/opt/bitnami/apps/django/django_projects/lasert')
os.environ['PYTHON_EGG_CACHE']="/opt/bitnami/apps/django/django_projects/lasert/egg_cache"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lasert.settings.local")

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
