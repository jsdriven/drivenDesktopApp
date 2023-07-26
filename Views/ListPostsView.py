import customtkinter
import logging

class ListPostsView(customtkinter.CTkFrame):
    def __init__(self,parent):        
        super().__init__(parent)
        self.text = customtkinter.CTkLabel(self, text="ListPostsView")
        self.text.pack()

    def onLoad():
        logging.info("hello")