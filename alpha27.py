#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
 * @Author: Augustus.Wang 
 * @Date: 2017-07-12 22:28:25 
 * @Last Modified by: Augustus.Wang
 * @Last Modified time: 2017-07-12 23:09:57
'''

import xlrd
import xlwt
from datetime import date,datetime

def openworkbook(_filename=0):
  '''
  开启一个workbook,输入参数为文件地址，若无输入则进入交互式输入界面
    * @Last Modified by: Augustus.Wang
    * @Last Modified time: 2017-07-14 
  '''
  if _filename==0:
    _filename=raw_input("file to read:")
  print (_filename)
  try:
      workbook = xlrd.open_workbook(_filename)
  except BaseException:
      print("something went wrong while trying to open a workbook")
  else:
        print("opening:")
        print(_filename)
        print("get sheet:")
        print (workbook.sheet_names())
        return workbook

def opensheet(workbook,numofsheet=0):
    '''
    开启一个sheet，注意sheet索引从0开始,默认为0
    '''
    try:
        _sheetget=workbook.sheet_by_index(numofsheet)
    except BaseException:
        print("something went wrong while trying to open a sheet")
    else:
        print("opening sheet number:")
        print(numofsheet)
        return _sheetget

def sheettoarray(sheet):
    array=[]
    for currow in range(sheet.nrows):
        array.append(sheet.row_values(currow))
    #print array
    return array

# #driver
# if __name__ == '__main__':
#     table1=sheettoarray(opensheet(openworkbook()))
#     print table1[0][1]
# #You can show a cell's contebt in this way. 

def arrayfindcol(array,keyword,search_in_which_row=0,search_mul_cols=0):
    """
    按关键字查找对应列，返回对应列的编号
    参数为：数组名，关键字，metadata所在的行(默认为0)，如何处理多个相同的结果(默认0报错,1为返回首个,2为返回一个list)
    """
    keyword=unicode(keyword,'utf-8')
    print ("looking for keyword:", keyword)
    if search_in_which_row>(len(array)-1):
        raise ValueError('this row does not exist in array')
    _rowtosearch=array[search_in_which_row]
    wordcount=0
    wordlist=[]
    for i in range(len(_rowtosearch)):
        print (_rowtosearch[i])
        if _rowtosearch[i]==keyword:
            wordlist.append(i)
            wordcount=wordcount+1
    if wordcount==0:
        print("found nothing but air")
        return -1
    if search_mul_cols==0:
        if wordcount==1:
            return wordlist[0]
        else:
            raise ValueError("the same elements occured mul times")
    if search_mul_cols==1:
        return wordlist[0]
    if search_mul_cols==2:
        return wordlist
    raise ValueError("search_mul_cols could only be 0,1,2")

def addcol(array,colname='',function=(lambda x:'')):
    '''
    在数组里引入新的列，默认列名为空，使用函数function来确定新列的值
    addcol将一行的所有数据换成dict传递给function
    function应返回一个值
    '''
    array[0].append(colname)
    if len(array)-1>0:
        for i in range(len(array)).pop(0):
            dictget={}
            for p in range(len(array[0])):
                dictget[array[0][p]]=array[i][p]
            array(i).append(function(dictget))

#driver
if __name__ == '__main__':
    table1=sheettoarray(opensheet(openworkbook()))
    print (table1[0][1])
    print (arrayfindcol(table1,'批次'))