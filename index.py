# 调用各个模块并协调数据，实现最终功能
# 最中处理完成的数据存放在proccessedData目录下
import os
import numpy as np
import filter
import markSignal
import mem
import readRecords
import separateBP

for i in range(10):
  recordsPath = f'../checkedDir/3{i}.txt'
  # 1. 读取checkdDir中的文件并将返回的字符串数组记录在records变量中
  records = readRecords.readRecords(recordsPath)
  recordsLen = len(records)
  if recordsLen != 0:
    # 2. 遍历records数组并调用markSignal函数，并将返回的结果传给filter函数进行滤波处理，处理完成后放入filtedList
    # filtedList是一个字典数组
    filtedList = []
    for recordPath in records:
      marked = markSignal.markSignal(recordPath)
      filtedMarked = filter.filter(marked)
      filtedList.append(filtedMarked)
    # 将checkedDir下的一个文件全部处理完后将filtedList的存储结果写入filtedData下

