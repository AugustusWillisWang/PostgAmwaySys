#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
 * @Author: Augustus.Wang 
 * @Date: 2017-07-12 22:28:25 
 * @Last Modified by: Augustus.Wang
 * @Last Modified time: 2017-08-01 00:09:57
'''

import xlrd
import xlwt
import os
import csv
import urllib
from datetime import date,datetime

segcount=0

def man():
    '''
    显示可用的函数
    '''
    print("\
    openworkbook(_filename=0):\
    opensheet(workbook,numofsheet=0):\
    sheettoarray(sheet):\
    arrayfindcol(array,keyword,search_in_which_row=0,search_mul_cols=0):\
    addcol(array,colname='',function=(lambda x:'')):\
    delcol(array,colnumber):\
    showrow(array,rownumber):\
    writecsv(filename,array):\
    readcsv(filename):\
    pickattr(array,attrlist):\
    seg(input):\
    combine(array1,key1,array2,key2):\
    ")    

def openworkbook(_filename=0):
  '''
  开启一个workbook,输入参数为文件地址，若无输入则进入交互式输入界面 
  '''
  if _filename==0:
    _filename=str(input("file to read:"))
    print(_filename)
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
    """
    将读取的sheet转化为数组
    """
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
        _temparray=list(range(len(array)))
        _temparray.pop(0)
        for i in _temparray:
            dictget={}
            for p in range(len(array[0])-1):
                dictget[array[0][p]]=array[i][p]
            array[i].append(function(dictget))

def egfunc(kw):
    return kw['批次']

def delcol(array,colnumber):
    '''
    删除列
    '''
    for i in range(len(array)):
        array[i].pop(colnumber)

def showrow(array,rownumber):
    """
    按主键与值之间的对应显示某一行
    """
    if rownumber<=len(array) and rownumber>=0:
        key=0
        for i in array[0]:
            print(array[0][key],":",array[rownumber][key])
            key=key+1
    else:
        raise ValueError("row does not exist")

def writecsv(filename,array):
    """
    写csv文件作为输出，采用a+模式
    """
    with open(filename, 'a+') as f:
        reader = csv.reader(f, delimiter=',')
        writer = csv.writer(f,delimiter=',')
        for i in range(array):
            writer.writerows(array[i])

def readcsv(filename):
    """
    读csv文件，采用r模式
    """
    array=[]
    with open(filename, 'a+') as f:
        reader = csv.reader(f, delimiter=',')
        writer = csv.writer(f,delimiter=',')
        for row in reader:
            array.append(row)
    return array          

def pickattr(array,attrlist):
    '''
    保留数组中list内的属性,删除其他无关元素
    新的数组按attrlist中的顺序排序
    '''
    key=0
    dellist=[]
    for name in array[0]:
        if (name in attrlist):
            pass
        else:
            dellist.append(key)
        key+1
    dellist=dellist[::-1]
    for i in dellist:
        delcol(array,i)
    return array

def seg(input):
    '''
    调用哈工大社会计算与信息检索研究中心研发的 “语言技术平台（LTP）进行中文分词处理
    返回分词后list
    注意查询上限为200次/s
    '''
    url_get_base = "http://api.ltp-cloud.com/analysis/"
    args = { 
        'api_key' : '51W3L3u3Q7sOZA3xuzLcufMLzCGg9XbAumrWKtjV',
        'text' : input,
        'pattern' : 'ws', #模式:分词
        #todo: try 实体检测 mode
        #文档参见 http://www.ltp-cloud.com/document/
        'format' : 'plain'
    }
    result = urllib.urlopen(url_get_base, urllib.urlencode(args)) # POST method
    content = result.read().strip()
    content = content.spilt(' ')
    if (debug):
        print(content)
    time.sleep(0.005)
    return content

def combine(array1,key1,array2,key2):
    """
    使用低性能的方式合并两表,复杂度为n2
    key为合并所凭借的字符串
    合并结果为inner product
    函数返回合并结果
    """
    pos1=0
    pos2=0
    while(array1[0][pos1]!=key1):
        pos1=pos1+1
        if(pos1>len(array1[0])):
            raise ValueError("keyword1 does not exist")
    while(array2[0][pos2]!=key2):
        key2=key2+1
        if(pos2>len(array2[0])):
            raise ValueError("keyword2 does not exist")
    newarray=[]
    newarray.append(array1.pop(0))
    newarray[0].extend(array2.pop(0))
    len1=len(array1)
    len2=len(array2)
    for a in range(len1):
        for b in range(len2):
            if (array1[a][key1]==array2[b][key2]):
                newarray.append(array1[a]+array2[b])
    return newarray
#todo: use bin-search to refactor
#todo: use panda to refactor
    

#test-driver
if (__name__ == '__main__'):
    table1=sheettoarray(opensheet(openworkbook()))
    # os.system("pause")
    print (table1[0][1])
    print (arrayfindcol(table1,'批次'))
    addcol(table1,'new',egfunc)
    print (arrayfindcol(table1,'new'))

    writecsv("output.csv",table1)
    table2=read("output.csv")
    attrlist=["批次","姓名"]

# #driver
# if __name__ == '__main__':
#     man()