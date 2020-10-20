# 本文件用于提供读取本地records的函数，并将读取大到的records记录以字符串列表的形式返回

import os

def readRecords(path):
  with open(path) as f:
    records = f.read().split('\n')
    records.pop()
  return records