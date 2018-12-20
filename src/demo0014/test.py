# coding=utf-8

#!/usr/bin/python3

'''
 Created by sunyufei on 2018/12/20.
'''
"""
第 0014 题： 纯文本文件 student.txt为学生信息, 里面的内容（包括花括号）如下所示：
{
    "1":["张三",150,120,100],
    "2":["李四",90,99,95],
    "3":["王五",60,66,68]
}
请将上述内容写到 student.xls 文件中。
"""
import xlwt
import json

def write_txt_to_xls(txt_file):
    txt_object = open(txt_file,'r')
    file_content = json.load(txt_object)

    xls_object = xlwt.Workbook()
    sheet = xls_object.add_sheet('student')
    for i in range(len(file_content)):
        sheet.write(i,0,i+1)
        data = file_content[str(i+1)]
        for j in range(len(data)):
            sheet.write(i,j+1,data[j])
    xls_object.save('student.xls')


if __name__ =='__main__':
    write_txt_to_xls('student.txt')
