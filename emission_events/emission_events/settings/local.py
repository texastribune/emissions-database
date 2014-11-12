##################
# LOCAL SETTINGS #
##################

import os

from .base import *


#######################
# DEBUG CONFIGURATION #
#######################

# https://docs.djangoproject.com/en/1.7/ref/settings/#debug
DEBUG = True

# https://docs.djangoproject.com/en/1.7/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG


##########################
# DATABASE CONFIGURATION #
##########################

# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
DATABASES = {
    'default': dj_database_url.config(
        default='postgres://malev@localhost:5432/emission_events'
    )
}


#######################
# CACHE CONFIGURATION #
#######################

# See: https://docs.djangoproject.com/en/1.7/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}


######################################
# DJANGO DEBUG TOOLBAR CONFIGURATION #
######################################

INSTALLED_APPS += (
    'debug_toolbar',
)
