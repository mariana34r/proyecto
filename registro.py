import dato_camper
import treiner
import dato_ruta_campers

def registrar_camper():
    camper  = {}
    camper["nombre"] = input("ingrese el nombre del camper: ")
    camper["apellido"] = input ("ingrese el apellido del camper: ")
    camper["dirrecion"]=input("ingrese la direccion del camper: ")
    camper["acudiente"] = input("ingrese el nombre del acudiente del camper: ")
    camper["Estado"] = "Inscrito"
    try:
        camper["contacto"] = int(input("ingrese el telefono fijo del camper: "))
        camper["contacto2"] = int (input("Ingrese ahora el numero de telefono del celular"))
    except Exception:
        print("Ingrese un valor válido!")
        return
   
   
    dato_camper.data.append(camper)
    dato_camper.guardar_datos()
    
def mostrar_campers():
    print("Los Campers registrados son:")
    for camper in dato_camper.data:
        print("- Camper:", camper["nombre"], "/ apellido", camper["apellido"], "/ dirrecion", camper["dirrecion"] ,"/ Estado",camper["Estado"] )
       

def mostrar_incritos():
    print("Los Campers Inscritos son:")
    for camper in dato_camper.data:
        print("Los campers son:", camper["nombre"])    
        
def notas_campers():
    print("Ingrese la notas de los campers")
    for camper in dato_camper.data:
        print("Nota de: ",camper["nombre"]) 
        camper["notas"]=int (input(""))

def cambiar_estado_camper ():
    print("Segun las notas Cambiar estado a (Aprobado o Reprobado)y luego valla a la opcion y asignele una correspondiente ruta")
    for camper in dato_camper.data:
        print("Camper: ",camper["nombre"],camper["notas"],"Estado",camper["Estado"])
        camper["Estado"]=input("")
     
        

  
def ruta_segun_camper():
    print("Asignele una Ruta a cada Camper")
    ruta={}
    for camper in dato_camper.data:
        print("Camper: ",camper["nombre"])
        print("Ruta disponibles son: \n1.Ruta NodeJS\n2.Ruta Java\n3.Ruta Netcore")
        opc_ru = input("Escriba una opcion ")
        if opc_ru == "Ruta NodeJS":
            ruta["Ruta NodeJS"]=input("")
            print("Agregado a Ruta NodeJs")
        elif opc_ru == "Ruta Java":
            ruta["Ruta java"]= input("")
            print("Agregado a Ruta Java")
        elif opc_ru == "Ruta NetCore":
            ruta["Ruta NetCore"] = input("")
        
    
    dato_ruta_campers.data.append(ruta)
    dato_ruta_campers.guardar_datos()       
        

    