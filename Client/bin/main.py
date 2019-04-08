#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-3-2 13:43
# @Author  : zhdya@zhdya.cn
# @File    : main.py

import os
import sys

BASE_DIR = os.path.dirname(os.getcwd())     #设置工作目录，使得包和模块能够正常导入
# print("SSS-->", BASE_DIR)
sys.path.append(BASE_DIR)

from core import handler

if __name__ == '__main__':
    handler.ArgvHandler(sys.argv)       ##获取参数，传入到ArgvHandler()