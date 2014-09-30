#/usr/bin/env python
import os
from setuptools import setup, find_packages

ROOT_DIR = os.path.dirname(__file__)
SOURCE_DIR = os.path.join(ROOT_DIR)

# Dynamically calculate the version based on photologue.VERSION
version_tuple = __import__('photologue').VERSION
if len(version_tuple) == 3:
    version = "%d.%d.%s" % version_tuple
else:
    version = "%d.%d" % version_tuple[:2]

setup(
    name = "django-photologue-praekelt",
    version = version,
    description = "Powerful image management for the Django web framework. Praekelt fork.",
    author = "Justin Driscoll",
    author_email = "hedley@praekelt.com",
    url = "https://github.com/praekelt/django-photologue/",
    packages = find_packages(),
    package_data = {
        'photologue': [
            'res/*.jpg',
            'locale/*/LC_MESSAGES/*',
            'templates/photologue/*.html',
            'templates/photologue/tags/*.html',
        ]
    },
    zip_safe = False,
    test_suite="setuptest.setuptest.SetupTestSuite",
    tests_require=[
        'django-setuptest>=0.1.4',
    ],
    classifiers = ['Development Status :: 5 - Production/Stable',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Utilities'],
)
