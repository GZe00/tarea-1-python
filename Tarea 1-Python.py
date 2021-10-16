from os import name, system
system('cls')
"""

    Contador de palabras: crear un script que lea el nombre de un archivo de texto y retorne las 10 palabras más repetidas. 

        Deberías usar listas, diccionarios, ciclos, funciones, try/excep

"""

# Adjuntar los archivos .txt en el mismo nivel de este programa para su lectura


def most_repeated_words(file_name):
    result = dict()
    j = 0
    try:
        file = open(str(file_name))
        for words in file:
            for word in words.strip().split(" "):
                if word == "":
                    continue
                result[word] = result.get(word, 0) + 1
        try:
            result_orders = sorted(result.items(), key=lambda x: x[1], reverse=True)
            1/len(result_orders)
            print('Las 10 palabras más repetidas del archivo', file_name)
            for i in result_orders:
                print(i[0], i[1])
                if j == 9:
                    break
                j += 1
        except ZeroDivisionError:
            print('El contenido del archivo está vacío.')
    except FileNotFoundError:
        print('No existe el archivo a operar.')



name_file = input('Ingrese el nombre del archivo (no incluya la extensión):> ')

most_repeated_words(name_file +'.txt')
