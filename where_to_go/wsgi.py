import os
import sys

from django.core.wsgi import get_wsgi_application

path = '/home/remboinc/where_to_go_4.0'
if path not in sys.path:
    sys.path.insert(0, path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'where_to_go.settings'

application = get_wsgi_application()
