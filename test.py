#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/10/18 21:31
# @funcation:
# @Author   : mx
# @File     : test.py
# @Software : PyCharm
guest=['liuyang','kaiyue','xiaotu']
print('Hi,'+guest[0]+',do u want have dinner with me?')
print('Hi,'+guest[1]+',do u want have dinner with me?')
print('Hi,'+guest[2]+',do u want have dinner with me?')
poped_guest=guest.pop(0)
print("poped_guest can't have dinner with me.")
guest.insert(0,'mengxin')
print("let us eat together,"+guest[0]+guest[1]+guest[2])
print("i've get a bigger table")
guest.insert(0,'erteng')
guest.insert(1,'xiaobai')
guest.append('xiaojiang')
print(guest)
print('Hi,'+guest[0]+',do u want have dinner with me?')
print('Hi,'+guest[1]+',do u want have dinner with me?')
print('Hi,'+guest[1]+',do u want have dinner with me?')
print('Hi,'+guest[2]+',do u want have dinner with me?')
print('Hi,'+guest[3]+',do u want have dinner with me?')
print('Hi,'+guest[4]+',do u want have dinner with me?')
print('Hi,'+guest[5]+',do u want have dinner with me?')
print('sorry,my new table can not reach in time.')
guest.pop()
guest.pop()
guest.pop()
guest.pop()
print('Hi,'+guest[0]+',u are still in the list')
print('Hi,'+guest[1]+',u are still in the list')
del guest[0]
del guest[0]
print(guest)

