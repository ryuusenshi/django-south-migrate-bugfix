"""
    Settings for shell tinkering

    Originally, same as test settings with the exception of
    the database residing on the disk in the form of ``test.db``

    Alter to your liking

"""
from testconf.settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test.db',
    },
}
