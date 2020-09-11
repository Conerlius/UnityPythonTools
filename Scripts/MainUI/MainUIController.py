import os
import UIFactory
import Scripts.GlobalVar as Global

class Create(UIFactory.MainUI):
    def __init__(self, parent):
        super(Create, self).__init__(parent)
        self.RefleshList()

    def RefleshList(self):
        self.files = os.listdir('./modules')
        for file in self.files:
            self.m_listBox1.Append(file.replace('.exe', ''))

    def OnOpenTools(self, event):
        index = self.m_listBox1.GetSelection()
        tool_name = self.files[index]
        isDebug = Global.get_value("isDebug")
        if not isDebug:
            result = os.system('start ./modules/{}'.format(tool_name))
            print(result)
        else:
            result = os.system('py ./modules/{}/{}.py'.format(tool_name, tool_name))
            print(result)