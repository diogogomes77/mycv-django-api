
# import dj_database_url
import django_heroku

from .base import *  # noqa: F401,F403

# Activate Django-Heroku.
django_heroku.settings(locals())
