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
    pass


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