# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class DGXRSFrame
###########################################################################

class DGXRSFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"DGX Remote Shell", pos = wx.DefaultPosition, size = wx.Size( 822,560 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer5 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel1, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )
		
		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText3 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"DGX IP", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		bSizer9.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.dgx_ip_txt = wx.TextCtrl( self.m_panel1, wx.ID_ANY, u"192.168.7.40", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.dgx_ip_txt, 0, wx.ALL, 5 )
		
		
		sbSizer5.Add( bSizer9, 1, wx.EXPAND, 5 )
		
		
		bSizer5.Add( sbSizer5, 1, wx.EXPAND|wx.ALL, 5 )
		
		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel1, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )
		
		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )
		
		type_cmbChoices = [ u"DGX Shell>", u"BCS>" ]
		self.type_cmb = wx.ComboBox( self.m_panel1, wx.ID_ANY, u"BCS>", wx.DefaultPosition, wx.DefaultSize, type_cmbChoices, 0 )
		self.type_cmb.SetSelection( 0 )
		bSizer8.Add( self.type_cmb, 0, wx.ALL, 5 )
		
		self.m_staticText2 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"DGX_Shell>", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		self.m_staticText2.Hide()
		
		bSizer8.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.dgx_command_txt = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		bSizer8.Add( self.dgx_command_txt, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_button2 = wx.Button( self.m_panel1, wx.ID_ANY, u"Submit", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.m_button2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer6.Add( bSizer8, 1, wx.EXPAND, 5 )
		
		
		sbSizer3.Add( bSizer6, 1, wx.EXPAND, 5 )
		
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button3 = wx.Button( self.m_panel1, wx.ID_ANY, u"Show", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_button3, 0, wx.ALL, 5 )
		
		self.m_button4 = wx.Button( self.m_panel1, wx.ID_ANY, u"Channel", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_button4, 0, wx.ALL, 5 )
		
		self.m_button5 = wx.Button( self.m_panel1, wx.ID_ANY, u"Show Stats", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_button5, 0, wx.ALL, 5 )
		
		self.m_button6 = wx.Button( self.m_panel1, wx.ID_ANY, u"Power", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_button6, 0, wx.ALL, 5 )
		
		self.m_button7 = wx.Button( self.m_panel1, wx.ID_ANY, u"Show AIE", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_button7, 0, wx.ALL, 5 )
		
		self.m_button8 = wx.Button( self.m_panel1, wx.ID_ANY, u"Switch", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_button8, 0, wx.ALL, 5 )
		
		
		bSizer7.Add( bSizer10, 1, wx.EXPAND, 5 )
		
		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button11 = wx.Button( self.m_panel1, wx.ID_ANY, u"~scr1v3!", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.m_button11, 0, wx.ALL, 5 )
		
		self.m_button12 = wx.Button( self.m_panel1, wx.ID_ANY, u"~scr4v3!", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.m_button12, 0, wx.ALL, 5 )
		
		self.m_button13 = wx.Button( self.m_panel1, wx.ID_ANY, u"~scr5v3!", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.m_button13, 0, wx.ALL, 5 )
		
		self.m_button14 = wx.Button( self.m_panel1, wx.ID_ANY, u"~scr6v3!", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.m_button14, 0, wx.ALL, 5 )
		
		self.m_button15 = wx.Button( self.m_panel1, wx.ID_ANY, u"~scr7v3!", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.m_button15, 0, wx.ALL, 5 )
		
		self.m_button16 = wx.Button( self.m_panel1, wx.ID_ANY, u"~scr9v3!", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.m_button16, 0, wx.ALL, 5 )
		
		
		bSizer7.Add( bSizer11, 1, wx.EXPAND, 5 )
		
		
		sbSizer3.Add( bSizer7, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer5.Add( sbSizer3, 0, wx.EXPAND|wx.ALL, 5 )
		
		
		bSizer2.Add( bSizer5, 0, wx.EXPAND, 5 )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.display_txt = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		self.display_txt.SetFont( wx.Font( 9, 75, 90, 90, False, "Courier New" ) )
		
		bSizer3.Add( self.display_txt, 1, wx.EXPAND, 5 )
		
		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button10 = wx.Button( self.m_panel1, wx.ID_ANY, u"Process", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_button10, 0, wx.ALL, 5 )
		
		self.m_button9 = wx.Button( self.m_panel1, wx.ID_ANY, u"Clear", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_button9, 0, wx.ALL, 5 )
		
		
		bSizer3.Add( bSizer10, 0, wx.ALIGN_RIGHT, 5 )
		
		
		bSizer2.Add( bSizer3, 1, wx.EXPAND, 5 )
		
		
		self.m_panel1.SetSizer( bSizer2 )
		self.m_panel1.Layout()
		bSizer2.Fit( self.m_panel1 )
		bSizer1.Add( self.m_panel1, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_RIGHT_DCLICK, self.on_clear )
		self.dgx_command_txt.Bind( wx.EVT_TEXT_ENTER, self.on_submit )
		self.m_button2.Bind( wx.EVT_BUTTON, self.on_submit )
		self.m_button3.Bind( wx.EVT_BUTTON, self.on_command_button )
		self.m_button4.Bind( wx.EVT_BUTTON, self.on_command_button )
		self.m_button5.Bind( wx.EVT_BUTTON, self.on_command_button )
		self.m_button6.Bind( wx.EVT_BUTTON, self.on_command_button )
		self.m_button7.Bind( wx.EVT_BUTTON, self.on_command_button )
		self.m_button8.Bind( wx.EVT_BUTTON, self.on_command_button )
		self.m_button11.Bind( wx.EVT_BUTTON, self.on_bcs_button )
		self.m_button12.Bind( wx.EVT_BUTTON, self.on_bcs_button )
		self.m_button13.Bind( wx.EVT_BUTTON, self.on_bcs_button )
		self.m_button14.Bind( wx.EVT_BUTTON, self.on_bcs_button )
		self.m_button15.Bind( wx.EVT_BUTTON, self.on_bcs_button )
		self.m_button16.Bind( wx.EVT_BUTTON, self.on_bcs_button )
		self.m_button10.Bind( wx.EVT_BUTTON, self.on_apply )
		self.m_button9.Bind( wx.EVT_BUTTON, self.on_clear )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def on_clear( self, event ):
		event.Skip()
	
	def on_submit( self, event ):
		event.Skip()
	
	
	def on_command_button( self, event ):
		event.Skip()
	
	
	
	
	
	
	def on_bcs_button( self, event ):
		event.Skip()
	
	
	
	
	
	
	def on_apply( self, event ):
		event.Skip()
	
	

