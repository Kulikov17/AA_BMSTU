import numpy as np
import random
import string
from time import process_time

def operations(s1, s2, matr):
    def pathfinder(m, i, j):
        if i > 0 and j > 0 and m[i - 1][j - 1] < m[i][j]:
            pathfinder(m, i - 1, j - 1)
            print('R', end=' ')
        elif i > 0 and m[i - 1][j] < m[i][j]:
            pathfinder(m, i - 1, j)
            print('D', end=' ')
        elif j > 0 and m[i][j - 1] < m[i][j]:
            pathfinder(m, i, j - 1)
            print('I', end=' ')
        elif i > 0 and j > 0 and m[i - 1][j - 1] == m[i][j]:
            pathfinder(m, i - 1, j - 1)
            print('M', end=' ')

    print('\nOperation:')
    pathfinder(matr, len(s1), len(s2))


def outputMatrix(s1, s2, matr):
    print("   ", end=" ")
    for i in s2:
        print(i, end=" ")

    for i in range(len(matr)):
        if i:
            print("\n" + s1[i - 1], end=" ")
        else:
            print("\n ", end=" ")
        for j in range(len(matr[i])):
            print(int(matr[i][j]), end=" ")

def generateString(lenString):
    return ''.join(random.choice(string.ascii_letters) for _ in range(lenString))

def LevenshteinDistanceMatrix(s1, s2, printMatrix = False):
    lens1 = len(s1)
    lens2 = len(s2)
    D = np.eye(lens1 + 1, lens2 + 1)
    D[0][0] = 0
    for i in range(1, lens1 + 1):
        D[i][0] = i
    for j in range(1, lens2 + 1):
        D[0][j] = j
    for i in range(1, lens1 + 1):
        for j in range(1, lens2 + 1):
            cost = 0 if s1[i - 1] == s2[j - 1] else 1
            D[i][j] = min(D[i - 1][j] + 1, D[i][j - 1] + 1, D[i - 1][j - 1] + cost)

    if printMatrix:
        print('Matrix:')
        outputMatrix(s1, s2, D)
        operations(s1, s2, D)
        print('')

    return D[lens1][lens2]

def LevenshteinDistanceRecursion(s1, s2, printAnswer = False):
    lens1 = len(s1)
    lens2 = len(s2)
    if lens1 == 0 or lens2 == 0:
        tmp = abs(lens1 - lens2)
    else:
        cost = 0 if s1[-1] == s2[-1] else 1
        tmp = min(LevenshteinDistanceRecursion(s1[:-1], s2) + 1,
               LevenshteinDistanceRecursion(s1, s2[:-1]) + 1,
               LevenshteinDistanceRecursion(s1[:-1], s2[:-1]) + cost)
    return tmp

def LevenshteinDistanceRecursionMatrix(s1, s2, printMatrix = False):
    def calcValue(D, i, j):
        if D[i][j] != -1:
            return D[i][j]
        else:
            cost = 0 if s1[i - 1] == s2[j - 1] else 1
            D[i][j] = min(calcValue(D, i - 1, j) + 1,
                          calcValue(D, i, j - 1) + 1,
                          calcValue(D, i - 1, j - 1) + cost)
            return D[i][j]

    lens1 = len(s1)
    lens2 = len(s2)
    D = np.full((lens1 + 1, lens2 + 1), -1)
    for i in range(lens1 + 1):
        D[i][0] = i
    for j in range(lens2 + 1):
        D[0][j] = j

    return calcValue(D, lens1, lens2)

def DamerauLevenshteinDistanceMatrix(s1, s2, printMatrix = False):
    lens1 = len(s1)
    lens2 = len(s2)
    D = np.eye(lens1 + 1, lens2 + 1)
    D[0][0] = 0
    for i in range(1, lens1 + 1):
        D[i][0] = i
    for j in range(1, lens2 + 1):
        D[0][j] = j
    for i in range(1, lens1 + 1):
        for j in range(1, lens2 + 1):
            cost = 0 if s1[i - 1] == s2[j - 1] else 1
            D[i][j] = min(D[i - 1][j] + 1, D[i][j - 1] + 1, D[i - 1][j - 1] + cost)
            if i > 1 and j > 1 and s1[i - 1] == s2[j - 2] and s1[i - 2] == s2[j - 1]:
                D[i][j] = min(D[i][j], D[i - 2][j - 2] + cost)

    if printMatrix:
        print('Matrix:')
        outputMatrix(s1, s2, D)
        operations(s1, s2, D)
        print('')

    return D[lens1][lens2]


def findDistance(func, s1, s2, printMatrix):
    return func(s1, s2, printMatrix)


def TimeAnalyse(function, iterations, length):
    t1 = process_time()
    for _ in range(iterations):
        s1 = generateString(length)
        s2 = generateString(length)
        function(s1, s2, False)
    t2 = process_time()
    return (t2 - t1) / iterations


if __name__ == "__main__":
    arrayFunction = {
        1: LevenshteinDistanceMatrix,
        2: LevenshteinDistanceRecursion,
        3: LevenshteinDistanceRecursionMatrix,
        4: DamerauLevenshteinDistanceMatrix,
        5: TimeAnalyse
    }

    menu = "Меню:\n\
1) Расстояние Левенштейна матричный алгоритм\n\
2) Расстояние Левенштейна рекурсивный алгоритм по формуле\n\
3) Расстояние Левенштейна рекурсивный алгоритм, заполняющий матрицу\n\
4) Расстояние Дамерау-Левенштейна матричный алгоритм\n\
5) Сравнение по времени расстояние Левенштейна\n"

    while True:
        print(menu)
        menuSelection = int(input('Выберите пункт меню: '))
        try:
           callFunc = arrayFunction[menuSelection]
           if menuSelection != 5:
               s1 = input("Введите первую строку: ")
               s2 = input("Введите вторую строку: ")
               printMatrix = True
               print(findDistance(callFunc, s1, s2, printMatrix))
           else:
               iterations = 100
               lengthString = 10
               print("Замер времени: ")
               print("Кол-во итераций: ", iterations)
               print("Длина строк: ", lengthString)
               print("Матричный алгоритм нахождения расстояния Левенштейна: ", TimeAnalyse(LevenshteinDistanceMatrix, 100, 5))
               print("Рекурсивный алгоритм нахождения расстояния Левенштейна: ", TimeAnalyse(LevenshteinDistanceRecursion, 100, 5))
               print("Рекурсивный алгоритм нахождения расстояния Левенштейна с заполнением матрицы: ", TimeAnalyse(LevenshteinDistanceRecursionMatrix, 100, 5))
               print("Матричный алгоритм нахождения расстояния Дамерау-Левенштейна: ", TimeAnalyse(DamerauLevenshteinDistanceMatrix, 100, 5))

        except KeyError:
            print("Выберите верный пункт меню")
            continue

