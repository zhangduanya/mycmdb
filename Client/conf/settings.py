#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-3-2 14:21
# @Author  : zhdya@zhdya.cn
# @File    : settings.py

import os

# 远端服务器配置
Params = {
    "server": "192.168.1.3",
    "port": 8000,
    'url': '/assets/report/',
    'request_timeout': 30,
}

# 日志文件配置

PATH = os.path.join(os.path.dirname(os.getcwd()), 'log', 'cmdb.log')
print("conf_settings-->>", PATH)


# 更多配置，请都集中在此文件中