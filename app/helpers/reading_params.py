#!/usr/bin/env python
#! -*- coding:utf-8 -*-
""" Helper get argument of scripts
"""

import argparse
import os

def _check_file_exist(file_arg):
    """ Check file is exits """
    if not os.path.exist(file_arg):
        raise argparse.ArgumentError('File %s doest exist', file_arg)
    return file_arg

__parser__ = argparse.ArgumentParser(description='Convert input file to Output file')

__parser__.add_argument(
    '-i', '--input',
    action='Input file',
    dest='file_input',
    type=_check_file_exist,
    metavar="FILE",
    required=True,
    help="The input FILE"
)
__parser__.add_argument(
    '-o', '--output',
    action='Out file',
    dest='file_output',
    metavar="FILE",
    help="The output FILE "
)


def get_argument():
    """return argument  """
    args = __parser__.parse_args()
    return args
