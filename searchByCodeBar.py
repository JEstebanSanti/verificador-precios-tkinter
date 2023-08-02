from conexion import *

def sByCodeBar(code):
    query = "SELECT codigo, nombre, precio, img FROM productos WHERE codigo='{}'".format(code)
    
   
    try:           
        cursor = db.cursor()
        cursor.execute(query)
        res = cursor.fetchone()
        while res is not None:
            return res
        noRes = ["El producto {} se ha no encontrado"].format(code)
        return noRes  
    except:
        res = "Ocurrio un Error"
        return res
    

#for fila in res:

 #    producto= [{'codigo':fila[0], 'nombre':fila[1], 'precio':fila[2], 'imgan':fila[4]}]
