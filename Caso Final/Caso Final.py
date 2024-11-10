""" 
El número de Sheldon: En la serie “Big Bang Theory” se conjeturó que el número
23 posee unas características únicas que no posee ningún otro número (link a la conjetura
original). En 2019 Pomerance y Spicer demostraron que solo el 73 cumple las condiciones de
la Conjetura de Sheldon (link a la desmostración). 

El ejercicio consistirá en comprobar que en los números entre el 1 y el 1 000 000 solo el 73 cumple la conjetura de Sheldon. Un
número de Sheldon debe cumplir 3 propiedades:

    a. Es primo.
    b. El producto de sus dígitos [llamemos a esta operación m()] es igual a su posición en
    la lista de todos los primos (empezando por el número 2). Por ejemplo: En 73, m(73)= 7*3 = 21 y en la lista de primos el 73 está en la posición 21ª (se puede comprobar
    con el ejercicio 6).
    c. El número espejo de otro será el conseguido al invertir el orden de las [llamemos a
    esta operación r()]. El primo en la posición de su número espejo es igual al número
    espejo de su posición. Por ejemplo: r(73) = 37, la posición del 37 es la doceava, el
    espejo de 12 es 21 y el número primo en la posición 21ª es el 73. """

import numpy as np

def soyprimo(x, primos):
    if x < 2:
        return False
    for primo in primos:
        if primo * primo > x:
            break
        if x % primo == 0:
            return False
    return True

def obtener_primos(hasta):
    primos = []
    for num in range(2, hasta + 1):
        if soyprimo(num, primos):
            primos.append(num)
    return primos

def posicion(primo, primos):
    return primos.index(primo) + 1  # La posición es índice + 1

def m(n):
    digitos = [int(digit) for digit in str(n)]
    m = 1
    for digito in digitos:
        m *= digito
    return m

def numero_espejo(n):
    return int(str(n)[::-1])

def r(n, primos):
    pos_n = posicion(n, primos)
    espejo_primo = numero_espejo(n)
    pos_espejo_primo = posicion(espejo_primo, primos)
    espejo_pos = numero_espejo(pos_espejo_primo)
    return espejo_pos == pos_n

primos = obtener_primos(1000000)

for primo in primos:
    if m(primo) == posicion(primo, primos) and r(primo, primos):
        print(f"El {primo} es un número Sheldon")
