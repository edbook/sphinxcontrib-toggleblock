#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

long_desc = """
This package contains a Sphinx extension to make text blocks toggleable. It defines two directives "begin-toggle" and "end-toggle".
"""

requires = ["Sphinx>=0.6", "setuptools"]


setup(
    name="sphinxcontrib-toggleblock",
    version="2.0",
    description="Sphinx extension",
    author="Solrun Einarsdottir",
    author_email="solrun.einarsdottir@gmail.com",
    maintainer="Benedikt Magnusson",
    maintainer_email="bsm@hi.is",
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    namespace_packages=["sphinxcontrib"],
)
