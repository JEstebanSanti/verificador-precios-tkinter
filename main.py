from tkinter import *
from searchByCodeBar import *

root = Tk()
#root.geometry("600x800")
root.state('zoomed')

root.title('Verificador De Precios');
Label(root, text="Verificar Precios").grid(row=0, column=3)
Label(root, text="Codigo").grid(row=1, column=3)

code = StringVar()
entryCode = Entry(root,  textvariable=code, borderwidth=1, width=60).grid(row=1, column=4)
root['background'] = '#fefae0'

def searchByCode():
    producto = sByCodeBar(code.get())
    renderProducto(producto)

def renderProducto(producto):
    
    if len(producto) > 2:
        Label(root, image=PhotoImage(file=producto[3]), width=300, height=300).grid(row=8, column=4)
        Label(root, text=producto[0]).grid(row=9, column=4)
        Label(root, text=producto[1]).grid(row=10, column=4)
        Label(root, text=producto[2]).grid(row=11, column=4)
    else:
        Label(root, text=producto).grid(row=11, column=7)



search = Button(root, text="Buscar", command=searchByCode).grid(row=5, column=4)
root.mainloop()

