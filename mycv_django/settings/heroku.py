
import dj_database_url
import django_heroku

from .base import *  # noqa: F401,F403

# Activate Django-Heroku.
django_heroku.settings(locals())

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config(conn_max_age=600, ssl_require=True)
}
