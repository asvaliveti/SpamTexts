import os
from time import sleep
import wx

class MainPage(wx.Frame):
    def __init__(self, parent, title):
        super(MainPage, self).__init__(parent, title=title, size=(500, 400))

        panel = wx.Panel(self) 
        vbox = wx.BoxSizer(wx.VERTICAL) 
            
        hbox1 = wx.BoxSizer(wx.HORIZONTAL) 
        l1 = wx.StaticText(panel, -1, "Phone number (ex: +12345678900) ") 
            
        hbox1.Add(l1, 1, wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5) 
        self.t1 = wx.TextCtrl(panel) 
            
        hbox1.Add(self.t1,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5) 
        # self.t1.Bind(wx.EVT_TEXT,self.OnKeyTyped) 
        vbox.Add(hbox1) 
            
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        l2 = wx.StaticText(panel, -1, "How many times should I spam them? ") 
            
        hbox2.Add(l2, 1, wx.ALIGN_LEFT|wx.ALL,5) 
        self.t2 = wx.TextCtrl(panel,style = wx.TE_PASSWORD) 
        self.t2.SetMaxLength(5) 
            
        hbox2.Add(self.t2,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5) 
        vbox.Add(hbox2) 
        # self.t2.Bind(wx.EVT_TEXT_MAXLEN,self.OnMaxLen)
            
        hbox3 = wx.BoxSizer(wx.HORIZONTAL) 
        l3 = wx.StaticText(panel, -1, "Text to spam with") 
            
        hbox3.Add(l3,1, wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5) 
        self.t3 = wx.TextCtrl(panel,size = (200,100),style = wx.TE_MULTILINE) 
            
        hbox3.Add(self.t3,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5) 
        vbox.Add(hbox3) 
        # self.t3.Bind(wx.EVT_TEXT_ENTER, self.OnEnterPressed) 

        submit = wx.Button(panel, -1, "Send!")
        vbox.Add(submit)

        panel.SetSizer(vbox) 
            
        self.Centre() 
        self.Show() 
        self.Fit()


    def get_words(self, file_path):
        with open(file_path, 'r') as f:
            text = f.readlines()
            length = len(text)
            wordsArr = []
            for i in range(length):
                words = text[i].split()
                wordsArr = wordsArr + words
            print(wordsArr)
        return wordsArr

    def send_message(self, phone_number, message):
        os.system('osascript send.scpt {} "{}"'.format(phone_number, message))

    def on_send(self, repeat_times, phone_number):
        words = self.get_words('words.txt')
        for i in range(repeat_times):
            word = ""
            for i in range(len(words)):
                word = words[i]
                print(word)
                self.send_message(phone_number, word)

def main():
        app = wx.App()
        ex = MainPage(None, title='Spam Your Friends!')
        ex.Show()
        app.MainLoop()


if __name__ == '__main__':
    main()