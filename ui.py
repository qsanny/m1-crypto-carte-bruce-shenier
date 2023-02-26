from tkinter import * 
from coder import Encoder, Decoder
from keygen import * 

class Interface:
    def __init__(self) -> None:
        self.fenetre = Tk()

        label = Label(self.fenetre, text="Hello World")
        label.pack()

        # value = StringVar() 
        # value.set("texte par défaut")
        # entree = Entry(self.fenetre,  width=30)
        # entree.pack()

        self.message_box=Text(self.fenetre, height=2, width=10)
        self.message_box.pack()

        self.encoder = Encoder(KeyGenerator())

        # bouton de cryptage
        bouton=Button(self.fenetre, text="Encoder", command=self.encrypt)
        bouton.pack()

        
    
    def encrypt(self):
        inputValue=self.message_box.get("1.0","end-1c")
        print(inputValue)
        encoded_msg = self.encoder.encode(inputValue)
        print(encoded_msg)
        label = Label(self.fenetre, text=encoded_msg)
        label.pack()


    def show(self):
        self.fenetre.mainloop()




