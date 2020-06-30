#!D:\python 3.8.2\python.exe
# 从FieldStorage中获取单个值的CGI脚本（simple2.cgi）

import cgi
form = cgi.FieldStorage()
name = form.getvalue('name', 'world')
print('Content-type: text/plain\n')
print('Hello, {}!'.format(name))
