# En una ferretería se quiere implementar un sistema que permita a los usuarios saber cuánto deberán pagar por la compra de lámparas de bajo consumo. Se tiene en cuenta que todas las lámparas cuestan $800.

# A partir de la cantidad y marca de las lámparas compradas (solo se puede comprar una marca por vez) se aplicará el siguiente descuento:

# Si compra 6 o más  lámparas bajo consumo tiene un descuento del 50%. 

# Si compra 5  lámparas bajo consumo marca "ArgentinaLuz" se hace un descuento del 40 % y si es de otra marca el descuento es del 30%.

# Si compra 4  lámparas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” se hace un descuento del 25 % y si es de otra marca el descuento es del 20%.

# Si compra 3  lámparas bajo consumo marca "ArgentinaLuz"  el descuento es del 15%, si es  “FelipeLamparas” se hace un descuento del 10 % y si es de otra marca un 5%.

# Por otro lado, si el importe final con descuento suma más de $4000  se obtiene un descuento adicional de 5%.

# Mostrar por pantalla: 

# Marca, cantidad de lámparas, total a pagar sin descuento, el descuento obtenido si corresponde, el descuento adicional (si corresponde) y el total a pagar con descuento.
PRECIO = 800
descuento = 0
descuento_extra = 0
#ENTRADAS
cantidad_lamparas = int(input("Ingrese cantidad de lamparas: "))
marca = input("Ingrese la marca: ")
#PROCESOS
total_sin_descuentos = PRECIO * cantidad_lamparas



if cantidad_lamparas >= 6:
    descuento = 0.50
elif cantidad_lamparas == 5 and marca == 'ArgentinaLuz':
    descuento = 0.40
elif cantidad_lamparas == 5:
    descuento = 0.30
elif cantidad_lamparas == 4 and (marca == 'ArgentinaLuz' or marca == 'FelipeLamparas'):
    descuento = 0.25
elif cantidad_lamparas == 4:
    descuento = 0.20
elif cantidad_lamparas == 3 and marca == 'ArgentinaLuz':
    descuento = 0.15
elif cantidad_lamparas == 3 and marca == 'FelipeLamparas':
    descuento = 0.10
elif cantidad_lamparas == 3:
    descuento = 0.05

descuento_aplicar = total_sin_descuentos * descuento


total_con_descuento = total_sin_descuentos - descuento_aplicar
if total_con_descuento > 4000:
    descuento_extra = total_con_descuento * 0.05
    
total_a_pagar = total_con_descuento - descuento_extra

#SALIDAS
print('Usted compro nuestra marca' , marca)
print('Usted compro una cantidad de ' , cantidad_lamparas)
print('El total sin descuentos seria de ' , total_sin_descuentos)
if descuento > 0: 
    print('Su descuento seria de ' , descuento_aplicar)
if descuento_extra > 0:
    print('Su descuento extra seria de ' , descuento_extra)
print('Y su total seria de 3' , total_con_descuento)



