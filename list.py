#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/10/18 21:09
# @funcation:
# @Author   : mx
# @File     : list.py
# @Software : PyCharm
#-------------------------------appdend()
motorcycles=[]
motorcycles.append('hongda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)
print(motorcycles[0])
print(motorcycles[1].title())
print(motorcycles[-1])
#------------------------------insert()
motorcycles.insert(0,'ducati')
print(motorcycles)
motorcycles.insert(-1,'ducati')#use append() to insert to the last
print(motorcycles)
motorcycles=['hongda','yamaha','suzuko']
#=============================del()
del motorcycles[-1]
print(motorcycles)
#--------------------------pop()
motorcycles=['hongda','yamaha','suzuko']
poped_motorcycles=motorcycles.pop()#pop(0),pop(-1)
print(motorcycles)
print(poped_motorcycles)
#---------------------------remove()
motorcycles=['hongda','yamaha','suzuko']
motorcycles.remove('suzuko')
print(motorcycles)
