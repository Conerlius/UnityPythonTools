#!/usr/bin/python
# -*- coding: UTF-8 -*-
import wx
import modules.图片通道批量处理工具.MainUIController as MainUIController

def Start():
    app = wx.App()
    ui = MainUIController.Create(None)
    ui.Show()
    app.SetExitOnFrameDelete(True)
    app.MainLoop()
    wx.Exit()

if __name__ == "__main__":
    Start()