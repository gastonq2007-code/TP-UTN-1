# La juguetería El MUNDO DE CHARLY nos encarga un programa para conocer qué cantidad de materiales se necesita para la fabricación de distintos juguetes.

# CONFECCIÓN DE UN COMETA: 

# Medidas:

# AB = Diágonal mayor

# DC = Diágonal menor

# BD y BC = lados menores

# AD y AC = lados mayores

# El usuario ingresará las medidas  BC, CD y DA.

# Detalles de construcción

# Debemos tener en cuenta que la estructura del cometa estará dada por un perímetro de varillas de plástico y los correspondientes entrecruces (DC y AB) del mismo material para mantener la forma del cometa.

# El cometa estará construido con papel de alta resistencia. La cola del mismo se construirá con el mismo papel que el cuerpo y representará un 10% adicional del necesario para el cuerpo.

# Necesitamos saber cuántos Mts de varillas de plástico y cuántos de papel son necesarios para la construcción en masa de 10 cometas. Tener en cuenta que los valores de entrada están expresados en Cms.

# ENTRADA
BC = float(input('Introducir BC en cm: '))
CD = float(input('Introducir CD en cm: '))
DA = float(input('Introducir DA en cm: '))


# PROCESO

#LADOS IGUALES DEL COMETA
BD = BC
AC = DA

#DIAGONAL MAYOR
AB = BC + DA

#VALORES PARA 1 COMETA
perimetro_cm = BC + BD + AC + DA
varillas_cm = perimetro_cm + AB + CD

#CALCULO DE AREA Y PAPEL CON 10% EXTRA
area = (AB * CD) / 2
papel_total_cm = area + (area * 0.10)

# MULTIPLICACION PARA 10 COMETAS
varillas_10cometas = varillas_cm * 10
papel_total_10cometas = papel_total_cm * 10

# CONVERSION A METROS
varillas_m = varillas_10cometas / 100
papel_total_m = papel_total_10cometas / 10000

# SALIDA
print('El material necesario para 10 cometas:')
print('Metros de varillas:', varillas_m,'m')
print('Metros de papel:', papel_total_m,'m')
