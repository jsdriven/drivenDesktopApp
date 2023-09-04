import customtkinter
import logging
import Widgets

class PostTable(customtkinter.CTkFrame):
    def __init__(self,parent,posts):        
        super().__init__(parent)