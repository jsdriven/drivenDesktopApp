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


#Run app
app = App()
#SystemSettings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")
app.mainloop()