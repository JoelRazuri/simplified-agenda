"""
    # Agenda simplificada:
    
    Escribir una función que reciba una cadena a buscar y una lista de tuplas (nombre_completo, telefono), y busque dentro de la lista, todas las entradas que contengan en el nombre completo 
    la cadena recibida (puede ser el nombre, el apellido o sólo una parte de cualquiera de ellos). Debe devolver una lista con todas las tuplas encontradas.
"""

lista_nombres = [('Axel Joel Rázuri Fiorilli',15512321), ('Matias Arevalo',15512154), ('Juanca Martinez Areval',1551234), ('Sofia Gucci Arev',1245621)]
sub_cadena = 'ev'




def agenda(lista_de_tuplas, cadena):

    lista = []

    for i in range(0,len(lista_de_tuplas)):
        if cadena in lista_de_tuplas[i][0]:
            lista.append(lista_de_tuplas[i])

    return lista



print(agenda(lista_nombres,sub_cadena))