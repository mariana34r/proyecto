import dato_treiner
import registro
import dato_ruta_traneirs


def registrar_trainers():
    trainers  = {}
    trainers["nombre"] = input("ingrese el nombre del trainer: ")
    trainers["apellido"] = input ("ingrese el apellido del trainer: ")
    trainers["Area_Entrenamiento"] = input ("Ingrese el area de entrenamineto valido")
    try:
        trainers["telefono"] = int(input("ingrese el telefono del trainer: "))
        trainers["documento"]=int(input("Ingrese su documento: "))
    except Exception:
        print("Ingrese un valor válido!")
        return
    
    dato_treiner.data.append(trainers)
    dato_treiner.guardar_datos()
 

def mostrar_trainers():
    print("Los Treiner registrados son:")
    for trainers in dato_treiner.data:
        print("Los Treins son:", trainers["nombre"], "/ apellido", trainers["apellido"], "/ documento:", trainers["documento"])
        

def horario_trainers():
    print("Bienevnido a Horarios")
    print("Asignele hoario al siguiente Trainer:")
    for trainers in dato_treiner.data:
        print("Trainer",trainers["nombre"])
        trainers["horario"]=input("Ingrese el horario del Trainer: ")
        
    dato_treiner.data.append(trainers)
    dato_treiner.guardar_datos()
    
def hoario_segun_trainers():
    print("Aqui esta tu horario busca tu nombre ")
    for trainers in dato_treiner.data:
        print("Trainer:",trainers["nombre"],"horario:",trainers["horario"])




        
def ruta_segun_trainer():
    print("Asignele una Ruta a cada Trainer")
    ruta={}
    for trainers in dato_treiner.data:
        print("Trainer",trainers["nombre"])
        print("Ruta disponibles son: \n1.Ruta NodeJS\n2.Ruta Java\n3.Ruta Netcore")
        opc_rut = input("Escriba una opcion ")
        if opc_rut == "Ruta NodeJS":
            ruta["Ruta NodeJS"]=input("")
            print("Agregado a Ruta NodeJs")
        elif opc_rut == "Ruta Java":
            ruta["Ruta java"]= input("")
            print("Agregado a Ruta Java")
        elif opc_rut == "Ruta NetCore":
            ruta["Ruta NetCore"] = input("")
            
        
    dato_ruta_traneirs.data.append(ruta)
    dato_ruta_traneirs.guardar_datos()       
        


