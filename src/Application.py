from tkinter import *
import myPOP3
 
class Application:
    def __init__(self, master=None):

        self.fonte = ("Verdana", "10")
    
        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()
        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()
        self.container3 = Frame(master)
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.pack()
        self.container4 = Frame(master)
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.pack()
        self.container5 = Frame(master)
        self.container5["padx"] = 20
        self.container5["pady"] = 5
        self.container5.pack()
        self.container6 = Frame(master)
        self.container6["padx"] = 20
        self.container6["pady"] = 5
        self.container6.pack()
        self.container7 = Frame(master)
        self.container7["padx"] = 20
        self.container7["pady"] = 5
        self.container7.pack()
        self.container8 = Frame(master)
        self.container8["padx"] = 20
        self.container8["pady"] = 10
        self.container8.pack()
        self.container9 = Frame(master)
        self.container9["pady"] = 15
        self.container9.pack()
    
        self.titulo = Label(self.container1, text="Correio Eletrônico")
        self.titulo["font"] = ("Verdana", "13", "bold")
        self.titulo.pack()

        self.lblport= Label(self.container4, text="Porta: ", font=self.fonte, width=10, height=2)
        self.lblport.pack(side=LEFT)
    
        self.port = Entry(self.container4)
        self.port["width"] = 25
        self.port["font"] = self.fonte
        self.port.pack(side=LEFT)
    
        self.lblemail= Label(self.container5, text="Email: ", font=self.fonte, width=10, height=2)
        self.lblemail.pack(side=LEFT)
    
        self.usuario = Entry(self.container5)
        self.usuario["width"] = 25
        self.usuario["font"] = self.fonte
        self.usuario.pack(side=LEFT)
    
        self.lblsenha= Label(self.container7, text="Senha: ", font=self.fonte, width=10, height=3)
        self.lblsenha.pack(side=LEFT)
    
        self.senha = Entry(self.container7)
        self.senha["width"] = 25
        self.senha["show"] = "*"
        self.senha["font"] = self.fonte
        self.senha.pack(side=LEFT)
    
        self.bntInsert = Button(self.container8, text="Login", font=("Verdana", 10, "bold"), width=12)
        self.bntInsert["command"] = self.loginAction
        self.bntInsert.pack (side=LEFT)
    
        self.bntExcluir = Button(self.container8, text="Cancelar", font=("Verdana", 10, "bold"), width=12)
        self.bntExcluir["command"] = self.closeApp
        self.bntExcluir.pack(side=LEFT)
    
        self.lblmsg = Label(self.container9, text="")
        self.lblmsg["font"] = ("Verdana", "9", "italic")
        self.lblmsg.pack()
    
    
    def loginAction(self):
        usuario = self.usuario.get()
        senha = self.senha.get()

        Mailbox = myPOP3.POP3_SSL('pop.googlemail.com', '995')
        Mailbox.user(usuario) 
        Mailbox.pass_(senha)
        
        for i in range(1):
            for msg in Mailbox.retr(i+1)[1]:
                print (msg)
        Mailbox.quit()
      
    def closeApp(self):
        root.destroy()

root = Tk()
Application(root)
root.geometry("400x405")
root.resizable(0, 0)
root.title("Correio eletronico")
root.mainloop()
 
 
