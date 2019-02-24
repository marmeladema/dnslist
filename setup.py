#!/usr/bin/env python3

from setuptools import setup

setup(
    name = 'dnslist',
    version = '0.1',
    description = 'Domain list generator',
    author = 'Elie ROUDNINSKI',
    author_email = 'xademax@gmail.com',
    url = 'https://github.com/marmeladema/dnslist/',
    packages = ['dnslist'],
    python_requires = '>=3',
    test_suite = 'tests',
    entry_points = {
        'console_scripts': [
            'dnslist=dnslist.__main__:main',
        ],
    }
)
