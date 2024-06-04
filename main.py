import coordinacion
import dato_camper
import treiner
print("")
print("**-------------------------**")
print("** Bienvenido a campusland **")
print("**-------------------------**")


def menu_principal():
    dato_camper.cargar_datos
    while True:
        print("")
        print("seleccione el cargo ")
        print("\n1.Coordinador\n2.Trainer\n3.salir")
        opc = 0
        print("")
        try:
            opc = int(input("Ingrese la opción deseada: "))
        except Exception:
            print("Valor incorrecto!!")            
        if opc == 1:
            coordinacion.coordinador()
        elif opc == 2:
            print("------------------------------")
            print("-         ROL TRAINER        -")
            print("------------------------------")
            print("Binevenidos Trainers")
            print("\n1.Ver Horario\n2.salir")
            opc_h=int(input("Ingrese una opcion"))
            if opc_h== 1:
                treiner.hoario_segun_trainers()
            elif opc_h==2:
                print(menu_principal)
        elif opc == 3:
            print("------------------------------")
            print("-        Usted ha salido     -")
            print("------------------------------")
            break
        else:
            print("La opción no es válida!")

menu_principal()
    