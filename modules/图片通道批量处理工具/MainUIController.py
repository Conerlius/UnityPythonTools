#!/usr/bin/python
# -*- coding: UTF-8 -*-

import modules.图片通道批量处理工具.UIFactory as UIFactory

from PIL import Image
import os

class Create(UIFactory.MainUI):
    def __init__(self, parent):
        super(Create, self).__init__(parent)

    def OnStart(self, event):
        # 文件夹
        maindir, subdirs, files = os.walk('temp')

        # 文件
        file_path = ''
        image_file = Image.open(file_path)
        image_file.