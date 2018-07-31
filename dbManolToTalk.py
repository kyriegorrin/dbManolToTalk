from tkinter import *
from tkinter import ttk, font

#GUI CLASS
class AppGUI():
    def __init__(self):
        #Window configuration
        self.window = Tk()
        self.window.geometry("500x200")
        self.window.resizable(0,0)
        self.window.configure(bg = "white")
        self.window.title("dbManolToTalk")
        self.window.iconbitmap("imanol.ico")
        
        #Miscellaneous variables
        self.imanolOriginal = PhotoImage(file="imanol.png")
        self.imanol = self.imanolOriginal.subsample(3)
        
        self.myFont = font.Font(weight="bold")

        self.sens = 0

        #Widget definition
        #TODO: commands for buttons
        self.talkKey = ttk.Button(self.window, text = "KEY BIND: V")
        self.stopKey = ttk.Button(self.window, text = "STOP KEY: F5")

        self.sensLabel = ttk.Label(self.window, text="Sensitivity", 
                                    font=self.myFont, background="white")

        self.slider = ttk.Scale(self.window, 
                                command=self.refreshIndicator,
                                orient = HORIZONTAL,
                                length=250,
                                from_=0.0,
                                to=100.0)

        self.canvas = Canvas(self.window, width=150, height=150, bg="white")

        #Widget configuration
        self.canvas.create_rectangle(75-self.sens, 75-self.sens,75+self.sens, 75+self.sens, fill="grey", outline="grey")
        self.canvas.create_image(75, 75, image=self.imanol, anchor=CENTER)

        #Widget placement
        self.canvas.place(x=10, y=25)
        self.sensLabel.place(x=200, y=50)
        self.slider.place(x=200, y=75)
        self.talkKey.place(x=250, y=150)
        self.stopKey.place(x=350, y=150)

    #Method for the canvas refresh
    def refreshIndicator(self, val):
        self.sens = self.slider.get()
        self.canvas.delete("all")
        self.canvas.create_rectangle(75-self.sens/2, 75-self.sens/2,75+self.sens/2, 75+self.sens/2, fill="grey", outline="grey")
        self.canvas.create_image(75, 75, image=self.imanol, anchor=CENTER)

    #Method to obtain the root for control purposes
    def getRoot(self):
        return self.window
        

#AUDIO CLASS
#class DbManolDetector():
#    def __init__(self):


#MAIN
def main():
    gui = AppGUI()
    guiRoot = gui.getRoot()

    #Main while
    while True:
        print("hello")
        
        #Non-blocking subtitutes for tk.mainloop()
        guiRoot.update_idletasks()
        guiRoot.update()        

    return 0

if __name__ == "__main__":
    main()