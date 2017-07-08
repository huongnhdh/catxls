#!/usr/bin/env python
#!-*-coding:utf8-*-
"""File setup.py"""
from setuptools import setup, find_packages
setup(
    name='mrconvertor',
    version='0.0.0',
    packages=find_packages(
        '.',
        exclude=[
            '*.tests', '*.tests.*', 'tests.*', 'tests'
        ]
    ),
    install_requires=[
    ],
    entry_points="""
    [console_scripts]
    md_xlsx=app.scripts.md_xlsx._main    
    """
)