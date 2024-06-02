import dato_bajo_rendimiento
import datos_expulsados

def camper_bajo ():
    bajo={}
    bajo["nombre"]=input("Ingrese el camepr con bajo rendimineto")
    
    dato_bajo_rendimiento.data.append(bajo)
    dato_bajo_rendimiento.guardar_datos()

def mostrar_camper_bajo():
    print("Los campers con bajo rendimineto son:")
    for bajo in dato_bajo_rendimiento.data:
        print("Los campers son:", bajo["nombre"])
        
def expulsar_camper():
    expulsado={}
    for bajo in dato_bajo_rendimiento.data:
        print("Desea Expulsar a este camper: " , bajo["nombre"] , "por su bajo rendimineto (si o no) ")
        opc_e=input("")
        if opc_e == "si" :
            expulsado["nombre"] = input("Ingrese el nombre del expulsado para guardarlo en expulsados")
        if opc_e == "no":
            print ("Queda condicional")
        
    datos_expulsados.data.append(expulsado)
    datos_expulsados.guardar_datos()
    
def mostrar_camper_expulsados ():
    print("Los camper expulsados son: ")
    for expulsado in datos_expulsados.data:
        print("Los campers son: ", expulsado["nombre"])
    