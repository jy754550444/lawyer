"""
WSGI config for lawyer project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os,sys

from django.core.wsgi import get_wsgi_application

sys.path.append('D:/xampp/htdocs/lawyer')
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lawyer.settings")

os.environ["DJANGO_SETTINGS_MODULE"] = "lawyer.settings"

application = get_wsgi_application()