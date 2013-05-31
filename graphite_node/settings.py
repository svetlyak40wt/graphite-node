import os
import os.path

ROOT_DIR = os.path.normpath(
    os.path.join(os.path.dirname(__file__), '..', '..', 'data'))

os.environ['GRAPHITE_CONF_DIR'] = os.path.join(ROOT_DIR, 'conf')
os.environ['GRAPHITE_STORAGE_DIR'] = os.path.join(ROOT_DIR, 'storage')

import pdb
from graphite.settings import *

ALLOWED_HOSTS = ['*']

DATABASES['default']['NAME'] = os.path.join(STORAGE_DIR, 'graphite.db')

try:
    from graphite_node.local_settings import *
except ImportError:
    pass

