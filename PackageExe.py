#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os

def Package():
    """
    打包
    :return:null
    """
    # 主工程
    order = "pyinstaller -F UnityPythonTools.py -w --distpath ./bin"
    result = os.system(order)
    print(u"UnityPythonTools打包结果码:", result)

    # 遍历旗下的所有的子工程
    all_sub_dirs = os.listdir('./modules')
    print(all_sub_dirs)
    for fileName in all_sub_dirs:
        order = "pyinstaller -F ./modules/{}/{}.py -w --distpath ./bin/modules".format(fileName, fileName)
        result = os.system(order)

    print("完成")

if __name__ == "__main__":
    Package()