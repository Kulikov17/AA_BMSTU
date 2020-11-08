from time import process_time
from random import randint


def vinogradOptimizeMultMatrix(m, n, q, mtrA, mtrB):
    mulH = [0 for i in range(m)]
    mulV = [0 for i in range(q)]
    mtrRes = [[0 for i in range(q)] for j in range(m)]

    tmp = n - n % 2

    i = 0
    while i < m:
        j = 0
        while j < tmp:
            mulH[i] += mtrA[i][j] * mtrA[i][j + 1]
            j += 2
        i += 1

    i = 0
    while i < q:
        j = 0
        while j < tmp:
            mulV[i] += mtrB[j][i] * mtrB[j + 1][i]
            j += 2
        i += 1

    i = 0
    while i < m:
        j = 0
        while j < q:
            buff = -mulH[i] - mulV[j]
            k = 0
            while k < tmp:
                buff += (mtrA[i][k + 1] + mtrB[k][j]) * (mtrA[i][k] + mtrB[k + 1][j])
                k += 2
            mtrRes[i][j] = buff
            j += 1
        i += 1


    if n % 2 == 1:
        i = 0
        tmp = n - 1
        while i < m:
            j = 0
            while j < q:
                mtrRes[i][j] = mtrRes[i][j] + mtrA[i][tmp] * mtrB[tmp][j]
                j += 1
            i += 1
    return mtrRes


def vinogradMultMatrix(m, n, q, mtrA, mtrB):
    mulH = [0 for i in range(m)]
    mulV = [0 for i in range(q)]
    mtrRes = [[0 for i in range(q)] for j in range(m)]

    i = 0
    while i < m:
        j = 0
        while j < n // 2:
            mulH[i] = mulH[i] + mtrA[i][j * 2] * mtrA[i][j * 2 + 1]
            j += 1
        i += 1

    i = 0
    while i < q:
        j = 0
        while j < n // 2:
            mulV[i] = mulV[i] + mtrB[j * 2][i] * mtrB[j * 2 + 1][i]
            j += 1
        i += 1

    i = 0
    while i < m:
        j = 0
        while j < q:
            mtrRes[i][j] = -mulH[i] - mulV[j]
            k = 0
            while k < n // 2:
                mtrRes[i][j] = mtrRes[i][j] + (mtrA[i][2 * k + 1] + mtrB[2 * k][j]) \
                               * (mtrA[i][2 * k] + mtrB[2 * k + 1][j])
                k += 1
            j += 1
        i += 1

    if n % 2 == 1:
        i = 0
        while i < m:
            j = 0
            while j < q:
                mtrRes[i][j] = mtrRes[i][j] + mtrA[i][n - 1] * mtrB[n - 1][j]
                j += 1
            i += 1
    return mtrRes


def standartMultMatrix(m, n, q, mtrA, mtrB):
    mtrRes = [[0 for i in range(q)] for j in range(m)]
    i = 0
    while i < m:
        j = 0
        while j < q:
            k = 0
            while k < n:
                mtrRes[i][j] += mtrA[i][k] * mtrB[k][j]
                k += 1
            j += 1
        i += 1
    return mtrRes

def menu():
    print('\nМеню: ')
    print('1) Перемножение матриц с помощью стандартного алгоритма')
    print('2) Перемножение матриц c помощью алгоритма Винограда')
    print('3) Перемножение матриц с помощью оптимизированного алгоритма Винограда')
    print('4) Сравнение по времени')


def printMtr(mtr):
    for i in range(len(mtr)):
        for j in range(len(mtr[i])):
            print(int(mtr[i][j]), end=' ')
        print('')


def generateMatrix(size):
    mtr = [[randint(-100, 100) for i in range(size)] for j in range(size)]
    return mtr


def time_analyse():
    size = (int(input("Введите размер: ")))
    iteration = (int(input("Введите кол-во итерации: ")))
    timeStandart = 0
    timeVinograd = 0
    timeOptVinograd = 0
    for i in range(iteration):
        mtr1 = generateMatrix(size)
        mtr2 = generateMatrix(size)

        start_time = process_time()
        standartMultMatrix(size, size, size, mtr1, mtr2)
        end_time = process_time()
        timeStandart += end_time - start_time

        start_time = process_time()
        standartMultMatrix(size, size, size, mtr1, mtr2)
        end_time = process_time()
        timeVinograd += end_time - start_time

        start_time = process_time()
        standartMultMatrix(size, size, size, mtr1, mtr2)
        end_time = process_time()
        timeOptVinograd += end_time - start_time
    return timeStandart / iteration, timeVinograd/iteration, timeOptVinograd/iteration

def mult(func):
    print('Дано матрица А[m x n] и матрица B[n x q]')
    m = int(input('Введите m: '))
    n = int(input('Введите n: '))
    q = int(input('Введите q: '))
    print('Ввод матрицы А:')
    a = [[0 for i in range(n)] for j in range(m)]
    for i in range(m):
        for j in range(n):
            a[i][j] = int(input('a['+ str(i) +']['+ str(j) +'] = '))
    b = [[0 for i in range(q)] for j in range(n)]
    print('Ввод матрицы B:')
    for i in range(n):
        for j in range(q):
            b[i][j] = int(input('b[' + str(i) + '][' + str(j) + '] = '))
    print()
    print('Матрица А:')
    printMtr(a)
    print()
    print('Матрица B:')
    printMtr(b)
    print()
    print('Результат переумножения: ')
    printMtr(func(m,n,q, a, b))

if __name__ == "__main__":
    while True:
        menu()
        menuSelection = int(input('Выберите пункт меню: '))
        print()
        if menuSelection == 1:
            print("Стандартный алгоритм умножения матриц")
            mult(standartMultMatrix)
        elif menuSelection == 2:
            print("Алгоритм умножения матриц по Винограду")
            mult(vinogradMultMatrix)
        elif menuSelection == 3:
            print("Оптимизированный алгоритм умножения матриц по Винограду")
            mult(vinogradOptimizeMultMatrix)
        elif menuSelection == 4:
            print("Анализ времени")
            timeStandart, timeVinograd, timeOptVinograd = time_analyse()
            print('Время работы стандартного алгоритма умножения: ', timeStandart, 'сек')
            print('Время работы алгоритма умножения по Винограду: ', timeVinograd, 'сек')
            print('Время работы оптимизированного алгоритма умножения по Винограду: ', timeOptVinograd, 'сек')
        else:
            print('Некорректный ввод меню')

