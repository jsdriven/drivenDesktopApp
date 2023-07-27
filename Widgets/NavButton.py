import customtkinter
import logging

class NavButton(customtkinter.CTkButton):
    def __init__(self,parent,page):        
        super().__init__(parent)
        self.parent = parent 
        self.viewName = page.get("viewName")
        self.tabName = page.get("tabName")
        self.configure(text=self.tabName)
        self.configure(command=lambda: self.SwitchEvent(self.viewName))
            
    def SwitchEvent(self,pageName):
        logging.info("SwitchEvent fire from %s" % pageName)
        self.parent.event_generate("<<%s>>" % pageName)