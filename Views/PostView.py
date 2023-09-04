import customtkinter
import logging
from Data import Post

class PostView(customtkinter.CTkFrame):
    def __init__(self,parent,post: Post):        
        super().__init__(parent)
        self.post = post
        logging.info(self.post)
        self.title = customtkinter.CTkLabel(self, text=self.post.title) 
        self.title.pack()
        