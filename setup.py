#!/usr/bin/env python3

import os
from setuptools import setup


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
	return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name = 'dnslist',
    version = '0.2',
    description = 'Domain list generator',
    long_description = read('README.rst'),
    author = 'Elie ROUDNINSKI',
    author_email = 'xademax@gmail.com',
    url = 'https://github.com/marmeladema/dnslist/',
    download_url = 'https://github.com/marmeladema/dnslist/archive/0.2.tar.gz',
    packages = ['dnslist'],
    python_requires = '>=3',
    test_suite = 'tests',
    entry_points = {
        'console_scripts': [
            'dnslist=dnslist.__main__:main',
        ],
    }
)
