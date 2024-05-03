import json,os
with open("Index.json",encoding="utf-8") as file:
    Data=json.load(file)
Inicio=False
bol=True
while bol:
    IE=[];TE=[];IC=[];T1=[];T2=[];T3=[];PI=[];T123=[];Eli=[];PR=[];PrIn=[];IPI=[];IPELI=[]
    for i in range(0,len(Data[0]["Personas"])):
        PI.append(Data[0]["Personas"][i])
        IPI.append(Data[0]["Personas"][i]["Identificacion"])
        if Data[0]["Personas"][i]["Estado"]=="ProcesoIngreso":
            PrIn.append(Data[0]["Personas"][i])
    for i in range(0,len(Data[1]["Personas"])):
        IE.append(Data[1]["Personas"][i]["Identificacion"])
        TE.append(Data[1]["Personas"][i])
    for i in range(0,len(Data[4]["Personas"])):
        PR.append(Data[4]["Personas"][i])
    IC.append(Data[3]["Personas"][0]["Identificacion"])
    for i in range(0,len(Data[2]["Personas"])):
        IPELI.append(Data[2]["Personas"][i]["Identificacion"])
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
    Opcion=str(input("Ingrese un numero para ir a la opcion deseada.\n"))
    if Opcion=="1":
        intento=True
        while intento:
            try:
                IdCor=int(input("==============================\nIngrese usuario de coordinador\n==============================\n"))
                intento=False
            except ValueError:
                print("Tienes que ingresar un numero entero para poder continuar D:")
        if IdCor in IC:
            print("\n                   *******Bienvenido coordinador :D********")
            print(input("\nPresione Enter para continuar"))
            bol1=True
            while bol1:
                with open("Index.json",encoding="utf-8") as file:
                    Data=json.load(file)
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
                for i in range(0,len(T123)):
                    if Data[1]["Personas"][i]["Rendimiento"]=="Bajo":
                        Data[2]["Personas"].append({
                                "Identificacion": T123[i]["Identificacion"],
                                "Nombre": T123[i]["Nombre"],
                                "Apellido": T123[i]["Apellido"],
                                "Estado": "Bajo rendimiento"
                                })
                        Data[1]["Personas"].pop(i)
                        with open("index.json","w") as file:
                            json.dump(Data,file)
                        break
                ITOTALES=IE+IPI+IPELI
                os.system("cls")
                print("================================================\n1).Inscribir.\n2).Ver Campers/Trainers/Inscritos.\n3).Ingresar notas.\n4).Destinar Trainers/Estudiantes.\n5).Expulsar camper\n6).Salir.\n================================================")
                Opcion=str(input("Ingrese un numero para ir a la opcion deseada.\n"))
                if Opcion=="1":
                    os.system("cls")
                    intento=True
                    while intento:
                        try:
                            IdNew=int(input("Ingrese la identificacion. (Solo numeros)\n"))
                            if IdNew not in ITOTALES:
                                NombreNew=str(input("Ingrese el nombre.\n"))
                                ApellidoNew=str(input("Ingrese apellido.\n"))
                                DireccionNew=str(input("Ingrese la direccion.\n"))
                                AcudienteNew=str(input("Ingrese el nombre del acudiente.\n"))
                                CelularNew=int(input("Ingrese el numero celular.\n"))
                                FijoNew=int(input("Ingrese un numero fijo.\n"))
                                intento=False
                            else:
                                print("La ID que ingresaste esta ya existe, por favor ingresa una ID nueva")
                                input("")
                        except ValueError:
                            print("vuelve a ingresar los datos(por favor ingresalos como estan especificados.)")
                            print(input("Presione Enter para continuar"))
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
                elif Opcion=="2":
                    os.system("cls")
                    Bol6=True
                    while Bol6:
                        os.system("cls")
                        print("===========================================\n1).Ver inscritos\n2).Ver Camper\n3).Ver profesor\n4).Ver campers en rendimientos bajo.\n5).Expulsados\n6).Salir\n===========================================")
                        Opcion=str(input("Ingrese el numero de la opcion deseada.\n"))
                        if Opcion=="1":
                            for i in range(0,len(PI)):
                                    print("=========Inscritos========")
                                    print("========================\nIdentificacion:",PI[i]["Identificacion"],"\nNombre:",PI[i]["Nombre"]+" "+PI[i]["Apellido"],"\nDireccion:",PI[i]["Direccion"],"\nAcudiente:",PI[i]["Acudiente"],"\nTelefono:",PI[i]["Fijo"],"\nCelular:",PI[i]["Celular"],"\nEstado:",PI[i]["Estado"])
                            print(input("Presione Enter para continuar"))
                        elif Opcion=="2":
                            bol3=True
                            while bol3:
                                os.system("cls")
                                print("=========================================================================================================\n1).T1.\n2).T2.\n3).T3.\n4).Salir.\n=========================================================================================================")
                                Opcion=str(input("¿Que grupo de estudiantes deseas ver?\n"))
                                if Opcion=="1":
                                    os.system("cls")
                                    for i in range(0,len(T1)):
                                        print("===========T1===========\nIdentificacion:",T1[i]["Identificacion"],"\nNombre:",T1[i]["Nombre"]+" "+T1[i]["Apellido"],"\nDireccion:",T1[i]["Direccion"],"\nAcudiente:",T1[i]["Acudiente"],"\nTelefono:",T1[i]["Fijo"],"\nCelular:",T1[i]["Celular"],"\nEstado:",T1[i]["Estado"],"\nTrainer:",T1[i]["Trainer"],"\nRuta:",T1[i]["Ruta"],"\nHoras:",T1[i]["Horas"])
                                    print(input("Presione Enter para continuar"))
                                elif Opcion=="2":
                                    os.system("cls")
                                    for i in range(0,len(T2)):
                                        print("===========T2===========\nIdentificacion:",T2[i]["Identificacion"],"\nNombre:",T2[i]["Nombre"]+" "+T2[i]["Apellido"],"\nDireccion:",T2[i]["Direccion"],"\nAcudiente:",T2[i]["Acudiente"],"\nTelefono:",T2[i]["Fijo"],"\nCelular:",T2[i]["Celular"],"\nEstado:",T2[i]["Estado"],"\nTrainer:",T2[i]["Trainer"],"\nRuta:",T2[i]["Ruta"],"\nHoras:",T2[i]["Horas"])
                                    print(input("Presione Enter para continuar"))
                                elif Opcion=="3":
                                    os.system("cls")
                                    for i in range(0,len(T3)):
                                        print("===========T3===========\nIdentificacion:",T3[i]["Identificacion"],"\nNombre:",T3[i]["Nombre"]+" "+T3[i]["Apellido"],"\nDireccion:",T3[i]["Direccion"],"\nAcudiente:",T3[i]["Acudiente"],"\nTelefono:",T3[i]["Fijo"],"\nCelular:",T3[i]["Celular"],"\nEstado:",T3[i]["Estado"],"\nTrainer:",T3[i]["Trainer"],"\nRuta:",T3[i]["Ruta"],"\nHoras:",T3[i]["Horas"])
                                    print(input("Presione Enter para continuar"))
                                elif Opcion=="4":
                                    print("Saliendo al menu de coordinacion.")
                                    print(input("Presione Enter para continuar"))
                                    bol3=False
                                else:
                                    print("Ingrese un numero disponible entre las opciones :D")
                                    print(input("Presione Enter para continuar"))
                        elif Opcion=="3":
                            os.system("cls")
                            print("==================================================")
                            for i in range(0,len(PR)):
                                print("===========Profesor===========\nIdentificacion:",PR[i]["Identificacion"],"\nNombre:",PR[i]["Nombre"]+" "+PR[i]["Apellido"],"\nEstado:",PR[i]["Estado"],"\nGrupo:",PR[i]["Grupo"])
                            print(input("Presione Enter para continuar"))
                        elif Opcion=="4":
                            os.system("cls")
                            for i in range (0,len(T123)):
                                if Data[1]["Personas"][i]["Rendimiento"] == "Bajo":
                                    print("===================================================\nIdentificacion:",T123[i]["Identificacion"],"\nNombre:",T123[i]["Nombre"]+" "+T123[i]["Apellido"],"\nRendimiento:",T123[i]["Rendimiento"],"\n===================================================")
                                    print(input("presione enter continuar"))
                                    break
                                else:
                                    print(input("No hay estudiantes con bajo rendimiento, presione Enter para continuar."))
                                    break
                        elif Opcion=="5":
                            os.system("cls")
                            for i in range(0,len(Data[2]["Personas"])):
                                print("====================Expulsado====================\nIdentificacion:",Data[2]["Personas"][i]["Identificacion"],"\nNombre:",Data[2]["Personas"][i]["Nombre"]+" "+Data[2]["Personas"][i]["Apellido"],"\nRazon:",Data[2]["Personas"][i]["Estado"])
                            print("====================Expulsado====================")
                            input("")
                        elif Opcion=="6":
                            print("=======================================\nSaliendo\n=======================================")
                            input("")
                            Bol6=False
                elif Opcion=="3":
                    os.system("cls")
                    Bol8=True
                    while Bol8:
                        os.system("cls")
                        print("==================================\nNotas\n==================================\n1).Notas examen inicial.\n2).Notas filtro.\n3).Salir.\n==================================")
                        Opcion=str(input("Ingrese el numero de la opcion desesada.\n"))
                        if Opcion=="1":
                            Bol6=True
                            while Bol6:
                                os.system("cls")
                                if Data[5]["InicioE"]=="True":
                                    print("=========================================================================================================")
                                    intento=True
                                    while intento:
                                        os.system("cls")
                                        try:
                                            CompaId=int(input("Ingrese el numero de identificacion del estudiante al que le deseas colocar la nota.\n"))
                                            intento=False
                                        except ValueError:
                                            print("Debes ingresar un numero para continuar :D")
                                            input("")
                                    for i in range(0,len(PI)):
                                        if CompaId == PI[i]["Identificacion"]:
                                            intento=True
                                            while intento:
                                                try:
                                                    NotaEx=int(input("Ingrese la nota que la persona obtuvo en el examen.\n"))
                                                    intento=False
                                                except ValueError:
                                                    print("Debes ingresar un numero entero para poder continuar :D")
                                                    input("")  
                                            Data[0]["Personas"][i]["NotaI"]=NotaEx
                                            if Data[0]["Personas"][i]["NotaI"]>59:
                                                Data[0]["Personas"][i]["Estado"]="ProcesoIngreso"
                                            else:
                                                Data[0]["Personas"][i]["Estado"]="Reprobado"
                                            with open("index.json","w") as file:
                                                json.dump(Data,file)
                                            print("=========================================================================================================")
                                            print(input("Presione Enter para continuar"))
                                            Bol6=False
                                        else:
                                            if i==len(PI)-1:
                                                print("No se encontro alguna persona por esa id.")
                                                print("=========================================================================================================")
                                                print(input("Presione Enter para continuar"))
                                                Bol6=False       
                                else:
                                    print("=========================================================================================================")
                                    print("No se han iniciado los examenes por lo tanto no se puede añadir notas")
                                    print("=========================================================================================================")
                                    print(input("Presione Enter para continuar"))
                        elif Opcion=="2":
                            Bol7=True
                            while Bol7:
                                os.system("cls")
                                intento=True
                                while intento:
                                    os.system("cls")
                                    try:
                                        CompaId=int(input("Ingrese el codigo del estudiante a quien deseas actualizar la nota de un filtro o escribe 1 para salir\n"))
                                        intento=False
                                    except ValueError:
                                        print("Debes ingresar un numero para poder continuar.")
                                        input("")
                                for i in range(len(T123)):
                                    if CompaId==T123[i]["Identificacion"]:
                                        bol2=True
                                        while bol2:
                                            print("=========================Notas======================================\n1).Filtro 1\n2).Filtro 2\n3).Filtro 3\n4).Filtro 4\n5).Filtro 5\n6).Salir\n===============================================================")
                                            Opcion=str(input("Ingrese un numero para ir a la opcion deseada.\n"))
                                            if Opcion=="1":
                                                intento=True
                                                while intento:
                                                    os.system("cls")
                                                    try:
                                                        print("=====================================Filtro 1=====================================")
                                                        print("Por favor solo numeros para agregar las notas :D")
                                                        NotaT=float(input("Ingrese la nota del trabajo: "))
                                                        NotaE=float(input("Ingrese la nota del examen: "))
                                                        NotaP=float(input("Ingrese la nota de los trabajos del modulo: "))
                                                        intento=False
                                                    except ValueError:
                                                        print("Debes ingresar numeros para las notas, Por favor volverlo a intentar de la forma especificada.")
                                                        input("")
                                                NotaT=NotaT*0.6
                                                NotaE=NotaE*0.3
                                                NotaP=NotaP*0.1
                                                NotaN=NotaT+NotaE+NotaP
                                                if NotaN < 60:
                                                    Data[1]["Personas"][i]["Rendimiento"]="Bajo"
                                                else:
                                                    Data[1]["Personas"][i]["Rendimiento"]="Alto"
                                                Data[1]["Personas"][i]["Notas"][0]["Filtro1"]=NotaN
                                                with open("index.json","w") as file:
                                                    json.dump(Data,file)
                                            elif Opcion=="2":
                                                intento=True
                                                while intento:
                                                    os.system("cls")
                                                    try:
                                                        print("=====================================Filtro 2=====================================")
                                                        print("Por favor solo numeros para agregar las notas :D")
                                                        NotaT=float(input("Ingrese la nota del trabajo: "))
                                                        NotaE=float(input("Ingrese la nota del examen: "))
                                                        NotaP=float(input("Ingrese la nota de los trabajos del modulo: "))
                                                        intento=False
                                                    except ValueError:
                                                        print("Debes ingresar numeros para las notas, Por favor volverlo a intentar de la forma especificada.")
                                                        input("")
                                                NotaT=NotaT*0.6
                                                NotaE=NotaE*0.3
                                                NotaP=NotaP*0.1
                                                NotaN=NotaT+NotaE+NotaP
                                                if NotaN < 60:
                                                    Data[1]["Personas"][i]["Rendimiento"]="Bajo"
                                                else:
                                                    Data[1]["Personas"][i]["Rendimiento"]="Alto"
                                                Data[1]["Personas"][i]["Notas"][0]["Filtro2"]=NotaN
                                                with open("index.json","w") as file:
                                                    json.dump(Data,file)
                                            elif Opcion=="3":
                                                intento=True
                                                while intento:
                                                    os.system("cls")
                                                    try:
                                                        print("=====================================Filtro 3=====================================")
                                                        print("Por favor solo numeros para agregar las notas :D")
                                                        NotaT=float(input("Ingrese la nota del trabajo: "))
                                                        NotaE=float(input("Ingrese la nota del examen: "))
                                                        NotaP=float(input("Ingrese la nota de los trabajos del modulo: "))
                                                        intento=False
                                                    except ValueError:
                                                        print("Debes ingresar numeros para las notas, Por favor volverlo a intentar de la forma especificada.")
                                                        input("")
                                                NotaT=NotaT*0.6
                                                NotaE=NotaE*0.3
                                                NotaP=NotaP*0.1
                                                NotaN=NotaT+NotaE+NotaP
                                                if NotaN < 60:
                                                    Data[1]["Personas"][i]["Rendimiento"]="Bajo"
                                                else:
                                                    Data[1]["Personas"][i]["Rendimiento"]="Alto"
                                                Data[1]["Personas"][i]["Notas"][0]["Filtro3"]=NotaN
                                                with open("index.json","w") as file:
                                                    json.dump(Data,file)
                                            elif Opcion=="4":
                                                intento=True
                                                while intento:
                                                    os.system("cls")
                                                    try:
                                                        print("=====================================Filtro 4=====================================")
                                                        print("Por favor solo numeros para agregar las notas :D")
                                                        NotaT=float(input("Ingrese la nota del trabajo: "))
                                                        NotaE=float(input("Ingrese la nota del examen: "))
                                                        NotaP=float(input("Ingrese la nota de los trabajos del modulo: "))
                                                        intento=False
                                                    except ValueError:
                                                        print("Debes ingresar numeros para las notas, Por favor volverlo a intentar de la forma especificada.")
                                                        input("")
                                                NotaT=NotaT*0.6
                                                NotaE=NotaE*0.3
                                                NotaP=NotaP*0.1
                                                NotaN=NotaT+NotaE+NotaP
                                                if NotaN < 60:
                                                    Data[1]["Personas"][i]["Rendimiento"]="Bajo"
                                                else:
                                                    Data[1]["Personas"][i]["Rendimiento"]="Alto"
                                                Data[1]["Personas"][i]["Notas"][0]["Filtro4"]=NotaN
                                                with open("index.json","w") as file:
                                                    json.dump(Data,file)
                                            elif Opcion=="5":
                                                intento=True
                                                while intento:
                                                    os.system("cls")
                                                    try:
                                                        print("=====================================Filtro 5=====================================")
                                                        print("Por favor solo numeros para agregar las notas :D")
                                                        NotaT=float(input("Ingrese la nota del trabajo: "))
                                                        NotaE=float(input("Ingrese la nota del examen: "))
                                                        NotaP=float(input("Ingrese la nota de los trabajos del modulo: "))
                                                        intento=False
                                                    except ValueError:
                                                        print("Debes ingresar numeros para las notas, Por favor volverlo a intentar de la forma especificada.")
                                                        input("")
                                                NotaT=NotaT*0.6
                                                NotaE=NotaE*0.3
                                                NotaP=NotaP*0.1
                                                NotaN=NotaT+NotaE+NotaP
                                                if NotaN < 60:
                                                    Data[1]["Personas"][i]["Rendimiento"]="Bajo"
                                                else:
                                                    Data[1]["Personas"][i]["Rendimiento"]="Alto"
                                                Data[1]["Personas"][i]["Notas"][0]["Filtro5"]=NotaN
                                                with open("index.json","w") as file:
                                                    json.dump(Data,file)
                                            elif Opcion=="6":
                                                print(input("Presione Enter para continuar"))
                                                break
                                            else:
                                                print("Ingrese un numero disponible dentro del menu :D")
                                                input("")          
                                    else:
                                        if CompaId==1:
                                            print("=======================Saliendo=======================")
                                            input("")
                                            Bol7=False
                                            break
                                        if i==len(T123)-1:
                                            print("No se encontro alguna persona por esa id.")
                                            print(input("Presione Enter para continuar"))
                                            Bol7=False
                                            break
                        elif Opcion=="3":
                            print("===================\nSaliendo\n===================")
                            input("")
                            Bol8=False
                elif Opcion=="4":
                    os.system("cls")
                    bol5=True
                    while bol5:
                        print("=========================================================\n1).Agregar estudiantes a un grupo.\n2).Agregar profesor a un grupo.\n3).Salir")
                        Opcion=str(input("Ingrese un numero para ir a la opcion deseada.\n"))
                        if Opcion=="1":
                            bol4=True
                            while bol4:
                                print("======================================================\n1).T1.(Ruta NodeJs).\n2).T2.(Ruta Java)\n3).T3.(NetCore)\n4).Salir\n======================================================")
                                Opcion=str(input("Ingresa el numero del grupo al que deseas agregar el estudiante.\n"))
                                if Opcion=="1":
                                    intento=True
                                    try:
                                        CompaId=int(input("Ingrese la identificacion del estudiante que quieres agregar al grupo T1.\n"))
                                        intento=False
                                    except:
                                        print("Ingrese un numero para poder continuar :D")
                                        input("")
                                    for i in range(0,len(PI)):
                                        if CompaId == PI[i]["Identificacion"]:
                                            if len(T1)<34:
                                                if PI[i]["Estado"] == "ProcesoIngreso":
                                                    Data[1]["Personas"].append({
                                                        "Grupo": "T1",
                                                        "Identificacion": PI[i]["Identificacion"],
                                                        "Nombre": PI[i]["Nombre"],
                                                        "Apellido": PI[i]["Apellido"],
                                                        "Estado": "Cursando",
                                                        "Direccion": PI[i]["Direccion"],
                                                        "Acudiente": PI[i]["Acudiente"],
                                                        "Celular": PI[i]["Celular"],
                                                        "Fijo": PI[i]["Fijo"],
                                                        "Trainer": "",
                                                        "Ruta":"NodeJS",
                                                        "Horas": "08:00 A.M - 12:00 P.M",
                                                        "Rendimiento": "",
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
                                                    print("La persona ha reprobado o no se a subido la nota del examen.")
                                            else:
                                                print("El grupo se encuentra lleno.")
                                                input("")
                                        else:
                                            if i==len(PI)-1:                                            
                                                print("La persona no se encuntra registrada por esa id.")
                                                print(input("Presione Enter para continuar"))
                                elif Opcion=="2":
                                    intento=True
                                    while intento:
                                        try:
                                            CompaId=int(input("Ingrese la identificacion del estudiante que quieres agregar al grupo T2.\n"))
                                            intento=False
                                        except ValueError:
                                            print("Debes ingresar un numero para poder continuar.")
                                            input("")
                                    for i in range(0,len(PI)):
                                        if CompaId == PI[i]["Identificacion"]:
                                            if len(T2) <34:
                                                if PI[i]["Estado"] == "ProcesoIngreso":
                                                    Data[1]["Personas"].append({
                                                        "Grupo": "T2",
                                                        "Identificacion": PI[i]["Identificacion"],
                                                        "Nombre": PI[i]["Nombre"],
                                                        "Apellido": PI[i]["Apellido"],
                                                        "Estado": "Cursando",
                                                        "Direccion": PI[i]["Direccion"],
                                                        "Acudiente": PI[i]["Acudiente"],
                                                        "Celular": PI[i]["Celular"],
                                                        "Fijo": PI[i]["Fijo"],
                                                        "Trainer": "",
                                                        "Ruta":"Java",
                                                        "Horas": "02:00 P.M - 06:00 P.M",
                                                        "Rendimiento": "",
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
                                                    print("La persona ha reprobado o no se a subido la nota del examen.")
                                            else:
                                                print("Este grupo se encuentra lleno")
                                                input("")
                                        else:
                                            if i==len(PrIn)-1:                                            
                                                print("La persona no se encuntra registrada por esa id.")
                                                print(input("Presione Enter para continuar"))
                                elif Opcion=="3":
                                    intento=True
                                    while intento:
                                        try:
                                            CompaId=int(input("Ingrese la identificacion del estudiante que quieres agregar al grupo T3.\n"))
                                            intento=False
                                        except ValueError:
                                            print("Debes ingresar un numero para poder continuar.")
                                            input("")
                                    for i in range(0,len(PI)):
                                        if CompaId == PI[i]["Identificacion"]:
                                            if len(T3) <33:
                                                if PI[i]["Estado"] == "ProcesoIngreso":
                                                    Data[1]["Personas"].append({
                                                        "Grupo": "T3",
                                                        "Identificacion": PI[i]["Identificacion"],
                                                        "Nombre": PI[i]["Nombre"],
                                                        "Apellido": PI[i]["Apellido"],
                                                        "Estado": "Cursando",
                                                        "Direccion": PI[i]["Direccion"],
                                                        "Acudiente": PI[i]["Acudiente"],
                                                        "Celular": PI[i]["Celular"],
                                                        "Fijo": PI[i]["Fijo"],
                                                        "Trainer": "",
                                                        "Ruta":"NetCore",
                                                        "Horas": "06:00 P.M - 10:00 P.M",
                                                        "Rendimiento": "",
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
                                                    print("La persona ha reprobado o no se a subido la nota del examen.")
                                            else:
                                                print("Este grupo se encuentra lleno")
                                                input("")
                                        else:
                                            if i==len(PrIn)-1:                                            
                                                print("La persona no se encuntra registrada por esa id.")
                                                print(input("Presione Enter para continuar"))
                                elif Opcion=="4":
                                    print(input("Presione Enter para ir al menu anterior"))
                                    bol4=False
                                else:
                                    print("Ingresa un numero que este entre las opciones del menu.")
                                    input("")
                        elif Opcion=="2": 
                                intento=True
                                while intento:
                                    try:
                                        CompaId=int(input("Ingrese el ID del profesor que desea establecer al grupo\n"))
                                        intento=False
                                    except ValueError:
                                        print("ingresa el ID del trainer deben ser solo numeros.")
                                        input("")
                                for i in range(0,len(PR)):
                                    if CompaId==PR[i]["Identificacion"]:
                                        NombreP=str(input("Ingrese el nombre del profesor que desea añadir al grupo\n"))
                                        NombreG=str(input("Ingrese el nombre del grupo al que deseas añadir al profesor\n"))
                                        for i in range(0,len(T123)):
                                            if Data[1]["Personas"][i]["Grupo"]==NombreG:
                                                Data[1]["Personas"][i]["Trainer"]=NombreP
                                                with open("index.json","w") as file:
                                                    json.dump(Data,file)
                                        for i in range(0,len(PR)):
                                            if Data[4]["Personas"][i]["Grupo"]==NombreG:
                                                with open("index.json","w") as file:
                                                    json.dump(Data,file)
                                    else:
                                        print("Este ID de profesor no se encuentra en la base de datos")
                                        print(input("Presione Enter para continuar"))
                        elif Opcion=="3":
                            print(input("Presione Enter para salir al menu"))
                            bol5=False    
                elif Opcion=="5":
                    intento=True
                    while intento:
                        try:
                            CompaId=int(input("===================================================\nIngrese la ID del camper que desea sacar del proceso\n==================================================="))
                            intento=False
                        except:
                            print("Debes ingresar un numero entero para poder continuar")
                            input("")
                    for i in range(0,len(T123)):
                        if CompaId==T123[i]["Identificacion"]:
                            Razon=str(input("Escribre la razon de la expulsion: "))
                            Data[2]["Personas"].append({
                                "Identificacion": T123[i]["Identificacion"],
                                "Nombre": T123[i]["Nombre"],
                                "Apellido": T123[i]["Apellido"],
                                "Estado": Razon
                                })
                            Data[1]["Personas"].pop(i)
                            with open("index.json","w") as file:
                                json.dump(Data,file)
                            print(input("Presione Enter para continuar"))
                            break
                        else:
                            if i>len(T123)-1:
                                print("No se encuentra ningun estudiante en la lista")
                                print(input("Presione Enter para continuar"))
                                break
                elif Opcion=="6":
                    print("Saliendo")
                    print(input("Presione Enter para continuar"))
                    bol1=False
                else:
                    print("Ingrese un numero disponible entre las opciones :D")
                    print(input("Presione Enter para continuar"))           
        else:
            print("Este usuario no se encuenta registrado.")
            print(input("Presione Enter para seguir al menu principal"))       
    elif Opcion=="2":
        bol2=True
        while bol2:
            intento=True
            while intento:
                try:
                    os.system("cls")
                    CompaId=int(input("=============================================================================\nIngrese su codigo para saber el estado de aprobacion del aspirante.\n"))
                    intento=False
                except ValueError:
                    print("Tienes que ingresar un numero entero para poder continuar :D")
                    print(input("Presione Enter para continuar"))
            for i in range(0,len(PR)):
                if CompaId == PR[i]["Identificacion"]:
                    print("===========Trainer===========\nIdentificacion:",PR[i]["Identificacion"],"\nNombre:",PR[i]["Nombre"]+" "+PR[i]["Apellido"],"\nEstado:",PR[i]["Estado"],"\nGrupo:",PR[i]["Grupo"])
                    print(input("Presione Enter para continuar"))
                    bol2=False
                    break
                else:
                    if i==len(PR)-1:
                        print("No se encontro alguna persona por esa id.")
                        print(input("Presione Enter para continuar"))
                        bol2=False                
    elif Opcion=="3":
        bol2=True
        while bol2:
            intento=True
            while intento:
                try:
                    os.system("cls")
                    CompaId=int(input("=============================================================================\nIngrese su codigo para saber el estado de aprobacion del aspirante.\n"))
                    intento=False
                except ValueError:
                    print("Tienes que ingresar un numero entero para poder continuar :D")
                    print(input("Presione Enter para continuar"))
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
    elif Opcion=="4":
        intento=True
        while intento:
            try:
                os.system("cls")
                Consulta=int(input("=============================================================================\nIngrese su codigo para saber el estado de aprobacion del aspirante.\n"))
                intento=False
            except ValueError:
                print("Tienes que ingresar un numero entero para poder continuar :D")
                print(input("Presione Enter para continuar"))
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
                        break
            else:
                if i==len(PI)-1:
                    print("No se encontro alguna persona por esa id.")
                    print(input("Presione Enter para continuar"))
                    bol2=False
    elif Opcion=="5":
        os.system("cls")
        print("=======================================\nAdios <(;D\n======================================")
        print("Presiona Enter para salir")
        bol=False
    else:
        print("Ingrese un numero valido para poder seguir con alguna de las opciones disponibles :D")
        print(input("Enter para continuar"))
#Hecho por Jerxon Correa CC.1004922559 y Valentina Molina CC.1007109135 