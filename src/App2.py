from tkinter import *

class MailBox:

    def __init__(self):
        frame = Frame(root)
        frame.pack()

        bottomframe = Frame(root)
        bottomframe.pack( side = BOTTOM )

        for i in range(1,11):
            myButton = Button(frame, text="Email %d" % i, font = ("Verdana", 11), fg = "white", pady=5, bg="#152500")
            myButton.pack(side = TOP)

        self.bntVoltar = Button(frame, text="Sair", font=("Verdana", 10, "bold"), width=12)
        self.bntVoltar["command"] = self.loginPage
        self.bntExcluir.pack(side=BOTTOM)

    def loginPage():    
        print("hello")

    root = Tk()
    root.geometry("750x500")
    root.title("Caixa de Entrada")
    root.configure(background = '#807f80')
    root.mainloop()