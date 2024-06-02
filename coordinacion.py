import registro
import treiner
import rutas_entrenamiento
import matricula
import campers_bajredi
import camper_graduados


def coordinador ():
    nombre=input("Ingrese su Nombre Coordinador: ")
    print("Binevenido", nombre )
    while True:
        print("")
        print("**Rol coordinacion**")
        print("*****Academica******")
        print("¿A que area de campus desea ingresar?")
        print("\n1.Campers\n2.Trainers\n3.Rutas de entrenamiento\n4.Reportes\n5.salir al menu principal")
        opc = 0
        print("")
        try:
            opc = int(input("Ingrese la opción deseada: "))
        except Exception:
            print("Valor incorrecto!!")
        if opc == 1:
            print("Has Ingresado a campers")
            print("\n1.Inscribir Campers Nuevos\n2.mostrar los campers registrados\n3.matriculas\n4.notas\n5.Editar Informacion\n6.Asignar ruta a los campers\n7.Mostrar Ruta de los campers\n8.salir")
            opc_dc=int(input("Ingrese una opcion"))
            if opc_dc== 1:
                registro.registrar_camper()
            elif opc_dc == 2:
                registro.mostrar_campers()
            elif opc_dc == 3:
                matricula.matricula_camper() 
            elif opc_dc== 4 :
                registro.notas_campers()
            elif opc_dc == 5:
                registro.cambiar_estado_camper() 
            elif opc_dc == 6 :
                registro.ruta_segun_camper()
            elif opc_dc == 8:
                break
        elif opc == 5:
            break
        elif opc == 2:
            print("Has Ingresado a Trainers")
            print("Que desea hacer")
            print("\n1.Crear Nuevo trainer\n2.Ver Trainer\n3.Asignar el Horario\n4.Asignarle su ruta al Trainers\n5.volver al menu principal")
            opc_dt=int(input("Ingrese una opcion"))
            if opc_dt==1:
                treiner.registrar_trainers()  
            elif opc_dt == 5:
                break    
            elif opc_dt == 2:
                treiner.mostrar_trainers()
            elif opc_dt== 3:
                treiner.horario_trainers()
            elif opc_dt == 4:
                treiner.ruta_segun_trainer()
        elif opc == 3:
            print("Bienvenido a rutas de entrenamiento")
            print("Que desea hacer ")
            print("\n1.Crear nueva Area de entrenamiento\n2.Mostrar Areas de entrenamiento\n4.volver al menu anterior")
            opc_r=int(input("Ingrese una opcion"))
            if opc_r == 1:
                rutas_entrenamiento.ruta_entreno()
            elif opc_r == 2:
                rutas_entrenamiento.mostrar_rutas()
            elif opc_r == 4:
                print("")
        elif opc == 4:
            print("Bienvenido a reportes")
            print("Que desea hacer ")
            print("\n1.Mostrar campers que estan Inscritos\n2.Campers que pasaron el examen inicial\n3. Entrenadores que se encuentran trabajando con CampusLands\n4. Campers que se encuentran con bajo rendimiento\n5.Campers y los trainer que se encuentren asociados a una ruta de entrenamiento\n6.Ingresar un nuevo camper graduado\n7.Mostrar campers graduados \n8.volver al menu anterior")
            opc_r=int(input("Ingrese una opcion"))
            if opc_r == 1:
                registro.mostrar_incritos()
            elif opc_r == 2 :
                matricula.mostrar_camper_admitidos() 
            elif opc_r ==3:
                treiner.mostrar_trainers()   
            elif opc_r == 8:
                print("")   
            elif opc_r == 4:
                print("Que desea Hacer:")
                print("\n1.Ingresar campers con bajo rendimiento\n2.Mostrar Campers con bajo rendimiento\n3.Expulsar campers por bajo rendimiento\n4.Mostrar campers expulsados\n5.salir")
                opc_cb= int(input("Ingrese una opcion"))
                if opc_cb == 1:
                    campers_bajredi.camper_bajo()
                elif opc_cb == 2:
                    campers_bajredi.mostrar_camper_bajo()
                elif opc_cb == 3:
                    campers_bajredi.expulsar_camper()
                elif opc_cb == 4:
                    campers_bajredi.mostrar_camper_expulsados()
            elif opc_r == 6:
                camper_graduados.campers_graduadoss()
            elif opc_r == 7:
                camper_graduados.mostrar_camper_graduados()
        else:
            print("La opción no es válida!")           
       
    
            
    
print(coordinador)
     