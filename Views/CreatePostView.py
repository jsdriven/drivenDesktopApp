import customtkinter
import logging

class CreatePostView(customtkinter.CTkFrame):
    def __init__(self,parent):        
        super().__init__(parent)
        self.text = customtkinter.CTkLabel(self, text="CreatePostView")
        self.text.pack()

    
    def onLoad():
        logging.info("hello")


