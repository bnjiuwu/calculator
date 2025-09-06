import tkinter as tk
from tkinter import messagebox
from unittest import case
from PIL import Image,ImageTk
class GUI:
    def __init__(self,root):

        #---------- Ventana -----------
        self.root = root
        self.root.title("C A L C U L A T O R")
        self.root.geometry("600x400")
        self.root.resizable(False,False)

        self.numero = tk.Label(root, text="Numero",font=("Comic Sans MS",12))
        self.numero.place(x=50,y=10)

        self.base = tk.Label(root, text="Origen",font=("Comic Sans MS",12))
        self.base.place(x=250,y=10) 

        tk.Label(root, text="a",font=("Comic Sans MS",12)).place(x=330,y=10)

        #------------ input ------------
        self.entrada = tk.Entry(root, font= ("Arial",14),justify = "center")
        self.entrada.place(x= 50,y=40,width=150,height=40)
        
        self.base_var = tk.StringVar(value="10")
        self.base_menu = tk.OptionMenu(root, self.base_var, "2", "8", "10", "16")
        self.base_menu.config(font=("Comic Sans MS",12),bg="#cc004e",fg="white")
        self.base_menu.place(x=350, y=40, width=80, height=40)

        tk.Label(root, text="Base",font=("Comic Sans MS",12)).place(x=350,y=10)
        self.origen = tk.StringVar(value="Decimal")
        self.origen_menu = tk.OptionMenu(root, self.origen, "Decimal", "Octal", "Binario", "Hexadecimal")
        self.origen_menu.config(font=("Comic Sans MS",12),bg="#00cc22",fg="white")
        self.origen_menu.place(x=210, y=40, width=130, height=40)

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
        self.imagen_frame.place(x=370,y=100)

        self.image2_frame = tk.Frame(root,width=400,height=100,relief="solid",borderwidth=1)
        self.image2_frame.place(x=50,y=300)

        self.image3_frame = tk.Frame(root,width=100,height=100,relief="solid",borderwidth=1)
        self.image3_frame.place(x=450,y=300)

        try:
            img = Image.open("nokotan.png")
            img = img.resize((180, 200))   # Ajustar tamaño al marco
            imagen = ImageTk.PhotoImage(img)

            img2 = Image.open("tama-chan.png")
            img2 = img2.resize((400, 100))
            imagen2 = ImageTk.PhotoImage(img2)

            img3 = Image.open("camello.png")
            img3 = img3.resize((100, 100))
            imagen3 = ImageTk.PhotoImage(img3)

            lbl_imagen = tk.Label(self.imagen_frame, image=imagen)
            lbl_imagen.place(relx=0.5, rely=0.5, anchor="center")

            lbl_imagen2 = tk.Label(self.image2_frame, image=imagen2)
            lbl_imagen2.place(relx=0.5, rely=0.5, anchor="center")

            lbl_imagen3 = tk.Label(self.image3_frame, image=imagen3)
            lbl_imagen3.place(relx=0.5, rely=0.5, anchor="center")

            # Mantener referencia para que no se borre de memoria
            lbl_imagen.image = imagen
            lbl_imagen2.image = imagen2
            lbl_imagen3.image = imagen3

        except Exception as e:
            tk.Label(self.imagen_frame, text="No se pudo cargar\nla imagen", fg="red").place(relx=0.5, rely=0.5, anchor="center")
            print("Error cargando imagen:", e)

    def NumToBin(self, num_str):
        try:
            num = float(num_str)
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese un número válido.")
            return None, None

        ent = int(num)
        frac = num - ent
        
        bin_ent = ""
        while ent > 0:
            resto = ent % 2
            ent //= 2
            bin_ent = str(resto) + bin_ent
        
        bin_frac = ""
        
        f = frac 
        count = 0
        
        while f > 0 and count < 4:
            f *= 2
            bit = int(f)
            bin_frac += str(bit)
            f -= bit
            count += 1
            
        binario = bin_ent
        if bin_frac:
            binario += "." + bin_frac

        self.salida_Binario.config(state="normal")
        self.salida_Binario.delete(0, tk.END)
        self.salida_Binario.insert(0, binario)
        self.salida_Binario.config(state="readonly")
        print(bin(int(self.entrada.get()))[2:])

    def NumToHex(self,num_str):
        try:
            num = float(num_str)
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese un número válido.")
            return None, None
        
        abc = ["A","B","C","D","E","F"]
        int_ = [10,11,12,13,14,15]
        
        ent = int(num)
        frac = num - ent

        hex_ent = ""
        while ent > 0:
            resto = ent % 16
            ent //= 16
            if resto in int_:
                resto = abc[int_.index(resto)]
            hex_ent = str(resto) + hex_ent

        hex_frac = ""

        f = frac
        count = 0
        
        while f > 0 and count < 4:
            f *= 16
            bit = int(f)
            f -= bit
            if bit in int_: bit = abc[int_.index(bit)]
            hex_frac += str(bit)
            count += 1

        hexadecimal = hex_ent
        if hex_frac:
            hexadecimal += "." + hex_frac

        
        self.salida_Hexadecimal.config(state="normal")
        self.salida_Hexadecimal.delete(0, tk.END)
        self.salida_Hexadecimal.insert(0, hexadecimal.upper())
        self.salida_Hexadecimal.config(state="readonly")
        print(hex(int(self.entrada.get()))[2:])

    def NumToOct(self, num_str):
        try:
            num = float(num_str)
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese un número válido.")
            return None, None

        ent = int(num)
        frac = num - ent
        
        oct_ent = ""
        while ent > 0:
            resto = ent % 8
            ent //= 8
            oct_ent = str(resto) + oct_ent

        oct_frac = ""

        f = frac
        count = 0
        
        while f > 0 and count < 4:
            f *= 8
            bit = int(f)
            oct_frac += str(bit)
            f -= bit
            count += 1

        octal = oct_ent
        if oct_frac:
            octal += "." + oct_frac

        self.salida_Octal.config(state="normal")
        self.salida_Octal.delete(0, tk.END)
        self.salida_Octal.insert(0, octal)
        self.salida_Octal.config(state="readonly")
        print(oct(int(self.entrada.get()))[2:])

    def NumToDec(self,num_str):
        try:
            num = float(num_str)
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese un número válido.")
            return None, None

        ent = int(num)
        frac = num - ent
        
        dec_ent = ""
        while ent > 0:
            resto = ent % 10
            ent //= 10
            dec_ent = str(resto) + dec_ent

        dec_frac = ""

        f = frac
        count = 0
        
        while f > 0 and count < 4:
            f *= 10
            bit = int(f)
            dec_frac += str(bit)
            f -= bit
            count += 1

        decimal = dec_ent
        if dec_frac:
            decimal += "." + dec_frac

        self.salida_decimal.config(state="normal")
        self.salida_decimal.delete(0, tk.END)
        self.salida_decimal.insert(0, decimal)
        self.salida_decimal.config(state="readonly")
        print(float(self.entrada.get()))

    def HexToDec(self,hex_str):
    
        dic_hex = {"A":10,"B":11,"C":12,"D":13,"E":14,"F":15}

        for c in hex_str:
            if c not in "0123456789ABCDEF.":
                messagebox.showerror("Error", "El número hexadecimal solo puede contener dígitos del 0 al 9, letras de la A a la F y un punto.")
                return None, None
        
        decimal = 0

        for i, char in enumerate(reversed(hex_str.split(".")[0])):
            if char in dic_hex:
                decimal += dic_hex[char] * (16 ** i)
            else:
                decimal += int(char) * (16 ** i)

        if len(hex_str.split(".")) > 1:
            f = 0
            for i, char in enumerate(hex_str.split(".")[1]):
                if char in dic_hex:
                    f += dic_hex[char] * (16 ** - (i + 1))
                else:
                    f += int(char) * (16 ** - (i + 1))
            self.salida_decimal.config(state="normal")
            self.salida_decimal.delete(0, tk.END)
            self.salida_decimal.insert(0, str(decimal) + str(f).replace("0.","."))  # Concatenar parte entera y fraccionaria
            self.salida_decimal.config(state="readonly")
            return str(decimal) + str(f).replace("0.",".")
            
        else:
            self.salida_decimal.config(state="normal")
            self.salida_decimal.delete(0, tk.END)
            self.salida_decimal.insert(0, decimal)
            self.salida_decimal.config(state="readonly")
            
            print(decimal)
            return str(decimal)
        
        


    def BinToDec(self,bin_str):

        for c in bin_str:
            if c not in "01.":
                messagebox.showerror("Error", "El número binario solo puede contener 0, 1 y un punto.")
                return None, None
        try:
            num = float(bin_str)
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese un número válido.")
            return None, None

        entero = 0
        
        for i, bit in enumerate(reversed(bin_str.split(".")[0])):
            entero += int(bit) * (2 ** i)

        if len(bin_str.split(".")) > 1:

            fraccion = 0
            for i, bit in enumerate(bin_str.split(".")[1]):
                fraccion += int(bit) * (2 ** -(i + 1))

            self.salida_decimal.config(state="normal")
            self.salida_decimal.delete(0, tk.END)
            self.salida_decimal.insert(0, str(entero) + str(fraccion).replace("0.","."))  # Concatenar parte entera y fraccionaria
            self.salida_decimal.config(state="readonly")
            print(str(entero) + str(fraccion).replace("0.","."))
            return str(entero) + str(fraccion).replace("0.",".")
        else:
            self.salida_decimal.config(state="normal")
            self.salida_decimal.delete(0, tk.END)
            self.salida_decimal.insert(0, str(entero) + "0")  # Si no hay parte fraccionaria
            self.salida_decimal.config(state="readonly")
            print(str(entero))
            return str(entero)

        
    
    def OctToDec(self,oct_str):
        
        try:
            temp = float(oct_str)
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese un número válido.")
            return None, None
        
        entero = 0

        for i, bit in enumerate(reversed(oct_str.split(".")[0])):
            entero += int(bit) * (8 ** i)

        if len(oct_str.split(".")) > 1:

            fraccion = 0
            for i, bit in enumerate(oct_str.split(".")[1]):
                fraccion += int(bit) * (8 ** -(i + 1))

            self.salida_decimal.config(state="normal")
            self.salida_decimal.delete(0, tk.END)
            self.salida_decimal.insert(0, str(entero) + str(fraccion).replace("0.","."))  # Concatenar parte entera y fraccionaria
            self.salida_decimal.config(state="readonly")
            return str(entero) + str(fraccion).replace("0.",".")
        else:
            self.salida_decimal.config(state="normal")
            self.salida_decimal.delete(0, tk.END)
            self.salida_decimal.insert(0, str(entero) + ".0")  # Si no hay parte fraccionaria
            self.salida_decimal.config(state="readonly")
            print(str(entero))
            return str(entero)



    def calcular_todo(self):
        base = self.base_var.get()
        origen = self.origen.get()
        num_str= self.entrada.get().strip().replace(",", ".").upper()

        match origen:
            case "Decimal":
                match base:
                    case "2":
                        self.NumToBin(num_str)
                    case "8":
                        self.NumToOct(num_str)
                    case "10":
                        self.NumToDec(num_str)
                    case "16":
                        self.NumToHex(num_str)
            case "Binario":
                match base:
                    case "8":
                        self.NumToOct(self.BinToDec(num_str))
                    case "10":
                        self.BinToDec(num_str)
                    case "16":
                        self.NumToHex(self.BinToDec(num_str))
            case "Octal":
                match base:
                    case "2":
                        self.NumToBin(self.OctToDec(num_str))
                    case "10":
                        self.OctToDec(num_str)
                    case "16":
                        self.NumToHex(self.OctToDec(num_str))
            case "Hexadecimal":
                match base:
                    case "2":
                        self.NumToBin(self.HexToDec(num_str))
                    case "8":
                        self.NumToOct(self.HexToDec(num_str))
                    case "10":
                        self.HexToDec(num_str)
                return

if __name__ == "__main__":
    root = tk.Tk()
    app = GUI(root)


    root.mainloop()


