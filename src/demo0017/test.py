# coding=utf-8

#!/usr/bin/python3

'''
 Created by sunyufei on 2018/12/21.
 lxml安装py35的3.7.1版本有etree
'''
'''
将 第 0014 题中的 student.xls 文件中的内容写到 student.xml 文件中，如

下所示：
<?xml version="1.0" encoding="UTF-8"?>
<root>
<students>
<!-- 
	学生信息表
	"id" : [名字, 数学, 语文, 英文]
-->
{
	"1" : ["张三", 150, 120, 100],
	"2" : ["李四", 90, 99, 95],
	"3" : ["王五", 60, 66, 68]
}
</students>
</root>
'''

import xlrd
from lxml import etree
import json
import io

fromfile = 'student.xls'

def read_xls(fromfile):
    book = xlrd.open_workbook(fromfile)
    sheet = book.sheet_by_name('student')
    data = {}
    rows = sheet.nrows
    cols = sheet.ncols
    kv = []
    for i in range(rows):
        for j in range(1, cols):
            if type(sheet.cell_value(i, j)) is float:
                kv.append(int(sheet.cell_value(i, j)))
            else:
                kv.append(sheet.cell_value(i, j))
        data[str(int(sheet.cell_value(i, 0)))] = kv
    return json.dumps(data, ensure_ascii = False)

def to_xml(data):
    #Create a document and elements
    root = etree.Element('root')
    stu = etree.SubElement(root,'students')
    #Create a comment
    stu.append(etree.Comment(u' 学生信息表\n\t"id" : [名字, 数学, 语文, 英文]'))

    #Create text
    stu.text = data

    #Save to file
    tree = etree.ElementTree(root)
    tree.write('student.xml',encoding = 'utf-8',pretty_print =True,xml_declaration = True)


if __name__ == '__main__':
    data = read_xls(fromfile)
    to_xml(data)