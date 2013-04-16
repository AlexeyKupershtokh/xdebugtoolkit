#!/usr/bin/env python
from setuptools import setup
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='xdebugtoolkit',
    version='0.2.2-1',
    author='Alexey Kupershtokh',
    author_email='alexey.kupershtokh@gmail.com',
    url='https://github.com/AlexeyKupershtokh/xdebugtoolkit',
    description="A toolkit for splitting, aggregating, analyzing and visualizing xdebug cachegrind files",
    long_description=read("README.rst"),
    license="LGPL",

    scripts=['bin/cg2dot', 'bin/cgsplit', 'bin/xdot-pygoocanvas'],
    py_modules=['cgparser', 'dot', 'stylers.default', 'reader']
)