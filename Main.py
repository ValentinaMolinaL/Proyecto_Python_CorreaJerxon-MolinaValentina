import json,os

with open("Index.json",encoding="utf-8") as file:
    Data=json.load(file)
Inicio=False
bol=True
while bol:
    Data[0]["Personas"][0]
    IE=[];TE=[];IC=[];T1=[];T2=[];T3=[];PI=[]
    for i in range(0,len(Data[0]["Personas"])):
        PI.append(Data[0]["Personas"][i])
    for i in range(0,len(Data[1]["Personas"])):
        IE.append(Data[1]["Personas"][i]["Identificacion"])
        TE.append(Data[1]["Personas"][i])

    IC.append(Data[3]["Personas"][0]["Identificacion"])

    for i in range(0,len(Data[1]["Personas"])):
        if Data[1]["Personas"][i]["Grupo"]=="T1":
            T1.append(Data[1]["Personas"][i])
        elif Data[1]["Personas"][i]["Grupo"]=="T2":
            T2.append(Data[1]["Personas"][i])
        elif Data[1]["Personas"][i]["Grupo"]=="T3":
            T3.append(Data[1]["Personas"][i])
    os.system("cls")
    print("================================================\n1).Coordinacion.\n2).Trainer\n3).Estudiante\n4).Consulta de aprobacion.\n5).Salir\n================================================")
    Opcion=int(input("Ingrese un numero para ir a la opcion deseada.\n"))
    if Opcion==1:
        IdCor=int(input("Ingrese usuario de coordinador.\n"))
        if IdCor in IC:
            print("Usuario de coordinacion encontrado.")
            bol1=True
            while bol1:
                with open("Index.json",encoding="utf-8") as file:
                    Data=json.load(file)
                Data[0]["Personas"][0]
                IE=[];TE;IC=[];T1=[];T2=[];T3=[];PI=[]
                for i in range(0,len(Data[0]["Personas"])):
                    PI.append(Data[0]["Personas"][i])
                for i in range(0,len(Data[1]["Personas"])):
                    IE.append(Data[1]["Personas"][i]["Identificacion"])
                    TE.append(Data[1]["Personas"][i])

                IC.append(Data[3]["Personas"][0]["Identificacion"])

                for i in range(0,len(Data[1]["Personas"])):
                    if Data[1]["Personas"][i]["Grupo"]=="T1":
                        T1.append(Data[1]["Personas"][i])
                    elif Data[1]["Personas"][i]["Grupo"]=="T2":
                        T2.append(Data[1]["Personas"][i])
                    elif Data[1]["Personas"][i]["Grupo"]=="T3":
                        T3.append(Data[1]["Personas"][i])
                os.system("cls")
                print("================================================\n1).Inscripción.\n2).Ver personas inscritas.\n3).Establecer fecha de inicio y finalizacion.\n4).Iniciar examen.\n5).Ingresar nota de examenes iniciales\n6).Establecer horarios.\n7).Cambiar estados de los estudiantes\n8).Destinar trainers y estudiantes a cada grupo.\n9).Ver rutas.\n10).Profesores registrados.\n11).Estudiantes en rendimiento bajo\n12).Ver campers.\n13).Salir.\n================================================")
                Opcion=int(input("Ingrese un numero para ir a la opcion deseada.\n"))
                if Opcion==1:
                    print("Inscripcion")
                    Cantidad=int(input("¿Cuantos estudiantes deseas registrar?\n"))
                    for i in range(0,Cantidad):
                        IdNew=int(input("Ingrese la identificacion.\n"))
                        NombreNew=str(input("Ingrese el nombre.\n"))
                        ApellidoNew=str(input("Ingrese apellido.\n"))
                        DireccionNew=str(input("Ingrese la direccion.\n"))
                        AcudienteNew=str(input("Ingrese el nombre del acudiente.\n"))
                        CelularNew=int(input("Ingrese el numero celular.\n"))
                        FijoNew=int(input("Ingrese un numero fijo.\n"))
                        Data[0]["Personas"].append({
                            "Grupo":"Inscrito",
                            "Identificacion":IdNew,
                            "Nombre":NombreNew,
                            "Apellido":ApellidoNew,
                            "Estado":"Inscrito",
                            "Direccion":DireccionNew,
                            "Acudiente":AcudienteNew,
                            "Celular":CelularNew,
                            "Fijo":FijoNew,
                            "Nota":0
                        })
                    with open("index.json","w") as file:
                        json.dump(Data,file)
                    print(input("Presione Enter para continuar"))

                elif Opcion==2:
                    for i in range(0,len(PI)):
                            print("=========Inscritos========")
                            print("========================\nIdentificacion:",PI[i]["Identificacion"],"\nNombre:",PI[i]["Nombre"]+" "+PI[i]["Apellido"],"\nDireccion:",PI[i]["Direccion"],"\nAcudiente:",PI[i]["Acudiente"],"\nTelefono:",PI[i]["Fijo"],"\nCelular:",PI[i]["Celular"],"\nEstado:",PI[i]["Estado"])
                    print(input("Presione Enter para continuar"))
                elif Opcion==3:
                    print("Fecha inicio curso")
                    print(input("Presione Enter para continuar"))
                elif Opcion==4:
                    print("Iniciar examen")
                    Inicio=True
                    print(input("Presione Enter para continuar"))
                elif Opcion==5:
                    if Inicio:
                        CompaId=int(input("Ingrese el numero de identificacion del estudiante al que le deseas colocar la nota.\n"))
                        for i in range(0,len(PI)):
                            if CompaId == PI[i]["Identificacion"]:
                                NotaEx=int(input("Ingrese la nota que el la persona obtuvo en el examen.\n"))
                                Data[0]["Personas"][i]["NotaI"]=NotaEx
                                if Data[0]["Personas"][i]["NotaI"]>59:
                                    Data[0]["Personas"][i]["Estado"]="Aprobado"
                                else:
                                    Data[0]["Personas"][i]["Estado"]="Reprobado"
                                with open("index.json","w") as file:
                                    json.dump(Data,file)
                                print(input("Presione Enter para continuar"))
                            else:
                                if i==len(PI)-1:
                                    print("No se encontro alguna persona por esa id.")
                                    print(input("Presione Enter para continuar"))
                                
                    else:
                        print("No se han iniciado los examenes por lo tanto no se puede añadir notas")
                        print(input("Presione Enter para continuar"))
                elif Opcion==12:
                    print("1).T1.\n2).T2.\n3).T3.")
                    Opcion=int(input("¿Que grupo de estudiantes deseas ver?\n"))
                    if Opcion==1:
                        for i in range(0,len(T1)):
                            print("===========T1===========\nIdentificacion:",T1[i]["Identificacion"],"\nNombre:",T1[i]["Nombre"]+" "+T1[i]["Apellido"],"\nDireccion:",T1[i]["Direccion"],"\nAcudiente:",T1[i]["Acudiente"],"\nTelefono:",T1[i]["Fijo"],"\nCelular:",T1[i]["Celular"],"\nEstado:",T1[i]["Estado"],"\nTrainer:",T1[i]["Trainer"])
                        print(input("Presione Enter para continuar"))
                    elif Opcion==2:
                        for i in range(0,len(T1)):
                            print("===========T2===========\nIdentificacion:",T2[i]["Identificacion"],"\nNombre:",T2[i]["Nombre"]+" "+T2[i]["Apellido"],"\nDireccion:",T2[i]["Direccion"],"\nAcudiente:",T2[i]["Acudiente"],"\nTelefono:",T2[i]["Fijo"],"\nCelular:",T2[i]["Celular"],"\nEstado:",T2[i]["Estado"],"\nTrainer:",T2[i]["Trainer"])
                        print(input("Presione Enter para continuar"))
                    elif Opcion==3:
                        for i in range(0,len(T1)):
                            print("===========T3===========\nIdentificacion:",T3[i]["Identificacion"],"\nNombre:",T3[i]["Nombre"]+" "+T3[i]["Apellido"],"\nDireccion:",T3[i]["Direccion"],"\nAcudiente:",T3[i]["Acudiente"],"\nTelefono:",T3[i]["Fijo"],"\nCelular:",T3[i]["Celular"],"\nEstado:",T3[i]["Estado"],"\nTrainer:",T3[i]["Trainer"])
                        print(input("Presione Enter para continuar"))
                elif Opcion==13:
                    print("Saliendo")
                    print(input("Presione Enter para continuar"))
                    bol1=False
                
        else:
            print("Este usuario no se encuenta registrado.")
            print(input("Presione Enter para seguir al menu principal"))
            
    elif Opcion==2:#15
        print("La mala pa zully")
    elif Opcion==3:
        IIden=int(input("Ingresa tu usuario.\n"))
        if IIden in IE:
            bol2=True
            while bol2:
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
        Consulta=int(input("Ingrese su codigo para saber el estado de aprobacion del estudiante.\n"))
        for i in range(0,len(PI)):
            if Consulta == PI[i]["Identificacion"]:
                print("Nombre:",PI[i]["Nombre"]+" "+PI[i]["Apellido"],"\nEstado:",PI[i]["Estado"])
                if PI[i]["NotaI"]>59:
                    print("Felicidades aprobaste, Espera que el coordinador academico active la siguiente fase para que seas parte de nuestro equipo estudiantil.")
                else:
                    if PI[i]["NotaI"]==0:
                        print("Revisa mas tarde, la nota aun no se a subido")
                        print(input("Presione Enter para continuar"))
                        break
                    else:
                        print("Lo sentimos, No alcanzaste la nota necesaria para aprobar el examen, te esperamos con los brazos abiertos a la siguiente oportunidad.")
                    print(input("Presione Enter para continuar"))
            else:
                if i==len(PI)-1:
                    print("No se encontro alguna persona por esa id.")
                    print(input("Presione Enter para continuar"))
    else:
        print("Adios <(;D")
        print("Presiona Enter para salir")
        bol=False

#Hecho por Jerxon Correa CC.1004922559 y Valentina Molina CC.1007109135