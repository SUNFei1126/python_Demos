# coding=utf-8

#!/usr/bin/python3

'''
 Created by sunyufei on 2018/12/21.
'''
'''
 将 第 0015 题中的 city.xls 文件中的内容写到 city.xml 文件中，如下 所示：

    <?xmlversion="1.0" encoding="UTF-8"?>
    <root>
    <cities>
    <!-- 
    	城市信息
    -->
    {
    	"1" : "上海",
    	"2" : "北京",
    	"3" : "成都"
    }
    </cities>
    </root>
'''

import json
import xlrd
from lxml import etree

testfile = 'city.xls'
savename = 'city.xml'
sheetname = 'city'


def to_xml(data):
    root = etree.Element('root')
    stu = etree.SubElement(root, 'cities')
    comm = etree.Comment(u'城市信息')
    stu.append(comm)

    stu.text = data
    tree = etree.ElementTree(root)
    tree.write(savename, encoding='utf-8', pretty_print=True, \
               xml_declaration=True)


def read_excel(testfile):
    book = xlrd.open_workbook(testfile)
    sheet = book.sheet_by_name(sheetname)
    data = {}
    rows = sheet.nrows
    cols = sheet.ncols
    for i in range(rows):
        data[str(int(sheet.cell_value(i, 0)))] = sheet.cell_value(i, 1)
    # The ensure_ascii param is very important for Chinese character, see the
    # document
    return json.dumps(data, ensure_ascii=False)


if __name__ == '__main__':
    data = read_excel(testfile)
    to_xml(data)