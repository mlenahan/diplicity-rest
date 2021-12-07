from .base import *
import dj_database_url
import django_heroku
import os

DEBUG = False

DATABASES = {
    'default': dj_database_url.parse(os.environ['DATABASE_URL'])
}

SECRET_KEY = os.environ['SECRET_KEY']

django_heroku.settings(locals())
