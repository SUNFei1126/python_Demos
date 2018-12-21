# coding=utf-8

#!/usr/bin/python3

'''
 Created by sunyufei on 2018/12/21.
'''
'''
 将 第 0016 题中的 numbers.xls 文件中的内容写到 numbers.xml 文件中，如下

所示：

<?xml version="1.0" encoding="UTF-8"?>
<root>
<numbers>
<!-- 
	数字信息
-->

[
	[1, 82, 65535],
	[20, 90, 13],
	[26, 809, 1024]
]

</numbers>
</root>
'''

import json
import xlrd
from lxml import etree

testfile = 'numbers.xls'
savename = 'numbers.xml'
sheetname = 'numbers'

def to_xml(data):
    root = etree.Element('root')
    stu = etree.SubElement(root, 'numbers')
    comm = etree.Comment(u'数字信息')
    stu.append(comm)

    stu.text = data
    tree = etree.ElementTree(root)
    tree.write(savename, encoding = 'utf-8', pretty_print = True, \
               xml_declaration = True)

def read_excel(testfile):
    book = xlrd.open_workbook(testfile)
    sheet = book.sheet_by_name(sheetname)
    data = []
    rows = sheet.nrows
    cols = sheet.ncols
    for i in range(rows):
        line = [int(sheet.cell_value(i, j)) for j in range(cols)]
        data.append(line)
    return json.dumps(data)


if __name__ == '__main__':
    data = read_excel(testfile)
    to_xml(data)