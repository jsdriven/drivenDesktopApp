import tkinter
import customtkinter
import traceback
import Widgets
from Views import *
import logging
from tkinter import messagebox
from enum import Enum
import sys

# Note : Should play files from H:\Jimmy\Music\Juice WRLD\Legends Never Die [Explicit]

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        #App Frame
        screen_width, screen_height = 900,900
        
        screen_width, screen_height = self.winfo_screenwidth()-10, self.winfo_screenheight()-100
        logging.info(screen_width)
        logging.info(screen_height)
        logging.info('%dx%d+0+0' % (screen_width, screen_height))
        self.geometry("%dx%d+0+0" % (screen_width, screen_height))
        self.title("DriveDev Home")
        self.rowconfigure(0, weight=1)        
        self.columnconfigure(0, weight=1)   
        self.columnconfigure(1, weight=7)
        self.PageSelect = Widgets.PageSelect(self, ["CreatePostView","ListPostsView"])
        self.PageSelect.grid(row=0,column=0,padx=10,pady=10, sticky="WENS")
        self.mainframe = customtkinter.CTkFrame(self)
        self.mainframe.grid(row=0,column=1,rowspan=10,columnspan=10,padx=10,pady=10,sticky="WENS")

class AppV2(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        #App Frame
        screen_width, screen_height = 900,900        
        screen_width, screen_height = self.winfo_screenwidth()-10, self.winfo_screenheight()-100
        logging.info('ScreenDimensions: %dx%d+0+0' % (screen_width, screen_height))
        self.geometry("%dx%d+0+0" % (screen_width, screen_height))
        self.title("DriveDev Home")   
        logging.info("Creating main View")
        self.mainview = MainView(
            master=self,
            pages=[
                {"tabName":"Create Post","viewName":"CreatePostView"},
                {"tabName":"List Posts","viewName":"ListPostsView"}]) 
        self.mainview.pack(fill="both", expand=True, padx=10,pady=10) 

class MainView(customtkinter.CTkTabview):    
    def __init__(self,master,pages):        
        super().__init__(master) 
        #self.bind("<Expose>", logging.info("Tabchanges"))
        for page in pages:
            logging.info(page.get("tabName"))
            logging.info(page.get("viewName"))
            logging.info(eval(page.get("viewName")))
            currentTab = self.add(page.get("tabName"))
            tabView = eval(page.get("viewName"))(currentTab)
            #Something needs to be added below to add a function for when
            #tab is loaded.
            #currentTab.command = tabView.onLoad
            logging.info(currentTab)
            currentTab.main = tabView
            currentTab.main.pack(fill="both", expand=True)
            logging.info(currentTab)
            
    
#Run app

logging.basicConfig(filename='logs.log', level=logging.DEBUG)
#logging.basicConfig(level=logging.DEBUG)
app = AppV2()
#SystemSettings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")
app.mainloop()
print("Window close")
#input("Enter to close")