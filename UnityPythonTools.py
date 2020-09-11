import sys
import wx
import Scripts.MainUI.MainUIController as MainUIController
import Scripts.GlobalVar as Global

isDebug = False

def Start():
    """
    启动函数
    :return:
    """
    app = wx.App()
    ui = MainUIController.Create(None)
    ui.Show()
    app.SetExitOnFrameDelete(True)
    app.MainLoop()
    wx.Exit()

if __name__ == "__main__":
    Global._init()
    arg_len = len(sys.argv)
    if arg_len > 1:
        isDebug = True

    Global.set_value("isDebug", isDebug)
    Start()