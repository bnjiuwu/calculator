import tkinter as tk
from tkinter import messagebox
from PIL import Image,ImageTk
class GUI:
    def __init__(self,root):
        #---------- icono ----------
        self.icono = ImageTk.PhotoImage(file="monke.png")
        root.iconphoto(False, self.icono)

        #---------- Ventana -----------
        self.root = root
        self.root.title("C A L C U L A T O R")
        self.root.geometry("600x400")
        self.root.resizable(False,False)
        
        self.label = tk.Label(root, text="semen")
        self.label.pack(pady=20)
        
        #------------ input ------------
        self.entrada = tk.Entry(root, font= ("Arial",14),justify = "center")
        self.entrada.place(x= 50,y=40,width=350,height=40)


        #-------------boton---------------
        self.boton1 = tk.Button(root,text="Calcular",bg="#0099cc" , fg="white",font=("Arial",12,"bold"))
        self.boton1.place(x= 420,y=40,width=120,height=40)

        #--------- labels & exits
        tk.Label(root,text="Decimal",font=("Arial",12,"bold")).place(x=50,y=100)
        self.salida_decimal = tk.Entry(root,font=("Arial",12,"bold"),state= "readonly")
        self.salida_decimal.place(x=150,y=100,width=200,height=30)

        tk.Label(root,text="Octal",font=("Arial",12,"bold")).place(x=50,y=150)
        self.salida_Octal = tk.Entry(root,font=("Arial",12,"bold"),state= "readonly")
        self.salida_Octal.place(x=150,y=150,width=200,height=30)

        tk.Label(root,text="Binario",font=("Arial",12,"bold")).place(x=50,y=200)
        self.salida_Binario = tk.Entry(root,font=("Arial",12,"bold"),state= "readonly")
        self.salida_Binario.place(x=150,y=200,width=200,height=30)

        tk.Label(root,text="Hexadecimal",font=("Arial",12,"bold")).place(x=40,y=250)
        self.salida_Hexadecimal = tk.Entry(root,font=("Arial",12,"bold"),state= "readonly")
        self.salida_Hexadecimal.place(x=150,y=250,width=200,height=30)
        #------marco imagen-----------
        self.imagen_frame = tk.Frame(root,width=180,height=200,relief="solid",borderwidth=1)
        self.imagen_frame.place(x=370,y=120)

        try:
            img = Image.open("nokotan.png")
            img = img.resize((180, 200))   # Ajustar tamaño al marco
            imagen = ImageTk.PhotoImage(img)

            lbl_imagen = tk.Label(self.imagen_frame, image=imagen)
            lbl_imagen.place(relx=0.5, rely=0.5, anchor="center")

            # Mantener referencia para que no se borre de memoria
            lbl_imagen.image = imagen

        except Exception as e:
            tk.Label(self.imagen_frame, text="No se pudo cargar\nla imagen", fg="red").place(relx=0.5, rely=0.5, anchor="center")
            print("Error cargando imagen:", e)

        
    def semen():
        print("semne2")
    
    def cambiar_texto(self):
        self.label.config(text="texto cambiado")
   
def decToHex(num):
    
    check = []
    
    if "," in num:
        print("plop")

    return num    
     
if __name__ == "__main__":
    root = tk.Tk()
    app = GUI(root)
    root.mainloop()