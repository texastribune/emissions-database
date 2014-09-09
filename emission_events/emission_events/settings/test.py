#################
# TEST SETTINGS #
#################

from .base import *


###########################
# IN-MEMORY TEST DATABASE #
###########################

# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
        "USER": "",
        "PASSWORD": "",
        "HOST": "",
        "PORT": "",
    },
}
