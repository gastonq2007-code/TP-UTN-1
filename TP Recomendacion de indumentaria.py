from colorama import init, Fore, Style
init(autoreset=True)

# Una cadena abierta 
nombre = input(Fore.CYAN + "Ingrese su nombre: ")
edad = float(input(Fore.CYAN + "Ingrese su edad: "))
genero = input(Fore.CYAN + "¿Qué género sos? (F/M): ")
genero = genero.lower()

opcion = input(Fore.BLUE + "\nSelecciona una opción:\n1. Selección de prenda\n2. Salir\n")

match opcion: 
    case "1":
        tipo_prenda = input(Fore.BLUE + "\n¿Qué tipo de prenda te interesa?\n1. Superior\n2. Inferior\n")
        
        if tipo_prenda == "1":
            medida_pecho = float(input("Ingrese su ancho de pecho: "))
            ancho_hombro = float(input("Ingrese su ancho de hombros: "))
            largo_torso = float(input("Ingrese su largo de torso: "))  

            if genero == "f":
                if (52 <= medida_pecho <= 54) and (43 <= ancho_hombro <= 45) and (64 <= largo_torso <= 66):
                    mensaje = "te recomiendo un talle S"
                elif (54 < medida_pecho <= 56) and (45 < ancho_hombro <= 47) and (66 < largo_torso <= 68):
                    mensaje = "te recomiendo un talle M"
                elif (56 < medida_pecho <= 58) and (47 < ancho_hombro <= 49) and (68 < largo_torso <= 70):
                    mensaje = "te recomiendo un talle L"
                else:
                    mensaje = None

            elif genero == "m":
                if (56 <= medida_pecho <= 58) and (52 <= ancho_hombro <= 54) and (68 <= largo_torso <= 70):
                    mensaje = "te recomiendo un talle S"
                elif (58 < medida_pecho <= 60) and (54 < ancho_hombro <= 56) and (70 < largo_torso <= 72):
                    mensaje = "te recomiendo un talle M"
                elif (60 < medida_pecho <= 62) and (56 < ancho_hombro <= 58) and (72 < largo_torso <= 74):
                    mensaje = "te recomiendo un talle L"
                else:
                    mensaje = None
                
        elif tipo_prenda == "2":
            medida_cintura = float(input("Ingrese contorno de cintura: "))
            medida_cadera = float(input("Ingrese contorno de cadera: "))
            largo_pierna = float(input("Ingrese el largo desde la cadera hasta el tobillo: "))
            
            if genero == "f":
                if ((70 <= medida_cintura <= 72) or (98 <= medida_cadera <= 100)) and (103 <= largo_pierna <= 105):
                    mensaje = "te recomiendo un talle 34"
                elif ((72 < medida_cintura <= 76) or (100 < medida_cadera <= 104)) and (105 < largo_pierna <= 107):
                    mensaje = "te recomiendo un talle 36"
                elif ((76 < medida_cintura <= 80) or (104 < medida_cadera <= 108)) and (107 < largo_pierna <= 109):
                    mensaje = "te recomiendo un talle 38"
                else:
                    mensaje = None

            elif genero == "m":
                if ((80 <= medida_cintura <= 84) or (108 <= medida_cadera <= 112)) and (104 <= largo_pierna <= 106):
                    mensaje = "te recomiendo un talle 42"
                elif ((84 < medida_cintura <= 88) or (112 < medida_cadera <= 116)) and (106 < largo_pierna <= 108):
                    mensaje = "te recomiendo un talle 44"
                elif ((88 < medida_cintura <= 92) or (116 < medida_cadera <= 120)) and (108 < largo_pierna <= 110):
                    mensaje = "te recomiendo un talle 46"
                else:
                    mensaje = None

    case "2":
        mensaje = "Gracias por tu visita"

# DESCUENTOS
if 12 <= edad <= 15:
    descuento = "10% OFF en todas nuestras tiendas"
elif edad >= 65:
    descuento = "15% OFF Martes y Jueves en todas nuestras tiendas"
else:
    descuento = "5% OFF pagando con MODO todos los lunes"

# OUTPUT FINAL
print(Fore.BLUE + "\n-----------------------------------")

if opcion == '2':
    print(Fore.CYAN + Style.BRIGHT + "¡Gracias por tu visita!")
elif not mensaje:
    print(Fore.RED + Style.BRIGHT + "Disculpa, no contamos con ese talle")
else:
    print(Fore.GREEN + Style.BRIGHT + f"{nombre}, {mensaje}")
    print(Fore.YELLOW + f"Descuento: {descuento}")

print(Fore.BLUE + "-----------------------------------")
