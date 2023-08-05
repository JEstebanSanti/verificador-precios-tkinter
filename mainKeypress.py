from tkinter import *
from searchByCodeBar import *
#from img import renderImg
import os
from PIL import ImageTk, Image

ventana = Tk()
ventana.geometry("500x500")
ventana.title('Verificador De Precios')

carpeta_principal = os.path.dirname(__file__)
carpeta_imagenes = os.path.join(carpeta_principal, "img")

Label(ventana, text="Verificar Precios").pack()
Label(ventana, text="Codigo").pack()
codigo = ''
entryCode = Entry(ventana, borderwidth=1, width=60)
entryCode.pack()
label_res = Label(ventana, text="Resultado")
label_res.pack(pady=10)
def key_pressed(event):
    global codigo
    if event.keysym=='Return':
        print(event.keysym)
        searchByCode(codigo)
        codigo = ''
    else:
        codigo+= event.keysym



def searchByCode(codigo):
    producto = sByCodeBar(codigo)
    if len(producto) == 4:
        pathImge = (os.path.join(carpeta_imagenes, producto[3]))
        #pathImgestr = str(pathImge)
        print(pathImge)
        image= Image.open(pathImge)
        #photoImg = ImageTk.PhotoImage(imgOpen)
        #labelImg = Label(root, image=photoImg)
        
        #image = Image.open("."+str(resultado[3]))
        #image = Image.open("./img/portatil_ultrafino.jpg")

        image = image.resize((200, 200))
        test = ImageTk.PhotoImage(image)
        label_imagen = Label(ventana, image=test, width=200, height=200)
        label_imagen.image = test
        #lbl_imagencita["image"] = test
        label_imagen.pack()
        searchByCode.label_imagen = label_imagen
        nombre = producto[1]
        precio = producto[2]
        y = (label_res.winfo_reqheight() + label_imagen.winfo_reqheight())
        label_imagen.place(x=150, y=y)
        searchByCode.label_imagen = label_imagen
        label_res.config(text=f"Nombre:{nombre} \n Precio:{precio}")

    else:
        print(producto)
        productoImgae = Image.open(os.path.join(carpeta_imagenes, str(producto[1]))).resize((350,360))
        Label(ventana, image=ImageTk.PhotoImage(productoImgae)).pack()
        Label(ventana, text=producto[0]).pack()


ventana.bind("<Key>",key_pressed)
ventana.resizable(False, False)
ventana.mainloop()

