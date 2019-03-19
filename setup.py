#!/usr/bin/env python
#!-*-coding:utf8-*-
"""File setup.py"""
from setuptools import setup, find_packages
setup(
    name='bean',
    version='0.0.0',
    packages=find_packages(
        '*.py',
        exclude=[
            '*.tests', '*.tests.*', 'tests.*', 'tests'
        ]
    ),
    install_requires=[
      'pyexcel==0.5.13',
      'pyexcel-xls==0.5.8'
    ],
    entry_points="""
    [console_scripts]
    catxlsx=app.scripts.catxlsx:_main
    """
)
