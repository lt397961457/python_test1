import getpass
# -*- coding: utf-8 -*-
name=input("请输入用户名：")
pwd=getpass.getpass("请输入密码：")
if name =="alex" and pwd =="cmd":
    print("成功")
else:
    print("失败")