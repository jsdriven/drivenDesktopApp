import tkinter
import customtkinter
import traceback
import Widgets
from Views import *
import logging
from tkinter import messagebox
from enum import Enum
import sys

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        

        #App Frame
        screen_width, screen_height = 900,900
        self.report_callback_exception = self.show_error
        self.activeTab ="NONE"
        screen_width, screen_height = self.winfo_screenwidth()-10, self.winfo_screenheight()-100
        logging.info(screen_width)
        logging.info(screen_height)
        logging.info('%dx%d+0+0' % (screen_width, screen_height))
        self.geometry("%dx%d+0+0" % (screen_width, screen_height))
        self.title("DriveDev Home")
        self.rowconfigure(0, weight=1)        
        self.columnconfigure(0, weight=1)   
        self.columnconfigure(1, weight=25)
        self.PageSelect = Widgets.PageSelect(parent=self, pages=[
                {"tabName":"Create Post","viewName":"CreatePostView"},
                {"tabName":"List Posts","viewName":"ListPostsView"}])
        self.PageSelect.grid(row=0,column=0,padx=10,pady=10, sticky="WENS")
        self.mainframe = customtkinter.CTkFrame(self)
        self.mainframe.grid(row=0,column=1,rowspan=10,columnspan=10,padx=10,pady=10,sticky="WENS")
        
        
        #Configure Grids for the main frame
        self.mainframe.rowconfigure(0, weight=1)        
        self.mainframe.columnconfigure(0, weight=1) 
        
        #Initialize each of the views under the main frame        
        self.mainframe.ListPosts = ListPostsView(parent=self.mainframe)
        #self.mainframe.ListPosts.bind('<Visibility>',lambda event:self.mainframe.ListPosts.onLoad)
        self.mainframe.CreatePost = CreatePostView(parent=self.mainframe)
        #self.mainframe.CreatePost.bind('<Visibility>',lambda event:logging.info("CreatePosts is visible"))
        
        #Bind each event for switching between tabs
        #Note it may be worth creating an event manager object for this as well
        self.bind("<<CreatePostView>>", lambda event:self.testMethod(event,"CreatePost"))
        self.bind("<<ListPostsView>>", lambda event:self.testMethod(event,"ListPosts"))
        
    #Switches between frames by compating against the active tab
    def testMethod(self,event,tabToOpen):
        logging.info("Event was emitted")
        logging.info("SwitchingTabs to %s" % tabToOpen)
        if self.activeTab != tabToOpen:
            if self.activeTab != "NONE":
                logging.info("Hiding current Tab %s" % self.activeTab)
                getattr(self.mainframe,self.activeTab).grid_remove()
            getattr(self.mainframe,tabToOpen).grid(sticky="WENS")
            self.activeTab = tabToOpen
    
    #Handles Crashes then closes.
    def show_error(self,*args):
        err = traceback.format_exception(*args)
        print(err)
        logging.info(err)
        messagebox.showerror('Exception',err)  
        self.destroy()


            
    
#Run app
#Establish configs for logging to file.
logging.basicConfig(filename='logs.log', level=logging.DEBUG)
app = App()
#SystemSettings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

#Start the main loop of the window
app.mainloop()
print("Window close")