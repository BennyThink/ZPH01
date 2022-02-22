#!/usr/bin/env python
# Learn more: https://github.com/kennethreitz/setup.py

# Note: To use the 'upload' functionality of this file, you must:
#   $ pip install twine
# python setup.py sdist upload -r pypi

import io
import os

from distutils.core import setup

# Where the magic happens:
setup(
    name="zph01",
    version="0.0.2",
    description="DESCRIPTION",
    long_description="long_description",
    author='BennyThink',
    author_email='benny@bennythink.com',
    python_requires='>=3.6.0',
    url='https://github.com/BennyThink/ZPH01',
    packages=['zph01'],
    install_requires=["pyserial"],
    license='MIT',

    # data_files=['README.rst']
)
