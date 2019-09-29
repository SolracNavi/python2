# -*- coding: utf-8 -*-
import random

def run():
    print("")
    print("A D I V I N A  E L  N Ú M E R O")
    print("")
    number_found = False
    min = int(input("Escribir el límite inferior:"))
    print("")
    max = int(input("Escribir el límite superior:"))
    print("")
    random_number = random.randint(min, max)

    while not number_found:
        print("")
        number = int(input("Ingresar un número: "))

        if number == random_number:
            print("")
            print("¡¡¡Ganaste!!!")
            print("")
            number_found = True
        elif number > random_number:
            print("")
            print("El número es más pequeño")
        else:
            print("")
            print("El número es más grande")

if __name__ == '__main__':
    run()
