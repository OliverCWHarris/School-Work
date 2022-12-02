from stat import filemode
import wx

class MainFrame(wx.Frame):

    def __init__(self, *args, **kw):
        super(MainFrame, self).__init__(*args, **kw)

        pnl=wx.Panel(self)

        st = wx.StaticText(pnl, label="idk what this does")
        font = st.GetFont()
        font.PointSize += 10
        font = font.Bold()
        st.SetFont(font)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(st, wx.SizerFlags().Border(wx.TOP|wx.LEFT, 25))
        pnl.SetSizer(sizer)

        self.makeMenuBar()

        self.CreateStatusBar()
        self.SetStatusText('this is a thing')

    def makeMenuBar(self):
        
        fileMenu=wx.Menu()
        mainItem=fileMenu.Append(-1,'this does a thing... \tCtrl-W',
                'seriously it does something')
        
        fileMenu.AppendSeparator()
        exitItem=fileMenu.Append(wx.ID_EXIT)

        helpMenu=wx.Menu()
        aboutItem=helpMenu.Append(wx.ID_ABOUT)

        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File")
        menuBar.Append(helpMenu, "&Help")

        self.SetMenuBar(menuBar)

        self.Bind(wx.EVT_MENU, self.OnMain, mainItem)
        self.Bind(wx.EVT_MENU, self.OnExit,  exitItem)
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)

    def OnMain(self,event):
        wx.MessageBox("i swear bro this does a thing")

    def OnExit(self,event):
        self.Close(True)
    
    def OnAbout(self,event):
        wx.MessageBox('i mean.... its a box isnt it?')




if __name__ == '__main__':
    app = wx.App()
    frm = MainFrame(None, title='This is the main frame')
    frm.Show()
    app.MainLoop()