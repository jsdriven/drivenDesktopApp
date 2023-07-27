import customtkinter
import logging

class ListPostsView(customtkinter.CTkFrame):
    def __init__(self,parent):        
        super().__init__(parent)
        self.bind('<Visibility>',lambda event:self.onLoad(event=event))
        #Below should be replace with Grid of Posts 
        # This will need to use Data.Post
        self.text = customtkinter.CTkLabel(self, text="ListPostsView")
        self.text.pack()

    #TODO This will need to handle fetching of items via pymongo
    def onLoad(self,event):
        logging.info("LOADING LIST View")
        logging.info(event)