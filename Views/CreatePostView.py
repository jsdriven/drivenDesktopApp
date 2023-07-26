import customtkinter
import logging

class CreatePostView(customtkinter.CTkFrame):
    def __init__(self,parent):        
        super().__init__(parent)
        self.text = customtkinter.CTkLabel(self, text="CreatePostView")
        self.text.pack()
        self.bind('<Expose>', logging.info("Expose"))
        self.bind('<FocuseIn>', logging.info("FocusIn"))
        self.bind('<Destroy>', logging.info("Destroy"))

    
    def onLoad():
        logging.info("hello")


