from conexion import *

def sByCodeBar(code):
    query = "SELECT codigo, nombre, precio, img FROM productos WHERE codigo='{}'".format(code)
    
   
    try:           
        cursor = db.cursor()
        cursor.execute(query)
        res = cursor.fetchone()
        if(len(res) >= 4):
            return res
        
    except:
        producto = ['No hay producto con el codigo '+code,'noimg.jpg']
        return producto
    

#for fila in res:

 #    producto= [{'codigo':fila[0], 'nombre':fila[1], 'precio':fila[2], 'imgan':fila[4]}]
