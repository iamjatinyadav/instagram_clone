"""
ASGI config for Instagram_clone project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Instagram_clone.settings')

application = get_asgi_application()
