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

        self.numero = tk.Label(root, text="Numero",font=("Comic Sans MS",12))
        self.numero.place(x=50,y=10)

        self.base = tk.Label(root, text="Base",font=("Comic Sans MS",12))
        self.base.place(x=250,y=10)

        #------------ input ------------
        self.entrada = tk.Entry(root, font= ("Arial",14),justify = "center")
        self.entrada.place(x= 50,y=40,width=150,height=40)
        
        self.base_var = tk.StringVar(value="10")
        self.base_menu = tk.OptionMenu(root, self.base_var, "2", "8", "10", "16")
        self.base_menu.config(font=("Comic Sans MS",12),bg="#cc004e",fg="white")
        self.base_menu.place(x=250, y=40, width=80, height=40)

        #-------------boton---------------
        self.boton1 = tk.Button(root,text="Calcular",bg="#0099cc" , fg="white",font=("Comic Sans MS",12),command=self.calcular_todo)
        self.boton1.place(x= 420,y=40,width=120,height=40)

        #--------- labels & exits
        tk.Label(root,text="Decimal",font=("Comic Sans MS",12,"bold")).place(x=50,y=100)
        self.salida_decimal = tk.Entry(root,font=("Comic Sans MS",12,"bold"),state= "readonly")
        self.salida_decimal.place(x=150,y=100,width=200,height=30)

        tk.Label(root,text="Octal",font=("Comic Sans MS",12,"bold")).place(x=50,y=150)
        self.salida_Octal = tk.Entry(root,font=("Comic Sans MS",12,"bold"),state= "readonly")
        self.salida_Octal.place(x=150,y=150,width=200,height=30)

        tk.Label(root,text="Binario",font=("Comic Sans MS",12,"bold")).place(x=50,y=200)
        self.salida_Binario = tk.Entry(root,font=("Comic Sans MS",12,"bold"),state= "readonly")
        self.salida_Binario.place(x=150,y=200,width=200,height=30)

        tk.Label(root,text="Hexadecimal",font=("Comic Sans MS",12,"bold")).place(x=40,y=250)
        self.salida_Hexadecimal = tk.Entry(root,font=("Comic Sans MS",12,"bold"),state= "readonly")
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

    def get_numero(self):
        num_str = self.entrada.get().strip()
        base = self.base_var.get()
        
        if not num_str:
            messagebox.showerror("Error", "Por favor ingrese un número.")
            return None, None
        try:
            if base == "10":
                num = float(num_str)
            else:
                if "." in num_str:
                    messagebox.showerror("Error", "Por favor ingrese un número entero.")
                    return None, None
                num = int(num_str, int(base))
            return num, base
        except ValueError:
            messagebox.showerror("Error", "Entrada inválida. Por favor ingrese un número.")
            return None, None

       

    def NumToBin(self):
        num_str = self.entrada.get()

        if not num_str.strip():
            messagebox.showerror("Error", "Por favor ingrese un número.")
            return
        try:
            num = int(num_str)
        except ValueError:
            messagebox.showerror("Error", "Entrada inválida. Por favor ingrese un número entero.")
            return
        binario = ""
        n = num

        if n == 0:
            binario = "0"
        else:
            while n >0:
                resto = n % 2
                n //= 2
                binario = str(resto) + binario

        self.salida_Binario.config(state="normal")
        self.salida_Binario.delete(0, tk.END)
        self.salida_Binario.insert(0, binario)
        self.salida_Binario.config(state="readonly")    
        print(binario)

    def NumToHex(self):

        self.salida_Hexadecimal.config(state="normal")
        self.salida_Hexadecimal.delete(0, tk.END)
        self.salida_Hexadecimal.insert(0, hex(int(self.entrada.get()))[2:])
        self.salida_Hexadecimal.config(state="readonly")
        print(hex(int(self.entrada.get()))[2:])


    
    def NumToOct(self):
        self.salida_Octal.config(state="normal")
        self.salida_Octal.delete(0, tk.END)
        self.salida_Octal.insert(0, oct(int(self.entrada.get()))[2:])
        self.salida_Octal.config(state="readonly")
        print()

    def NumToDec(self):
        self.salida_decimal.config(state="normal")
        self.salida_decimal.delete(0, tk.END)
        self.salida_decimal.insert(0, str(int(self.entrada.get())))
        self.salida_decimal.config(state="readonly")
        print(int(self.entrada.get()))

    def calcular_todo(self):
        if self.base_var.get() == "2":
            self.NumToBin()
        elif self.base_var.get() == "8":
            self.NumToOct()
        elif self.base_var.get() == "10":
            self.NumToDec()
        elif self.base_var.get() == "16":
            self.NumToHex()

if __name__ == "__main__":
    root = tk.Tk()
    app = GUI(root)


    root.mainloop()


