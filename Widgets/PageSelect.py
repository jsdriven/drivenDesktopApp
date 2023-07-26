import customtkinter
import logging

class PageSelect(customtkinter.CTkFrame):
    def __init__(self,parent,pages):        
        super().__init__(parent)
        self.columnconfigure(0,weight=1)
        currentRow = 0
        #Dictionary of page buttons, will need to add reference to panels as well
        pageDict = {}
        for page in pages:
            print(page)
            logging.info(page)
            pageDict[page] = customtkinter.CTkButton(self, text=page)
            pageDict[page].grid(row=currentRow, column=0, padx=10, pady=10,sticky="WE")
            currentRow+=1
