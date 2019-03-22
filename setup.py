#!/usr/bin/env python3
#!-*-coding:utf8-*-
"""File setup.py"""
from setuptools import setup, find_packages
setup(
    name='catxls',
    version='0.0.5',
    packages=find_packages(
        '.',
        exclude=[
            '*.tests', '*.tests.*', 'tests.*', 'tests'
        ]
    ),
    license='MIT',
    description='read xls, xlsx on server',
    author='huongnhd',
    author_email = 'huong.nhdh@gmail.com',
    url = 'https://github.com/huongnhdh/catxls.git',
    download_url = 'https://github.com/huongnhdh/catxls/archive/v_005.tar.gz',
    keywords = ['xls', 'xlsx', 'cat xlsx', 'server'],
    install_requires=[
      'pyexcel==0.5.13',
      'pyexcel-xls==0.5.8',
      'chardet==3.0.4'
    ],
    classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: System Administrators',
    'Topic :: System :: System Shells',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
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
