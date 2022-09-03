# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 18:11:24 2022

@author: Brian
"""

def binary(natural):
    """
    input: natural number
    output: number and binary representation of that number in a tuple
    """
    if type(natural) != int or  natural < 0 :
        raise TypeError(f"'{natural}' is not a natural number")
   
    input_ = natural
   
    if natural == 0:
        return input_,0
    
    if natural == 1:
        return input_,1
   
    binary_result = ""
    while natural != 1:    # entro al bucle si natural >= 2
        if natural%2 == 0:       #natural es par
            add = "0"
        else:                    #natural es impar
            add = "1"
        binary_result = add + binary_result
        natural = natural//2
        
        # print for debug como si fuera console.log() :)
        # print(add, natural, binary_result)
        
    binary_result = "1" + binary_result
    return input_,int(binary_result)



# Pruebo el código
for i in range(20):
    print(binary(i))



