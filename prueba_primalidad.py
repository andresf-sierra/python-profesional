# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 23:23:47 2021

@author: TAURET
"""

"""
Este código es para saber si un número
es primo o no es primo. En este caso estoy 
tipado estático y hay un error en la 
variable número

"""
def es_primo(number: int) -> str:
    cont = 0
    
    for i in range(1, number + 1):
        if i == 1 or i == number:
            continue 
        if number % i == 0:
            cont += 1
    if cont == 0:
        return True
    else:
        return False     
        

def main():
    number = "Apolo" #Aquí podría pedir mi número
    if es_primo(number):
        print("Es primo")
    else: 
        print("No es primo")
    
    
if __name__ == "__main__":
        main()