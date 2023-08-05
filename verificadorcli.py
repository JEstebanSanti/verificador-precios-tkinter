from searchByCodeBar import sByCodeBar
codigo  = ""
while (codigo != "salir"):
    codigo = input("Introduce el codigo")
    if codigo == "salir": break
    producto = sByCodeBar(codigo)
    if producto == 0 : print("No exite El producto buscado")
    if producto == -1 : print("conexion perdida")
    else: print(producto)

