# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainUI
###########################################################################

class MainUI ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"图片通道批量处理工具", pos = wx.DefaultPosition, size = wx.Size( 960,640 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel1 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"选择拆分的资源的目录", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		bSizer3.Add( self.m_staticText1, 0, wx.ALL, 5 )

		self.m_dirPicker1 = wx.DirPickerCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		bSizer3.Add( self.m_dirPicker1, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText2 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"选择拆分的资源", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		bSizer3.Add( self.m_staticText2, 0, wx.ALL, 5 )

		self.m_filePicker1 = wx.FilePickerCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.tga\n*.png\n*.dds\n*.jpg", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		bSizer3.Add( self.m_filePicker1, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_button1 = wx.Button( self.m_panel1, wx.ID_ANY, u"拆解", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_button1, 0, wx.ALL, 5 )


		self.m_panel1.SetSizer( bSizer3 )
		self.m_panel1.Layout()
		bSizer3.Fit( self.m_panel1 )
		self.m_notebook1.AddPage( self.m_panel1, u"拆分", False )
		self.m_panel2 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_notebook1.AddPage( self.m_panel2, u"合并", False )

		bSizer2.Add( self.m_notebook1, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button1.Bind( wx.EVT_BUTTON, self.OnStart )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def OnStart( self, event ):
		event.Skip()


