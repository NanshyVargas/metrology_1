import numpy as np
import pandas as pd
import math

#тестовые данные
def GetDataTest():
    result = np.zeros((5,5))
    for i in range(result.shape[0]):
        for j in range(result.shape[1]):
            result[i][j] = i
    return result

'''
Функция, которая заполняет массив
'''
def ZapolnitMassiv(mas : np.ndarray):
    masB = np.zeros((5))
    temp = np.zeros((5))
    for i in range(mas.shape[0]):
        temp[i] = sum(mas[i])
        if (temp[i]%2==0):
            masB[i] = 2
        else:
            masB[i] = 1
    return(masB)


'''
Факториал
'''
def Factorial(mas : np.ndarray):
    pass


def main():
    masA = GetDataTest()
    print(masA)
    masA = ZapolnitMassiv(masA)
    masA = Factorial(masA)


main()