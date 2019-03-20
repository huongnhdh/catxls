#!/usr/bin/env python3
#! -*- coding:utf8 -*-
"""The script change a file md table to excel
"""
import sys
import logging
from app.helpers.reading_params import get_argument
import pyexcel as pe

def check_validate(file_input, file_output):
  """check the file in put as md and file excel is not exit"""
  pass

def _main(argv=get_argument()):
  """Main executer"""
  print(argv.file_input.name)
  sheet = pe.get_book(file_name=argv.file_input.name)
  print(sheet)

if __name__ == '__main__':
    _main()