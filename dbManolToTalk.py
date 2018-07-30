from tkinter import *
from tkinter import ttk

#GUI part
class AppGUI():
    def __init__(self):
        #Window configuration
        window = Tk()
        window.geometry("500x200")
        window.resizable(0,0)
        window.configure(bg = "white")
        window.title("dbManolToTalk")
        
        #Miscellaneous variables
        imanolOriginal = PhotoImage(file="imanol.png")
        imanol = imanolOriginal.subsample(2)

        #Widget definition
        #TODO: commands for buttons
        self.talkKey = ttk.Button(window, text = "KEY BIND: V")
        self.stopKey = ttk.Button(window, text = "STOP KEY: F5")

        self.canvas = Canvas(window, width=150, height=150, bg="white")

        #Widget configuration
        self.canvas.create_image(75, 75, image=imanol, anchor=CENTER)

        #Widget placement
        self.canvas.pack(side=LEFT)

        #Whatever the fuck this is
        window.mainloop()

def main():
    gui = AppGUI()
    return 0

if __name__ == "__main__":
    main()