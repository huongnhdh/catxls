#!/usr/bin/env python3
#! -*- coding:utf-8 -*-
""" Helper get argument of scripts
"""

import argparse
import os


__parser__ = argparse.ArgumentParser(description='input')
__parser__.add_argument(
    action='store',
    dest='file_input',
    type=open,
    metavar="FILE",
    help="The input FILE xls"
)
# __parser__.add_argument(
#     '-i', '--input',
#     action='store',
#     dest='file_input',
#     type=open,
#     metavar="FILE",
#     help="The input FILE"
# )
# __parser__.add_argument(
#     '-o', '--output',
#     action='store',
#     dest='file_output',
#     metavar="FILE",
#     help="The output FILE "
# )


def get_argument():
    """return argument  """
    args = __parser__.parse_args()
    return args
