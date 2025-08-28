import tkinter as tk
class GUI:
    def __init__(self,root):
        self.root = root
        self.root.title("C A L C U L A T O R")
        self.root.geometry("600x400")
        
        self.label = tk.Label(root, text="semen")
        self.label.pack(pady=20)
        
        #boton
        #self.boton = tk.Button(root,text="cambiar texto",command=self.cambiar_texto)
        #self.boton.pack()
        
        
        self.label_1 = tk.Label(root,text="calcular")
        self.label_1.pack()
        self.num_braket = tk.Entry()
        self.entry = self.num_braket.get()
        self.num_braket.pack()
        
        self.num_braket2 = tk.Entry()
        self.num_braket2.pack()
        
        self.num_braket3 = tk.Entry()
        self.num_braket3.pack()
    
    def cambiar_texto(self):
        self.label.config(text="texto cambiado")
   
def decToHex(num):
    print("lol"+num)
    Hex = 1001
    return Hex
    
     
if __name__ == "__main__":
    root = tk.Tk()
    app = GUI(root)
    root.mainloop()