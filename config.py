"""
    Configuration utility for python distutils

    Provide all the info about your python project here
"""
class ImproperlyConfigured(Exception):
    pass

# Change the import package to fit your project
#
# If your app/project resided in directory ``moderated_actions``
# then write ``import moderated_actions as project``
import djsouth as project


# The name of your python package/project.
#
# This name will be used by the package manager
# to register the package locally
# and by PyPi to register the package within its database.
NAME = 'django-south-migrate-bugfix'


# Type of license used for your package/project
# e.g. Apache License, Version 2.0 
LICENSE = ''


# Short text description of your project
DESCRIPTION = ''


# The author's name. Distutils dictates that it must be a string.
# If there are multiple authors, provide authors as
# a comma separated list
AUTHOR_NAME = ''


# The author's email. Distutils dictates that it must be a string.
# Even if there are multiple authors, provide a single email,
# for the entire group (e.g. support mailing list email)
AUTHOR_EMAIL = ''


# The URL of where to find the project online (must be a valid URL)
# i.e. the homepage for the package
# e.g. https://github.com/ryuusenshi/django-moderated-actions 
URL = ''


# The URL of where to download the project online (must be a valid URL)
# e.g. https://github.com/ryuusenshi/django-moderated-actions/releases
DOWNLOAD_URL = ''


# Python path to the python function that is the test suite runner
#
# The boilerplate provides as django test runner within: testconf.testrunner.main
TEST_SUITE = 'testconf.testrunner.main'


# List of additional requirements for the testing enviroment
#
# Should be a list of package names if packages are available on PyPi
# or urls if they're available elsewhere
TEST_REQUIREMENTS = [
]


# List of packages to exclude when building/installing
#
# These are packages included in the install directory
# that should not be distributed in the final build
EXCLUDE_PACKAGES = [
    'testconf',  # default test configuration
]


# List of classifiers, used by PyPi to tag your package
#
# for a list of valid classifiers see:
# https://pypi.python.org/pypi?%3Aaction=list_classifiers
#
# It's recommended that the followingf classifiers be provided:
#   Environment, Intended Audience, License, Operating System
#   Programming Language, Framework (if any)
#
# An example is shown below:
"""
    'Environment :: Web Environment',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: Apache Software License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Framework :: Django',
"""
# Note: classifier ``Development Status`` will be automatically
# set based on your package version
CLASSIFIERS = [
]

def _get_attribute(name):
    try:
        return globals()[name]
    except KeyError:
        raise ImproperlyConfigured(
            'Your ``config.py`` must define a ``%s`` attribute' % name
        )

def get_project_version():
    try:
        return project.get_version()
    except AttributeError:
        raise ImproperlyConfigured(
            'Your project must define a ``get_version``' +
            'function that returns a valid PEP440 version string.'
        )

def get_exclude_packages():
    return _get_attribute('EXCLUDE_PACKAGES')

def get_project_name():
    return _get_attribute('NAME')

def get_project_license():
    return _get_attribute('LICENSE')

def get_project_desc():
    return _get_attribute('DESCRIPTION')

def get_author_name():
    return _get_attribute('AUTHOR_NAME')

def get_author_email():
    return _get_attribute('AUTHOR_EMAIL')

def get_project_url():
    return _get_attribute('URL')

def get_project_download_url():
    return _get_attribute('DOWNLOAD_URL')

def get_test_requirements():
    return _get_attribute('TEST_REQUIREMENTS')

def get_test_suite():
    return _get_attribute('TEST_SUITE')

def get_classifiers():
    classifiers = []
    version = get_project_version().lower()

    if ('a' in version):
        # alpha
        classifiers += ['Development Status :: 3 - Alpha']
    elif ('b' in version):
        # beta
        classifiers += ['Development Status :: 4 - Beta']
    else:
        # final/release candidate/stable
        classifiers += ['Development Status :: 5 - Production/Stable']

    return classifiers + _get_attribute('CLASSIFIERS')
