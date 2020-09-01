#!Users\shuai\AppData\Local\Programs python
# -*- coding:utf-8 -*-
# @Time : 2020/8/11 17:31
# @Author : shuai
# @File : dir_config.py
# @Software: PyCharm


import os


# 定义项目框架顶层目录

# 定义基本文件路径 
base_dir = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]

# 定义测试参数文件路径 
testdatas_dir = os.path.join(base_dir,"Testdatas")

# 定义测试案例文件路径
testcases_dir = os.path.join(base_dir,"Testcase")

#定义测试报告输入文件 html报告，log
htmlreport_dir = os.path.join(base_dir,"Outputs/htmlreport")

logs_dir = os.path.join(base_dir,"Outptus/logs")

screenshot_dir = os.path.join(base_dir,"Outptus/screenshot")

# 定义APP属性值文件
caps_dir = os.path.join(base_dir,"Caps")


