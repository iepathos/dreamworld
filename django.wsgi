import os
import sys

path = '/home/ubuntu/dreamworld'
if path not in sys.path:
	sys.path.insert(0, '/home/ubuntu/dreamworld')

os.environ['DJANGO_SETTINGS_MODULE'] = 'dreamworld.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()