# First practices

hello = 'Hello word'
whatever = ""

whatever.input()
# you can write what's in the print

hello.upper()
# HELLO WORLD

hello.lower()
# hello world

hello.capitalize()
# Hello world

hello.swapcase()
# hELLO WORLD

hello.title()
# Hello World

hello.strip()
# erases spaces

hello.split()
# ['Hello', 'world']
hello.split('o')
# ['Hell', 'w', 'rld']

hello.replace("world", "python")
# Hello python 

whatever.join(list)
# joins a list of strigns and you can split 'em with spaces, '_', ...

whatever.find(value, init, end)
# to find the position


len(whatever)
# counts characteres


#to change types int to str, int to float...
str(whatever)
int(whatever)
float(whatever)

type(whatever)
# data types
isinstance(whatever, type)
# verifies the type, returns bool


## LISTS & TUPLES ##


"""
- list.append(): add element at the end 

- list.extend(): METE LAS COSAS EN LA UNA A UNA, SACA LO DE LA POSICIÓN QUE SE INDICA, like `+` 

- list.insert(index, 'whatever'): add element in specific position

- list.remove(): removes first element selected based on

- list.pop(): removes and returns the element on a specific position

- list.clear(): erases all elements

- list.index(): returns the position of the first occurence of an element

- list.count(): returns how many times an element appears on the lis

- list.sort(): sort the elements, also alphabetically

- sorted(list): sort the elements, also alphabetically, IT DOESN'T MODIFY THE ORIGINAL

- list.reverse(): reverses order

- list.copy()

- len()

- min() / max()

- zip(lista, lista): creates pairs, but you have to  make it a list : list(zip)
"""

"""
[start:stop:step]

- El `start` se refiere al índice de inicio de la lista. Si se omite, se considera 0.
- El `stop` se refiere al índice de fin de la lista, excluyéndolo. Si se omite, se considera la longitud de la lista.
- El `step` se refiere al número de elementos que se salta entre cada elemento en la lista. Si se omite, se considera 1.
"""

## DICTIONARIES ##

dict.fromkeys()
# creates a dicc from keys and values predet, from two lists

dict.len()
dict.keys()
dict.values()
dict.items()

"""
- .copy()

- .clear()

- .update(): Actualiza el diccionario con pares clave-valor de otro diccionario o de una lista de tuplas (clave, valor).

- .get()`: Devuelve el valor de la clave dada si está presente en el diccionario, de lo contrario devuelve el valor predeterminado (opcional).

- .setdefault(): Si la clave está en el diccionario, devuelve su valor. Si no, inserta la clave con el valor predeterminado (opcional) y devuelve ese valor.

- .pop(): Elimina la clave y devuelve su valor. Si la clave no está presente y se proporciona un valor predeterminado, se devuelve ese valor. Si la clave no está presente y no se proporciona un valor predeterminado, se produce una excepción KeyError.

- .popitem(): Elimina y devuelve un par clave-valor arbitrario del diccionario. Si el diccionario está vacío, se produce una excepción KeyError.

"""
