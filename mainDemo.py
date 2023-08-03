import tkinter
import customtkinter
from enum import Enum

# Note : Should play files from H:\Jimmy\Music\Juice WRLD\Legends Never Die [Explicit]

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        #App Frame
        self.title("DriveDev Home")
        self.geometry("400x150")
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)

        #Adding UI elements
        self.button = customtkinter.CTkButton(self, text="HelloWorld", command=self.button_callback)
        self.button.grid(row=3, column=0, padx=10, pady=10, sticky="ew", columnspan=2)

        self.checkbox_frame = customtkinter.CTkFrame(self)
        self.checkbox_frame.grid(row=0,column=0, padx=10, pady=(10,0))
        self.check_box_1 =customtkinter.CTkCheckBox(self.checkbox_frame, text="checkbox 1")
        self.check_box_1.grid(row=0, column=0, padx=10, pady=(10,0), sticky="w")
        self.check_box_2 =customtkinter.CTkCheckBox(self.checkbox_frame, text="checkbox 2")
        self.check_box_2.grid(row=1, column=0, padx=10, pady=(10,0), sticky="w")       

    def button_callback(self):
        print("Button pressed")
        

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
app = App()
#SystemSettings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")
app.mainloop()