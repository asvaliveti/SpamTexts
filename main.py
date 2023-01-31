import os
from time import sleep
import wx

class MainPage(wx.Frame):
    # state variables to track changes to text field
    phone = ""
    repeat = ""
    msg = ""

    def __init__(self, parent, title):
        super(MainPage, self).__init__(parent, title=title, size=(500, 400))

        panel = wx.Panel(self) 
        vbox = wx.BoxSizer(wx.VERTICAL) 
        
        # create horizontal box 1, label phone number and text field
        hbox1 = wx.BoxSizer(wx.HORIZONTAL) 
        l1 = wx.StaticText(panel, -1, "Phone number (ex: +12345678900) ") 
        hbox1.Add(l1, 1, wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)

        self.phone_text = wx.TextCtrl(panel)    
        hbox1.Add(self.phone_text,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5) 
        self.phone_text.Bind(wx.EVT_TEXT,self.onPhoneTyped) 
        vbox.Add(hbox1) 
            

        # create horizontal box 2, label repeat number and create text field
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        l2 = wx.StaticText(panel, -1, "How many times should I spam them? ") 
        hbox2.Add(l2, 1, wx.ALIGN_LEFT|wx.ALL,5) 

        self.repeat_text = wx.TextCtrl(panel)    
        hbox2.Add(self.repeat_text,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5) 
        vbox.Add(hbox2) 
        self.repeat_text.Bind(wx.EVT_TEXT,self.onRepeatTyped)
            
        # create horizontal box 3, label msg to send, and create text field
        hbox3 = wx.BoxSizer(wx.HORIZONTAL) 
        l3 = wx.StaticText(panel, -1, "Text to spam with")     
        hbox3.Add(l3,1, wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5) 

        self.msg_text = wx.TextCtrl(panel,size = (200,100),style = wx.TE_MULTILINE) 
        hbox3.Add(self.msg_text,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5) 
        vbox.Add(hbox3) 
        self.msg_text.Bind(wx.EVT_TEXT, self.onTextTyped)

        # create the submit button and add it to the bottom
        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        self.submit_individually = wx.Button(panel, -1, "Send word by word!")
        self.submit_individually.Bind(wx.EVT_BUTTON, self.on_send_individually)
        hbox4.Add(self.submit_individually, 1, wx.EXPAND|wx.ALL, 5)

        self.submit_line = wx.Button(panel, -1, "Send line by line!")
        self.submit_line.Bind(wx.EVT_BUTTON, self.on_send_by_line)
        hbox4.Add(self.submit_line, 1, wx.EXPAND|wx.ALL, 5)
        vbox.Add(hbox4)

        panel.SetSizer(vbox) 
        
        # show the panel
        self.Centre() 
        self.Show() 
        self.Fit()


    def onPhoneTyped(self, event):
        self.phone = self.phone_text.GetValue()

    def onRepeatTyped(self, event):
        self.repeat = self.repeat_text.GetValue()

    def onTextTyped(self, event):
        self.msg = self.msg_text.GetValue()

    def get_words_individually(self, text):
        return text.split()

    def get_words_by_line(self, text):
        return text.split("\n")

    def send_message(self, phone_number, message):
        os.system('osascript send.scpt {} "{}"'.format(phone_number, message))

    def disable_fields(self):
        # Disable text fields while sending
        self.phone_text.Disable()
        self.repeat_text.Disable()
        self.msg_text.Disable()
        self.submit_individually.Disable()
        self.submit_line.Disable()

    def enable_fields(self):
        # Disable text fields while sending
        self.phone_text.Enable()
        self.repeat_text.Enable()
        self.msg_text.Enable()
        self.submit_individually.Enable()
        self.submit_line.Enable()

    def on_send_individually(self, event):
        words = self.get_words_individually(self.msg)

        self.disable_fields()

        # send each word a given amount of times
        for i in range(int(self.repeat)):
            for word in words:
                print(word)
                self.send_message(self.phone, word)

        self.enable_fields()

        # clear the value of the text fields
        self.repeat_text.SetValue("")
        self.msg_text.SetValue("")

    def on_send_by_line(self, event):
        words = self.get_words_by_line(self.msg)

        self.disable_fields()

        # send each word a given amount of times
        for i in range(int(self.repeat)):
            for line in words:
                print(line)
                self.send_message(self.phone, line)

        self.enable_fields()
        
        # clear the value of the text fields
        self.repeat_text.SetValue("")
        self.msg_text.SetValue("")

def main():
        app = wx.App()
        ex = MainPage(None, title='Spam Your Friends!')
        ex.Show()
        app.MainLoop()


if __name__ == '__main__':
    main()