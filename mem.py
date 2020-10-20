# 该文件提供信号写入函数，将处理完成的信号写入到指定的文件中
# 参数： signal: 要存储的信号, 
#       signalName: 信号名(PLETH, SBP, DBP)
#       path: 指定存储的路径
''' 写入数据的基本格式
[
  {
    PLETH: number[],
    SBP: number[],
    DBP: number[]
  },
  ...
]
 
'''