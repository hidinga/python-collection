#!/usr/bin/python3

from dbClass import MyDBClass

# 读取数据列表

db = MyDBClass() 

for ticker in db.getTickers():
    print(ticker)
  