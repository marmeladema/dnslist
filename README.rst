========
dnslist
========

.. image:: https://travis-ci.com/marmeladema/dnslist.svg?branch=master
    :target: https://travis-ci.com/marmeladema/dnslist

---------------

:Author: `Elie ROUDNINSKI <mailto:xademax@gmail.com>`_

**dnslist** is a Python package that allows to easily load domain list from
various sources and merge them together. It is mainly used for merging
ads/malware domain list together.

.. contents::
    :backlinks: none

.. sectnum::

Installation
============

Requirements
------------

**dnslist** requires Python 3. It has been tested on Python 3.6 on Linux.
For dependencies, see requirements.txt file.

From github
-----------

You can clone this repository and install it with setuptools directly::

    $ python3 setup.py install --user

From pip
--------

As every pip available package, you can install it easily with the pip package::

    $ python3 -m pip install --user dnslist

Usage
=====

**dnslist** comes with both a Python module and an executable tool.
You will more lilely want to use the executable directly.

Configuration
-------------

First, you will need to create a configuration file with toml syntax::

    [source.yoyo]
    url = "https://pgl.yoyo.org/adservers/serverlist.php?hostformat=nohtml&showintro=0"

This file should most likely resides in ~/.config/dnslst/config.toml

Generation
----------

Then you can just execute the dnslist executable tool::

    $ dnslist domains.txt

This should generate a domain.txt file in the current working directory.

Template
--------

You can customize how the generated file looks like by providing a moustache
template::

    $ dnslist -t <path/to/template.moustache> domains.txt

If you need help with moustache syntax, you can check out the:

- Officiel moustache website: https://mustache.github.io/
- Underlying rendering module: https://github.com/noahmorrison/chevron

Examples
--------

Take a look at the |examples/|_ directory for some classic configurations
or templates.

.. |examples/| replace:: ``examples/``
.. _examples/: examples/
