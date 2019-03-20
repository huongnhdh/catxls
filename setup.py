#!/usr/bin/env python
#!-*-coding:utf8-*-
"""File setup.py"""
from setuptools import setup, find_packages
setup(
    name='catxls',
    version='0.0.1',
    packages=find_packages(
        '*.py',
        exclude=[
            '*.tests', '*.tests.*', 'tests.*', 'tests'
        ]
    ),
    license='MIT',
    description='read xls, xlsx on server',
    author='huongnhd',
    author_email = 'huong.nhdh@gmail.com',
    url = 'https://github.com/huongnhdh/catxls.git',
    download_url = 'https://github.com/huongnhdh/catxls/archive/v_001.tar.gz',
    keywords = ['xls', 'xlsx', 'cat xlsx', 'server'],
    install_requires=[
      'pyexcel==0.5.13',
      'pyexcel-xls==0.5.8'
    ],
    classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build System :: System Shells',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
    entry_points="""
    [console_scripts]
    catxls=app.scripts.catxlsx:_main
    """
)
