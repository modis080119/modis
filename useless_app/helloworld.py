#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 19:50:21 2019

@author: om
"""

#from kivy.app import App
#from kivy.uix.label import Label
#from kivy.uix.textinput import TextInput
#from kivy.uix.gridlayout import GridLayout
#
#
#class LoginScreen(GridLayout):
#    def __init__(self, *args, **kwargs):
#        super(LoginScreen, self).__init__(*args, **kwargs)
#        self.cols = 2
#        
#        self.add_widget(Label(text='Username'))
#        self.username = TextInput(multiline=False)
#        self.add_widget(self.username)
#        
#        
#
#    
#
#class SimpleApp(App):
#    def build(self):
##        return Label(text='Hello World!!!')
#        return LoginScreen()
#    
#if __name__ == '__main__':
#    SimpleApp().run()
    



from kivy.app import App
from kivy.uix.label import Label        

class SimpleApp(App):
    def build(self):
        return Label() #text='Hello World!!!')
    
if __name__ == '__main__':
    SimpleApp().run()


