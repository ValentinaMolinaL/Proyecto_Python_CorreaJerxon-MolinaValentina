import json,os

with open("Index.json",encoding="utf-8") as file:
    Data=json.load(file)
Inicio=False
bol=True
while bol:
    Data[0]["Personas"][0]
    IE=[];TE=[];IC=[];T1=[];T2=[];T3=[];PI=[];T123=[];Eli=[];PR=[];PrIn=[]
    for i in range(0,len(Data[0]["Personas"])):
        PI.append(Data[0]["Personas"][i])
        if Data[0]["Personas"][i]["Estado"]=="ProcesoIngreso":
            PrIn.append(Data[0]["Personas"][i])
    for i in range(0,len(Data[1]["Personas"])):
        IE.append(Data[1]["Personas"][i]["Identificacion"])
        TE.append(Data[1]["Personas"][i])
    for i in range(0,len(Data[4]["Personas"])):
        PR.append(Data[4]["Personas"][i])
    IC.append(Data[3]["Personas"][0]["Identificacion"])

    for i in range(0,len(Data[2]["Personas"])):
        Eli.append(Data[2]["Personas"][i])
    for i in range(0,len(Data[1]["Personas"])):
        T123.append(Data[1]["Personas"][i])
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
                IE=[];TE;IC=[];T1=[];T2=[];T3=[];PI=[];T123=[];PR=[];PrIn=[]
                for i in range(0,len(Data[0]["Personas"])):
                    if Data[0]["Personas"][i]["Estado"]=="ProcesoIngreso":
                        PrIn.append(Data[0]["Personas"][i])
                    PI.append(Data[0]["Personas"][i])
                for i in range(0,len(Data[1]["Personas"])):
                    IE.append(Data[1]["Personas"][i]["Identificacion"])
                    TE.append(Data[1]["Personas"][i])
                for i in range(0,len(Data[4]["Personas"])):
                    PR.append(Data[4]["Personas"][i])

                IC.append(Data[3]["Personas"][0]["Identificacion"])
                for i in range(0,len(Data[2]["Personas"])):
                    Eli.append(Data[2]["Personas"][i])
                for i in range(0,len(Data[1]["Personas"])):
                    T123.append(Data[1]["Personas"][i])
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
                    os.system("cls")
                    FechaI=str(input("Ingrese la fecha de inicio del programa (DD-MM-AAAA)\n"))
                    FechaF=str(input("Ingrese la fecha final del programa (DD-MM-AAAA)\n"))
                    Data[5]["FechaI"]=FechaI
                    Data[5]["FechaF"]=FechaF
                    with open("index.json","w") as file:
                        json.dump(Data,file)
                    print("La fecha de inicio sera:",FechaI,"\nLa fecha de finalizacion sera:",FechaF)
                    print(input("Presione Enter para continuar"))
                elif Opcion==4:
                    if Data[5]["InicioE"]=="False":
                        Data[5]["InicioE"]="True"
                        print("Examenes iniciados con exito")
                        with open("index.json","w") as file:
                            json.dump(Data,file)
                    else:
                        print("Ya iniciaste los examenes")
                    print(input("Presione Enter para continuar"))
                elif Opcion==5:
                    if Data[5]["InicioE"]=="True":
                        CompaId=int(input("Ingrese el numero de identificacion del estudiante al que le deseas colocar la nota.\n"))
                        for i in range(0,len(PI)):
                            if CompaId == PI[i]["Identificacion"]:
                                NotaEx=int(input("Ingrese la nota que la persona obtuvo en el examen.\n"))
                                Data[0]["Personas"][i]["NotaI"]=NotaEx
                                if Data[0]["Personas"][i]["NotaI"]>59:
                                    Data[0]["Personas"][i]["Estado"]="ProcesoIngreso"
                                else:
                                    Data[0]["Personas"][i]["Estado"]="Reprobado"
                                with open("index.json","w") as file:
                                    json.dump(Data,file)
                                print(input("Presione Enter para continuar"))
                                break
                            else:
                                if i==len(PI)-1:
                                    print("No se encontro alguna persona por esa id.")
                                    print(input("Presione Enter para continuar"))            
                    else:
                        print("No se han iniciado los examenes por lo tanto no se puede añadir notas")
                        print(input("Presione Enter para continuar"))
                elif Opcion==7:
                    bol4=True
                    while bol4:
                        os.system("cls")
                        print("==================================================================================\n¿En que grupo esta la persona a la que deseas cambiar el estado\n1).Inscritos\n2).Cursando\n3).Retirados.\n4).Salir\n==========================================================================")
                        Opcion=int(input("Ingrese el numero de la opcion deseada."))
                        if Opcion==1:
                            CompaId=int(input("Ingrese la identificacion de la persona inscrita.\n"))
                            for i in range(0,len(PI)):
                                if CompaId == PI[i]["Identificacion"]:
                                    EstadoNew=str(input("Ingrese el nuevo estado de la persona inscrita."))
                                    Data[0]["Personas"][i]["Estado"]=EstadoNew
                                    print(input("Presione Enter para continuar"))
                                    break
                                else:
                                    if i==len(PI)-1:
                                        print("No se encontro alguna persona por esa id.")
                                        print(input("Presione Enter para continuar"))                       
                        elif Opcion==2:
                            print("Cursando")
                            CompaId=int(input("Ingrese la identificacion del estudiante.\n"))
                            for i in range(0,len(T123)):
                                if CompaId == T123[i]["Identificacion"]:
                                    EstadoNew=str(input("Ingrese el nuevo estado de la persona inscrita."))
                                    Data[1]["Personas"][i]["Estado"]=EstadoNew
                                    print(input("Presione Enter para continuar"))
                                    break
                                else:
                                    if i==len(T123)-1:
                                        print("No se encontro alguna persona por esa id.")
                                        print(input("Presione Enter para continuar")) 
                        elif Opcion==3:
                            print("Retirados")
                            CompaId=int(input("Ingrese la identificacion de la persona.\n"))
                            for i in range(0,len(Eli)):
                                if CompaId == Eli[i]["Identificacion"]:
                                    EstadoNew=str(input("Ingrese el nuevo estado de la persona inscrita."))
                                    Data[2]["Personas"][i]["Estado"]=EstadoNew
                                    print(input("Presione Enter para continuar"))
                                    break
                                else:
                                    if i==len(Eli)-1:
                                        print("No se encontro alguna persona por esa id.")
                                        print(input("Presione Enter para continuar")) 
                        elif Opcion==4:
                            bol4=False
                            with open("index.json","w") as file:
                                json.dump(Data,file)
                            print(input("Presione Enter para continuar"))
                elif Opcion==8:
                    bol5=True
                    while bol5:
                        print("=========================================================\n1).Agregar profesores a un grupo de estudiantes.\n2).Agregar estudiantes a un grupo.\n3).Salir")
                        Opcion=int(input("Ingrese un numero para ir a la opcion deseada.\n"))
                        if Opcion==1:
                            print("======================================================\n1).T1.\n2).T2\n3).T3\n4).Salir\n======================================================")
                            Opcion=int(input("Ingresa el numero del grupo al que deseas agregar el profesor.\n"))
                            CompaId=int(input("Ingrese la ID del profesor que quieres asignar a un grupo."))
                            if Opcion==1:
                                print("")
                            elif Opcion==2:
                                print("")
                            elif Opcion==3:
                                print("")
                            elif Opcion==4:
                                print("")
                        elif Opcion==2:
                            Grupo=str(input("Ingrese el nombre del grupo al que desea agregarlo. (T1,T2,T3)\n"))
                                #if Data:"
                                CompaId=int(input("Ingrese la identificacion de la persona.\n"))
                                for i in range(0,len(PI)):
                                    if CompaId == PI[i]["Identificacion"]:
                                        if PI[i]["Estado"] == "ProcesoIngreso":
                                            Data[1]["Personas"].append({
                                                "Grupo": Grupo,
                                                "Identificacion": PI[i]["Identificacion"],
                                                "Nombre": PI[i]["Nombre"],
                                                "Apellido": PI[i]["Apellido"],
                                                "Estado": "Cursando",
                                                "Direccion": PI[i]["Direccion"],
                                                "Acudiente": PI[i]["Acudiente"],
                                                "Celular": PI[i]["Celular"],
                                                "Fijo": PI[i]["Fijo"],
                                                "Trainer": "",
                                                "Horas": "",
                                                "Notas": [
                                                    {
                                                        "Filtro1": 0,
                                                        "Filtro2": 0,
                                                        "Filtro3": 0,
                                                        "Filtro4": 0,
                                                        "Filtro5": 0
                                                    }
                                                ]
                                            })
                                            print(input("Presione Enter para continuar"))
                                            Data[0]["Personas"].pop(i)
                                            with open("index.json","w") as file:
                                                json.dump(Data,file)
                                        else:
                                            print("La persona ha reprovado el examen te esperamos la proxima.")

                                    else:
                                        if i==len(PrIn)-1:                                            
                                            print("La persona no se encuntra registrada por esa id.")
                                            print(input("Presione Enter para continuar"))
                            else:
                                print("lo sentimos el salon ",Grupo,"esta en su limite de campers")
                            
                                bol5=False
                elif Opcion==9:
                    bol5:True
                    while bol5:
                        print("Cual de las 3 rutas deseas ver \n1).Ruta NodeJS \n2).Ruta Java \n3).Ruta NetCore \n4).salir")
                        Opcion=int(input("elige una ruta"))
                        if Opcion==1:
                            print("Ruta NodeJS")
                        elif Opcion==2:
                            print("Ruta Java")
                        elif Opcion==3:
                            print("Ruta NetCore")
                        elif Opcion==4:
                            print("Saliendo al menu de coordinacion.")
                            print(input("Presione Enter para continuar"))
                            bol5=False
                elif Opcion==10:
                    print("==================================================")
                    for i in range(0,len(PR)):
                        print("===========Estudiante===========\nIdentificacion:",PR[i]["Identificacion"],"\nNombre:",PR[i]["Nombre"]+" "+PR[i]["Apellido"],"\nEstado:",PR[i]["Estado"],"\nGrupo:",PR[i]["Grupo"])
                    print(input("Presione Enter para continuar"))
                elif Opcion==11:
                    for i in range (0,len(Data[1])):
                        if Data[1]["Personas"][i]["Rendimiento"] == "alto":
                            print("Identificacion:",T123[i]["Identificacion"],"\nNombre:",  T123[i]["Nombre"]+" "+T123[i]["Apellido"],"\nRendimiento:",T123[i]["Rendimiento"])
                        print(input("presione enter continuar"))
                elif Opcion==12:
                    bol3=True
                    while bol3:
                        os.system("cls")
                        print("1).T1.\n2).T2.\n3).T3.\n4).Salir.")
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
                        elif Opcion==4:
                            print("Saliendo al menu de coordinacion.")
                            print(input("Presione Enter para continuar"))
                            bol3=False
                elif Opcion==13:
                    print("Saliendo")
                    print(input("Presione Enter para continuar"))
                    bol1=False
                
        else:
            print("Este usuario no se encuenta registrado.")
            print(input("Presione Enter para seguir al menu principal"))
            
    elif Opcion==2:#15
        bol2=True
        while bol2:
            CompaId=int(input("Ingrese la identificacion de la persona.\n"))
            for i in range(0,len(PR)):
                if CompaId == PR[i]["Identificacion"]:
                    print("===========Estudiante===========\nIdentificacion:",PR[i]["Identificacion"],"\nNombre:",PR[i]["Nombre"]+" "+PR[i]["Apellido"],"\nEstado:",PR[i]["Estado"],"\nGrupo:",PR[i]["Grupo"])
                    print(input("Presione Enter para continuar"))
                    bol2=False
                    break
                else:
                    if i==len(PR)-1:
                        print("No se encontro alguna persona por esa id.")
                        print(input("Presione Enter para continuar"))
                        bol2=False
                    
    elif Opcion==3:
            bol2=True
            while bol2:
                CompaId=int(input("Ingrese la identificacion de la persona.\n"))
                for i in range(0,len(T123)):
                    if CompaId == T123[i]["Identificacion"]:
                        print("===========Estudiante===========\nIdentificacion:",T123[i]["Identificacion"],"\nNombre:",T123[i]["Nombre"]+" "+T123[i]["Apellido"],"\nEstado:",T123[i]["Estado"],"\nTrainer:",T123[i]["Trainer"])
                        print(input("Presione Enter para continuar"))
                        bol2=False
                        break
                    else:
                        if i==len(T123)-1:
                            print("No se encontro alguna persona por esa id.")
                            print(input("Presione Enter para continuar"))
                            bol2=False
                    
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
                    bol2=False
    else:
        print("Adios <(;D")
        print("Presiona Enter para salir")
        bol=False

#Hecho por Jerxon Correa CC.1004922559 y Valentina Molina CC.1007109135