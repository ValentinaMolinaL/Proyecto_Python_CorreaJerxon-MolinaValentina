import json,os

with open("Index.json",encoding="utf-8") as file:
    Data=json.load(file)

Data[0]["Personas"][0]
IE=[];IC=[];T1=[];T2=[];T3=[]
for i in range(0,len(Data[1]["Personas"])):
    IE.append(Data[1]["Personas"][i]["Identificacion"])
IC.append(Data[3]["Personas"][0]["Identificacion"])
for i in range(0,len(Data[1]["Personas"])):
    if Data[1]["Personas"][i]["Grupo"]=="T1":
        T1.append(Data[1]["Personas"][i])
    elif Data[1]["Personas"][i]["Grupo"]=="T2":
        T2.append(Data[1]["Personas"][i])
    elif Data[1]["Personas"][i]["Grupo"]=="T3":
        T3.append(Data[1]["Personas"][i])

bol=True
while bol:
    os.system("cls")
    print("================================================\n1).Coordinacion.\n2).Trainer\n3).Estudiante\n4).Consulta de aprobacion.\n5).Salir\n================================================")
    Opcion=int(input("Ingrese un numero para ir a la opcion deseada.\n"))
    if Opcion==1:
        IdCor=int(input("Ingrese usuario de coordinador.\n"))
        if IdCor in IC:
            print("Usuario de coordinacion encontrado.")
            
        else:
            print("Este usuario no se encuenta registrado.")
            print("================================================\n1).Inscripción.\n2).Iniciar examen\n3).cambiar estado de estudiantes\n4).Asignar trainers y estudiantes a cada grupo \n5).ver rutas\n6).Salir\n================================================")

    elif Opcion==2:#15
        print("La mala pa zully")
    elif Opcion==3:
        IIden=int(input("Ingresa tu usuario.\n"))
        if IIden in IE:
            print("Usuario encontrado.")
            print("================================================\n1).Notas.\n2).Horas de estudio\n3).Trainer\n4).Estado\n5).Salon\n6).Salir\n================================================")
            Opcion=int(input("Ingrese un numero para ir a la opcion deseada.\n"))
            if Opcion==1:
                print("Notas")
            elif Opcion==2:
                print("Horas")
            elif Opcion==3:
                print("Trainer")
            elif Opcion==4:
                print("Estado")
            elif Opcion==5:
                print("Salon")
            elif Opcion==6:
                print("Salir")
        else:
            print("Este usuario no se encuentra registrado.")
            print(input("Presione Enter para continuar"))
    elif Opcion==4:
        print("La mala pa Jerxon")
    else:
        print("Adios <(;D")