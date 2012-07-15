#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='deploy_tools',
    version='0.0.1',
    description='A fabric based deployment toolset',
    author='Dimagi',
    author_email='information@dimagi.com',
    url='http://www.dimagi.com/',
    packages = find_packages(exclude=['*.pyc']),
    include_package_data = True,
    install_requires = [
        "fabric", "pip",
    ],
)

