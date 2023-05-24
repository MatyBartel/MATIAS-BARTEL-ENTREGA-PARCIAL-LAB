
from functions import *
import os

while True:
    os.system("cls")
    match(menu()):
        case 1:
            try:
                lista_diccionario =  csv_list_dic(nombre_archivo=input("-Ingrese direccion del archivo a usar 'carpeta//ejemplo.csv' :"))      # Parcial//insumos.csv
            except FileNotFoundError:
                print("ERROR: El archivo que ingreso no existe, ingrese la direccion correctamente.")
            os.system("cls")
        case 2:
            try: 
                contador_lista_dic = contar_en_lista_dic(lista_diccionario,"marca")
            except NameError:
                print("ERROR: Primero debe cargar los datos del archivo (OPCION 1)")
            os.system("cls")
        case 3:            
            try: 
                diccionario_filtrado=mostrar_tres_claves(lista_diccionario,"marca","nombre","precio")
            except NameError:
                print("ERROR: Primero debe cargar los datos del archivo (OPCION 1)")
            os.system("cls")
        case 4:
            try: 
                lista_filtrada=buscar_por_caracteristica(lista_diccionario,caracteristica_ingresada=input("Ingrese caracteristica:"))
            except NameError:
                print("ERROR: Primero debe cargar los datos del archivo (OPCION 1)")
            os.system("cls")
        case 5:
            try: 
                lista_ordenada = ordenar_lista(lista_diccionario,"marca","precio")
            except NameError:
                print("ERROR: Primero debe cargar los datos del archivo (OPCION 1)")
            os.system("cls")
        case 6:
            try: 
                carrito = comprar(lista_diccionario,caracteristica_ingresada=input("Ingrese marca :"))
                archivo_texto = generar_archivo_txt(carrito,"carrito.txt")
            except NameError:
                print("ERROR: Primero debe cargar los datos del archivo (OPCION 1)")
            os.system("cls")
        case 7:
            try:
                guardar_JSON(lista_diccionario,"./lista_filtrada.json")
                print("ARCHIVO GUARDADO CON EXITO")
            except NameError:
                print("ERROR: Primero debe cargar los datos del archivo (OPCION 1,6)")
            os.system("cls")

        case 8:
            try:
                lista_filtrada=leer_JSON("./lista_filtrada.json")
                print(lista_filtrada)
            except FileNotFoundError:
                print("EL ARCHIVO NO SE GENERO TODAVIA (punto 7)")
            os.system("cls")
        case 9:
            try:
                diccionario = lista_diccionario
                resultado=list(map(aumentar_precio,diccionario))
                lista_aumentada = aumentar_precio(diccionario)
                guardar_csv(lista_aumentada,"./aumentos.csv")
            except NameError:
                print("ERROR: Primero debe cargar los datos del archivo (OPCION 1)")
            os.system("cls")
        case 10:
            seguir_salir()

#---------------------------------- EXTRAS ------------------------------------------- 

        case 11:
            try:
                lista_con_agregados=agregar_producto(lista_diccionario)
                mostrar_diccionarios(lista_con_agregados)
                
            except NameError:
                print("ERROR: Primero debe cargar los datos del archivo (OPCION 1)")
            os.system("pause")
            os.system("cls")
        case 12:
            try:
                guardar_json__o_csv=input("Ingrese como quiere guardar (json/csv):")
                direccion_archivo_nuevo = input("Ingrese direccion y nombre al final como quiera guardar el archivo: EJ: ./nuevo_archivo.formato:")
                guardar_json_csv(lista_con_agregados,direccion_archivo_nuevo,False)
            except NameError:
                print("ERROR: Primero debe cargar los datos del archivo (OPCION 1)")
            os.system("cls")

        case _:
            print("Ingrese opcion valida")
