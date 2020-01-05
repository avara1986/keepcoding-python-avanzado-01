# -*- coding: utf-8 -*-
# Copyright (c) 2017 by Alberto Vara <a.vara.1986@gmail.com>
import codecs
import os

from setuptools import setup, find_packages

if os.path.exists('README.md'):
    long_description = codecs.open('README.md', 'r', 'utf-8').read()
else:
    long_description = ''

# parse_requirements() returns generator of pip.req.InstallRequirement objects
with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name="curso",
    version="0.0.1",
    author="Alberto Vara",
    author_email="a.vara.1986@gmail.com",
    description="Curso ejemplo python",
    long_description=long_description,
    classifiers=[
        'Development Status :: 6 - Mature',
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.6"
        "Programming Language :: Python :: 3.7"
        "Programming Language :: Python :: 3.8"
    ],
    license="MIT",
    platforms=["any"],
    keywords="python, aws, lambda",
    url='',
    packages=find_packages(),
    install_requires=required,
    include_package_data=True,
    zip_safe=True,
)