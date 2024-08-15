#Importamos Json
import json,os
import datetime

Fecha = str(datetime.datetime.now())

with open("Index.json",encoding="utf-8") as file:
    Data=json.load(file)
Inicio=False
bol=True
#Activamos un ciclo while
while bol:
    #Todos los estudiantes, profesores, coordinadores estan guardados en diferentes listas, esto lo usamos para ahorrar tiempo en las impresiones de datos de cada persona.
    IE=[];TE=[];IC=[];T1=[];T2=[];T3=[];PI=[];T123=[];Eli=[];PR=[];PrIn=[];IPI=[];IPELI=[];ICC=[]
    for i in range(0,len(Data[0]["Personas"])):
        PI.append(Data[0]["Personas"][i]) #PI=Personas inscritas
        IPI.append(Data[0]["Personas"][i]["Identificacion"])#IPI=Identificacion de personas inscritas
        if Data[0]["Personas"][i]["Estado"]=="ProcesoIngreso":#Personas inscritas que ya estan en proceso de ingreso, las personas en proceso de ingreso son todas aquellas que aprobaron el examen inicial
            PrIn.append(Data[0]["Personas"][i])
    for i in range(0,len(Data[1]["Personas"])):
        IE.append(Data[1]["Personas"][i]["Identificacion"])#IE=Identificacion de estudiantes
        TE.append(Data[1]["Personas"][i])#TE=Todos los estudiantes con todos sus datos
    for i in range(0,len(Data[4]["Personas"])):
        PR.append(Data[4]["Personas"][i])#PR=Profesores registrados en el sistema
    IC.append(Data[3]["Personas"][0]["Identificacion"])#IC=Identificacion del coordinador y contraseña del coordinador
    ICC.append(Data[3]["Personas"][0]["Contraseña"])
    for i in range(0,len(Data[2]["Personas"])):
        IPELI.append(Data[2]["Personas"][i]["Identificacion"])#IPELI=Identificacion de persona fuera del programa
        Eli.append(Data[2]["Personas"][i])#Eli=Todas las personas eliminadas
    for i in range(0,len(Data[1]["Personas"])):
        T123.append(Data[1]["Personas"][i])#T123=Todos los estudiantes
        if Data[1]["Personas"][i]["Grupo"]=="T1":
            T1.append(Data[1]["Personas"][i])#T1=Solo guarda los estudiantes que pertenecen a T1
        elif Data[1]["Personas"][i]["Grupo"]=="T2":
            T2.append(Data[1]["Personas"][i])#T2=Solo guarda los estudiantes que pertenecen a T2
        elif Data[1]["Personas"][i]["Grupo"]=="T3":
            T3.append(Data[1]["Personas"][i])#T3=Solo guarda los estudiantes que pertenecen a T3
    os.system("cls")
    #Menu principal
    print("================================================\n1).Coordinacion.\n2).Trainer\n3).Estudiante\n4).Consulta de aprobacion\n5).Iniciar sesión\n6).Cerrar sesión \n7).Salir\n================================================")
    Opcion=str(input("Ingrese un numero para ir a la opcion deseada.\n"))
    if Opcion=="1":
        intento=True
        while intento:
            try:
                IdCor=int(input("==============================\nIngrese usuario de coordinador\n==============================\n"))
                ConCor=int(input("==============================\nIngrese la contraseña del coordinador\n==============================\n"))
                intento=False
            except ValueError:
                print("Tienes que ingresar un numero entero para poder continuar D:")
        if IdCor in IC and ConCor in ICC:#Compara el usuario y la contraseña con los datos que haya en una lista respectiva para cada datos
            print("\n                   *******Bienvenido coordinador :D********")
            print(input("\nPresione Enter para continuar"))
            bol1=True
            while bol1:
                with open("Index.json",encoding="utf-8") as file:
                    Data=json.load(file)
                #Listas que guardan los mismos datos que las listas anteriores
                IE=[];TE=[];IC=[];T1=[];T2=[];T3=[];PI=[];T123=[];Eli=[];PR=[];PrIn=[];IPI=[];IPELI=[];ICC=[]
                for i in range(0,len(Data[0]["Personas"])):
                    PI.append(Data[0]["Personas"][i]) #PI=Personas inscritas
                    IPI.append(Data[0]["Personas"][i]["Identificacion"])#IPI=Identificacion de personas inscritas
                    if Data[0]["Personas"][i]["Estado"]=="ProcesoIngreso":#Personas inscritas que ya estan en proceso de ingreso, las personas en proceso de ingreso son todas aquellas que aprobaron el examen inicial
                        PrIn.append(Data[0]["Personas"][i])
                for i in range(0,len(Data[1]["Personas"])):
                    IE.append(Data[1]["Personas"][i]["Identificacion"])#IE=Identificacion de estudiantes
                    TE.append(Data[1]["Personas"][i])#TE=Todos los estudiantes con todos sus datos
                for i in range(0,len(Data[4]["Personas"])):
                    PR.append(Data[4]["Personas"][i])#PR=Profesores registrados en el sistema
                IC.append(Data[3]["Personas"][0]["Identificacion"])#IC=Identificacion del coordinador y contraseña del coordinador
                ICC.append(Data[3]["Personas"][0]["Contraseña"])
                for i in range(0,len(Data[2]["Personas"])):
                    IPELI.append(Data[2]["Personas"][i]["Identificacion"])#IPELI=Identificacion de persona fuera del programa
                    Eli.append(Data[2]["Personas"][i])#Eli=Todas las personas eliminadas
                for i in range(0,len(Data[1]["Personas"])):
                    T123.append(Data[1]["Personas"][i])#T123=Todos los estudiantes
                    if Data[1]["Personas"][i]["Grupo"]=="T1":
                        T1.append(Data[1]["Personas"][i])#T1=Solo guarda los estudiantes que pertenecen a T1
                    elif Data[1]["Personas"][i]["Grupo"]=="T2":
                        T2.append(Data[1]["Personas"][i])#T2=Solo guarda los estudiantes que pertenecen a T2
                    elif Data[1]["Personas"][i]["Grupo"]=="T3":
                        T3.append(Data[1]["Personas"][i])#T3=Solo guarda los estudiantes que pertenecen a T3
                for i in range(0,len(T123)):#Un ciclo que pasa por todos los estudiantes y cuando encuentre un estudiante que tenga el rendimiento en bajo entonces lo eliminara de curso
                    if Data[1]["Personas"][i]["Rendimiento"]=="Bajo":
                        Data[2]["Personas"].append({#Agrega un estudiante con rendimiento bajo en la lista de expulsados
                                "Identificacion": T123[i]["Identificacion"],
                                "Nombre": T123[i]["Nombre"],
                                "Apellido": T123[i]["Apellido"],
                                "Estado": "Bajo rendimiento"
                                })
                        Data[1]["Personas"].pop(i)#Elimina el estudiante de la lista de los que estan cursando
                        with open("index.json","w") as file:#Guarda los cambios
                            json.dump(Data,file)
                        break
                ITOTALES=IE+IPI+IPELI#La lista ITOTALES guarda todos los identificadores de todos los estudiantes, inscritos y expulsados
                os.system("cls")
                #Menu de coordinador
                print("================================================\n1).Inscribir.\n2).Ver Campers/Trainers/Inscritos.\n3).Ingresar notas.\n4).Destinar Trainers/Estudiantes.\n5).Expulsar camper\n6).Salir.\n================================================")
                Opcion=str(input("Ingrese un numero para ir a la opcion deseada.\n"))
                if Opcion=="1":
                    #Inscribir
                    os.system("cls")
                    intento=True
                    while intento:
                        try:
                            IdNew=int(input("Ingrese la identificacion. (Solo numeros)\n"))
                            if IdNew not in ITOTALES:#Compara la id nueva que se dio con las id dentro de la lista de todas las id, si la Id no se encuentra permite seguir con el proceso
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
                    #Crea la persona inscrita en la lista
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
                    #Guardar
                    with open("index.json","w") as file:
                        json.dump(Data,file)
                    print(input("Presione Enter para continuar"))
                elif Opcion=="2":
                    #Ver inscritos/campers/profesores/expulsados
                    os.system("cls")
                    Bol6=True
                    while Bol6:
                        os.system("cls")
                        #Menu ver
                        print("===========================================\n1).Ver inscritos\n2).Ver Camper\n3).Ver profesor\n4).Ver campers en rendimientos bajo.\n5).Expulsados\n6).Salir\n===========================================")
                        Opcion=str(input("Ingrese el numero de la opcion deseada.\n"))
                        if Opcion=="1":
                            #Ver inscritos
                            for i in range(0,len(PI)):
                                    print("=========Inscritos========")
                                    print("========================\nIdentificacion:",PI[i]["Identificacion"],"\nNombre:",PI[i]["Nombre"]+" "+PI[i]["Apellido"],"\nDireccion:",PI[i]["Direccion"],"\nAcudiente:",PI[i]["Acudiente"],"\nTelefono:",PI[i]["Fijo"],"\nCelular:",PI[i]["Celular"],"\nEstado:",PI[i]["Estado"])
                            print(input("Presione Enter para continuar"))
                        elif Opcion=="2":
                            #Ver campers
                            bol3=True
                            while bol3:
                                os.system("cls")
                                print("=========================================================================================================\n1).T1.\n2).T2.\n3).T3.\n4).Salir.\n=========================================================================================================")
                                Opcion=str(input("¿Que grupo de estudiantes deseas ver?\n"))
                                if Opcion=="1":
                                    #Ver grupo T1 de campers
                                    os.system("cls")
                                    for i in range(0,len(T1)):
                                        print("===========T1===========\nIdentificacion:",T1[i]["Identificacion"],"\nNombre:",T1[i]["Nombre"]+" "+T1[i]["Apellido"],"\nDireccion:",T1[i]["Direccion"],"\nAcudiente:",T1[i]["Acudiente"],"\nTelefono:",T1[i]["Fijo"],"\nCelular:",T1[i]["Celular"],"\nEstado:",T1[i]["Estado"],"\nTrainer:",T1[i]["Trainer"],"\nRuta:",T1[i]["Ruta"]["Nombre"],"\nHoras:",T1[i]["Horas"])
                                    print(input("Presione Enter para continuar"))
                                elif Opcion=="2":
                                    #Ver grupo T2 de campers
                                    os.system("cls")
                                    for i in range(0,len(T2)):
                                        print("===========T2===========\nIdentificacion:",T2[i]["Identificacion"],"\nNombre:",T2[i]["Nombre"]+" "+T2[i]["Apellido"],"\nDireccion:",T2[i]["Direccion"],"\nAcudiente:",T2[i]["Acudiente"],"\nTelefono:",T2[i]["Fijo"],"\nCelular:",T2[i]["Celular"],"\nEstado:",T2[i]["Estado"],"\nTrainer:",T2[i]["Trainer"],"\nRuta:",T2[i]["Ruta"]["Nombre"],"\nHoras:",T2[i]["Horas"])
                                    print(input("Presione Enter para continuar"))
                                elif Opcion=="3":
                                    #Ver grupo T3 de campers
                                    os.system("cls")
                                    for i in range(0,len(T3)):
                                        print("===========T3===========\nIdentificacion:",T3[i]["Identificacion"],"\nNombre:",T3[i]["Nombre"]+" "+T3[i]["Apellido"],"\nDireccion:",T3[i]["Direccion"],"\nAcudiente:",T3[i]["Acudiente"],"\nTelefono:",T3[i]["Fijo"],"\nCelular:",T3[i]["Celular"],"\nEstado:",T3[i]["Estado"],"\nTrainer:",T3[i]["Trainer"],"\nRuta:",T3[i]["Ruta"]["Nombre"],"\nHoras:",T3[i]["Horas"])
                                    print(input("Presione Enter para continuar"))
                                elif Opcion=="4":
                                    #Salir al menu principal de coordinacion
                                    print("Saliendo al menu anterior.")
                                    print(input("Presione Enter para continuar"))
                                    bol3=False
                                else:
                                    #Si no llega a estar una de las opciones posibles dara el mensaje 
                                    print("Ingrese un numero disponible entre las opciones :D")
                                    print(input("Presione Enter para continuar"))
                        elif Opcion=="3":
                            #Ver profesores
                            os.system("cls")
                            print("==================================================")
                            for i in range(0,len(PR)):
                                print("===========Profesor===========\nIdentificacion:",PR[i]["Identificacion"],"\nNombre:",PR[i]["Nombre"]+" "+PR[i]["Apellido"],"\nEstado:",PR[i]["Estado"],"\nGrupo:",PR[i]["Grupo"])
                            print(input("Presione Enter para continuar"))
                        elif Opcion=="4":
                            #Ver estudiantes con rendimiento bajo
                            #Revisar
                            os.system("cls")
                            for i in range (0,len(T123)):
                                if Data[1]["Personas"][i]["Rendimiento"] == "Bajo":
                                    print("===================================================\nIdentificacion:",T123[i]["Identificacion"],"\nNombre:",T123[i]["Nombre"]+" "+T123[i]["Apellido"],"\nRendimiento:",T123[i]["Rendimiento"],"\n===================================================")
                                else:
                                    print(input("No hay estudiantes con bajo rendimiento, presione Enter para continuar."))
                                    break
                        elif Opcion=="5":
                            #Ver personas expulsadas
                            os.system("cls")
                            for i in range(0,len(Data[2]["Personas"])):
                                print("====================Expulsado====================\nIdentificacion:",Data[2]["Personas"][i]["Identificacion"],"\nNombre:",Data[2]["Personas"][i]["Nombre"]+" "+Data[2]["Personas"][i]["Apellido"],"\nRazon:",Data[2]["Personas"][i]["Estado"])
                            print("====================Expulsado====================")
                            input("")
                        elif Opcion=="6":
                            #Salir al menu principal
                            print("=======================================\nSaliendo\n=======================================")
                            input("")
                            Bol6=False
                elif Opcion=="3":
                    #Agregar notas
                    os.system("cls")
                    Bol8=True
                    while Bol8:
                        os.system("cls")
                        #Menu
                        print("==================================\nNotas\n==================================\n1).Notas examen inicial.\n2).Notas filtro.\n3).Salir.\n==================================")
                        Opcion=str(input("Ingrese el numero de la opcion desesada.\n"))
                        if Opcion=="1":
                            #Agregar nota de examen inicial a personas inscritas
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
                                            Data[0]["Personas"][i]["Nota"]=NotaEx
                                            if Data[0]["Personas"][i]["Nota"]>59:
                                                Data[0]["Personas"][i]["Estado"]="ProcesoIngreso"
                                                Bol6=False
                                            else:
                                                Data[0]["Personas"][i]["Estado"]="Reprobado"
                                            with open("index.json","w") as file:
                                                json.dump(Data,file)
                                            print("=========================================================================================================")
                                            print("Nota ingresada con exito :D")
                                            print(input("Presione Enter para continuar"))
                                            Bol6=False
                                            break
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
                            #Agregar nota de examenes filtro a estudiantes dependiendo del grupo(T1,T2,T3)
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
                                            #Menu para ir a una nota de filtro
                                            print("=========================Notas======================================\n1).Filtro 1\n2).Filtro 2\n3).Filtro 3\n4).Filtro 4\n5).Filtro 5\n6).Salir\n===============================================================")
                                            Opcion=str(input("Ingrese un numero para ir a la opcion deseada.\n"))
                                            if Opcion=="1":
                                                #Filtro 1
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
                                                #Filtro 2
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
                                                #Filtro 3
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
                                                #Filtro 4
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
                                                #Filtro 5
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
                                                #Salir
                                                print(input("Presione Enter para continuar"))
                                                break
                                            else:
                                                print("Ingrese un numero disponible dentro del menu :D")
                                                input("")          
                                    else:
                                        if CompaId==1:
                                            #Salir del bucle
                                            print("=======================Saliendo=======================")
                                            input("")
                                            Bol7=False
                                            break
                                        if i==len(T123)-1:
                                            #Cuando el contador i valga la cantidad de objetos que hay en t123 dira que no se encontro ninguna persona con esa id en toda la lista
                                            print("No se encontro alguna persona por esa id.")
                                            print(input("Presione Enter para continuar"))
                                            Bol7=False
                                            break
                        elif Opcion=="3":
                            #Salir
                            print("===================\nSaliendo\n===================")
                            input("")
                            Bol8=False
                elif Opcion=="4":
                    #Agregar estudiantes o profesores a un grupo
                    os.system("cls")
                    bol5=True
                    while bol5:
                        #Menu 
                        print("=========================================================\n1).Agregar estudiantes a un grupo.\n2).Agregar profesor a un grupo.\n3).Agregar ruta a grupo.\n4).Salir.")
                        Opcion=str(input("Ingrese un numero para ir a la opcion deseada.\n"))
                        if Opcion=="1":
                            bol4=True
                            while bol4:
                                #Menu de grupos
                                print("======================================================\n1).T1\n2).T2\n3).T3\n4).Salir\n======================================================")
                                Opcion=str(input("Ingresa el numero del grupo al que deseas agregar el estudiante.\n"))
                                if Opcion=="1": # Agregar estudiantes a T1
                                    intento=True
                                    while intento:
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
                                                    # Se guardara con la estructura establecida
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
                                                        "Ruta":{
                                                            "Nombre":"",
                                                            "Formal":"",
                                                            "BaseD1":"",
                                                            "BaseD2":"",
                                                            "Backed":""
                                                        },
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
                                                        ],
                                                        "Sesion":"Inactiva",
                                                        "FechaEntrada": "-----",
                                                        "Actividad":"-----"
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
                                elif Opcion=="2": # Agregar estudiantes a T2
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
                                                        "Ruta":{
                                                            "Nombre":"",
                                                            "Formal":"",
                                                            "BaseD1":"",
                                                            "BaseD2":"",
                                                            "Backed":""
                                                        },
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
                                                        ],
                                                        "Sesion":"Inactiva",
                                                        "FechaEntrada": "-----",
                                                        "Actividad":"-----"
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
                                elif Opcion=="3": # Agregar estudiantes a T3
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
                                                        "Ruta":{
                                                            "Nombre":"",
                                                            "Formal":"",
                                                            "BaseD1":"",
                                                            "BaseD2":"",
                                                            "Backed":""
                                                        },
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
                                                        ],
                                                        "Sesion":"Inactiva",
                                                        "FechaEntrada": "-----",
                                                        "Actividad":"-----"
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
                        elif Opcion=="2": # destinar profesores a cada grupo 
                                intento=True
                                while intento:
                                    try:
                                        CompaId=int(input("Ingrese el ID del profesor que desea establecer al grupo\n"))
                                        intento=False
                                    except ValueError:
                                        print("ingresa el ID del trainer deben ser solo numeros.")
                                        input("")
                                bol9=True
                                while bol9:
                                    for i in range(0,len(PR)):
                                        if CompaId==PR[i]["Identificacion"]:
                                            NombreG=str(input("Ingrese el nombre del grupo al que deseas añadir al profesor\n"))
                                            for j in range(0,len(T123)):
                                                if Data[1]["Personas"][j]["Grupo"]==NombreG:
                                                    Data[1]["Personas"][j]["Trainer"]=PR[i]["Nombre"]
                                                    with open("index.json","w") as file:
                                                        json.dump(Data,file)
                                                        print("El profesor ha sido destinado correctamente.")
                                                        bol9=False
                                                        break
                                                else:
                                                    print("El nombre del grupo no coincide con algun grupo existente.")
                                                    input("")

                                            for i in range(0,len(PR)):
                                                if CompaId==PR[i]["Grupo"]=="T1":
                                                    Data[4]["Personas"][i]["Grupo"]=""
                                                if CompaId==PR[i]["Identificacion"]:
                                                    Data[4]["Personas"][i]["Grupo"]=NombreG
                                            
                                            with open("index.json","w") as file:
                                                        json.dump(Data,file)
                                        else:
                                            if i>len(PR)-1:
                                                print("Este ID de profesor no se encuentra en la base de datos")
                                                print(input("Presione Enter para continuar"))
                                                break
                        elif Opcion=="3": # Destinar o crear rutas a un grupo
                            print("====================Rutas====================\n1).Java.\n2).NodeJs.\n3).NetCore.\n4).Nueva ruta.\n5).Salir\n=============================================")
                            Opcion=str(input("Ingrese un numero para ir a la opcion deseada\n"))
                            if Opcion =="1":
                                NombreG=str(input("Ingrese el nombre del grupo al que deseas establecer la ruta(T1,T2,T3)\n"))
                                BaseD2=str(input("Ingrese el nombre del modulo de Datos alternativo\n"))
                                for i in range(0,len(T123)):
                                    if T123[i]["Grupo"]==NombreG:
                                        Data[1]["Personas"][i]["Ruta"]["Nombre"]="Java"
                                        Data[1]["Personas"][i]["Ruta"]["Formal"]="Java"
                                        Data[1]["Personas"][i]["Ruta"]["BaseD1"]="MySQl"
                                        Data[1]["Personas"][i]["Ruta"]["BaseD2"]=BaseD2
                                        Data[1]["Personas"][i]["Ruta"]["Backed"]="SpringBoot"
                                        with open("index.json","w") as file:
                                                    json.dump(Data,file)
                            elif Opcion=="2":
                                NombreG=str(input("Ingrese el nombre del grupo al que deseas establecer la ruta\n"))
                                BaseD2=str(input("Ingrese el nombre del modulo de Datos alternativo\n"))
                                for i in range(0,len(T123)):
                                    if T123[i]["Grupo"]==NombreG:
                                        Data[1]["Personas"][i]["Ruta"]["Nombre"]="NodeJs"
                                        Data[1]["Personas"][i]["Ruta"]["Formal"]="C#"
                                        Data[1]["Personas"][i]["Ruta"]["BaseD1"]="ProgresQL"
                                        Data[1]["Personas"][i]["Ruta"]["BaseD2"]=BaseD2
                                        Data[1]["Personas"][i]["Ruta"]["Backed"]="NodeJs"
                                        with open("index.json","w") as file:
                                                    json.dump(Data,file)
                            elif Opcion=="3":
                                NombreG=str(input("Ingrese el nombre del grupo al que deseas establecer la ruta\n"))
                                BaseD2=str(input("Ingrese el nombre del modulo de Datos alternativo\n"))
                                for i in range(0,len(T123)):
                                    if T123[i]["Grupo"]==NombreG:
                                        Data[1]["Personas"][i]["Ruta"]["Nombre"]="NetCore"
                                        Data[1]["Personas"][i]["Ruta"]["Formal"]="JavaScript"
                                        Data[1]["Personas"][i]["Ruta"]["BaseD1"]="MongoDB"
                                        Data[1]["Personas"][i]["Ruta"]["BaseD2"]=BaseD2
                                        Data[1]["Personas"][i]["Ruta"]["Backed"]="Netcore"
                                        with open("index.json","w") as file:
                                                    json.dump(Data,file)
                            elif Opcion=="4":
                                NombreG=str(input("Ingrese el nombre del grupo al que deseas establecer la ruta\n"))
                                NombreR=str(input("Ingrese el nombre de la nueva ruta que desea establecer al grupo\n"))
                                Formal=str(input("Ingrese el nombre del modulo formal\n"))
                                BaseD1=str(input("Ingrese el nombre del modulo de Datos principal\n"))
                                BaseD2=str(input("Ingrese el nombre del modulo de Datos alternativo\n"))
                                Backed=str(input("Ingrese el nombre del modulo de backed\n"))
                                for i in range(0,len(T123)):
                                    if T123[i]["Grupo"]==NombreG:
                                        Data[1]["Personas"][i]["Ruta"]["Nombre"]=NombreR
                                        Data[1]["Personas"][i]["Ruta"]["Formal"]=Formal
                                        Data[1]["Personas"][i]["Ruta"]["BaseD1"]=BaseD1
                                        Data[1]["Personas"][i]["Ruta"]["BaseD2"]=BaseD2
                                        Data[1]["Personas"][i]["Ruta"]["Backed"]=Backed
                                        with open("index.json","w") as file:
                                                    json.dump(Data,file)
                            elif Opcion=="5":
                                input("Presione Enter para continuar")
                            else:
                                print("Ingresa una opcion valida")
                                input("")
                        elif Opcion=="4":
                            print(input("Presione Enter para salir al menu"))
                            bol5=False
                        else:
                            print("Ingrese una opcion valida")
                            input("")
                elif Opcion=="5": # Expulsar camper
                    intento=True
                    while intento:
                        try:
                            CompaId=int(input("===================================================\nIngrese la ID del camper que desea sacar del proceso\n===================================================\n"))
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
            print("Usuario o contraseña erroneo.")
            print(input("Presione Enter para seguir al menu principal"))       
    elif Opcion=="2": # Ver estado y datos del trainer 
        bol2=True
        while bol2:
            intento=True
            while intento:
                try:
                    os.system("cls")
                    CompaId=int(input("=============================================================================\nIngrese su codigo para saber el estado del profesor.\n"))
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
    elif Opcion=="3": # Ver estado de camper
        bol2=True
        while bol2:
            intento=True
            while intento:
                try:
                    os.system("cls")
                    CompaId=int(input("=============================================================================\nIngrese su codigo para saber el estado del estudiante.\n"))
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
    elif Opcion=="4": # Ver si el inscrito aprobo el examen principal 
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
                if PI[i]["Nota"]>59:
                    print("Felicidades aprobaste, Espera que el coordinador academico active la siguiente fase para que seas parte de nuestro equipo estudiantil.")
                    break
                else:
                    if PI[i]["Nota"]==0:
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

    elif Opcion=="5":# Registrar la entrada de todos los camper que ingresan a la plataforma.
        os.system("cls")
        print("""============Hola Camper==================
              Para que el registro de tu entrada sea exitoso ingresa los siguientes datos""")
        IdSesion=int(input("Ingrese su ID.\n"))
        FechaSesión=str(datetime.datetime.now())
        print("Que actividad realizaras \n1).Clases. \n2).Labor Social. \n3).Asesorias.")
        OpcionSesión=str(input("Ingresa un numero para elegir la actividad: "))
        if OpcionSesión=="1":
            for i in Data[1]["Personas"]:
                if IdSesion == i["Identificacion"]:
                    i["Sesion"]="Activa"
                    i["FechaEntrada"]=FechaSesión
                    i["Actividad"]="Clase"
                    
                    with open("index.json","w") as file:
                        json.dump(Data,file)

        elif OpcionSesión=="2":
            for i in Data[1]["Personas"]:
                if IdSesion == i["Identificacion"]:
                    i["Sesion"]="Activa"
                    i["FechaEntrada"]=FechaSesión
                    i["Actividad"]="Labor Social"
                    
                    with open("index.json","w") as file:
                        json.dump(Data,file)
                        
        elif OpcionSesión=="3":
            for i in Data[1]["Personas"]:
                if IdSesion == i["Identificacion"]:
                    i["Sesion"]="Asesorias"
                    i["FechaEntrada"]=FechaSesión
                    i["Actividad"]="Clase"
                    
                    with open("index.json","w") as file:
                        json.dump(Data,file)

    elif Opcion=="6":
        os.system("cls")
        print("""============Hola Camper==================
              Para cerrar sesión ingresa los siguientes datos""")
        IdSesión=str(input("Ingrese su ID.\n"))
        for i in Data["Personas"]:
            if IdSesión == i["Identificacion"]:
                i["Sesion"]="Finalizada"
                i["FechaEntrada"] = "-----"
                i["Actividad"] = "-----"
                
                with open("Index.json","w") as file:
                    json.dump(Data,file)

    elif Opcion=="7":
        os.system("cls")
        print("=======================================\nAdios <(;D\n======================================")
        print("Presiona Enter para salir")
        bol=False
    else:
        print("Ingrese un numero valido para poder seguir con alguna de las opciones disponibles :D")
        print(input("Enter para continuar"))
#Hecho por Jerxon Correa CC.1004922559 y Valentina Molina CC.1007109135 