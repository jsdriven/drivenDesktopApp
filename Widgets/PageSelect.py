import customtkinter
import logging
import Widgets

class PageSelect(customtkinter.CTkFrame):
    def __init__(self,parent,pages):        
        super().__init__(parent)
        self.columnconfigure(0,weight=1)
        self.parent = parent 
        currentRow = 0
        for page in pages:
            currentButton = Widgets.NavButton(self, page)
            currentButton.grid(row=currentRow, column=0, padx=10, pady=10,sticky="WE")
            currentRow+=1
            