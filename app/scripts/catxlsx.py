#!/usr/bin/env python3
#! -*- coding:utf8 -*-
"""The script change a file md table to excel
"""
import os  
import sys
import chardet
import pyexcel as pe
from xlrd.biffh import XLRDError
from app.helpers.reading_params import get_argument

def check_path_is_file(file_input):
  """check the file in put as md and file excel is not exit"""
  if os.path.isfile(file_input.name ):  
    return True
  else:  
    print("Not a file!")
    return False

def _main(argv=get_argument()):
  """Main executer"""
  try:
    sheet = pe.get_book(file_name=argv.file_input.name)
    print(sheet)
  except pe.exceptions.FileTypeNotSupported:
    print("FileTypeNotSupported!")
  except XLRDError as e:
    print(e)
  except UnicodeDecodeError:
    # import pdb; pdb.set_trace()
    encoding = chardet.detect(open(argv.file_input.name, 'rb').read()).get('encoding')
    sheet = pe.get_book(file_name=argv.file_input.name, encoding=encoding)
    print(sheet)
  except IOError as e:
    print(e.message)
    
if __name__ == '__main__':
    _main()