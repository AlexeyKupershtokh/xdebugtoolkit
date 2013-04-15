#!/usr/bin/env python
from setuptools import setup

setup(
    name='xdebugtoolkit',
    version='0.2.0',
    author='Alexey Kupershtokh',
    author_email='alexey.kupershtokh@gmail.com',
    url='https://github.com/AlexeyKupershtokh/xdebugtoolkit',
    description="A toolkit for splitting, aggregating, analyzing and visualizing xdebug cachegrind files",
    long_description="""
        A toolkit for splitting, aggregating, analyzing and visualizing xdebug cachegrind files.
        """,
    license="LGPL",

    scripts=['cg2dot.py', 'cgsplit.py'],
    py_modules=['cgparser', 'dot', 'stylers', 'stylers.default', 'reader']
)