import math_pi
f = open(r'', encoding='utf-8').read().split() # переменной f присвоил и разделил на слова текст
pi=str(math_pi.pi(b = 401))                                                              #присвоил 400 цифр числа п т.к. таблица 20 на 20

def hash(slovo):                                                                         #функция прибавляет акси коду одну из цифр числа п и делит на длину слова     
    summa = 0
    t=0
    for bukva in slovo:
        summa = summa + ord(bukva) + int(tablica[0][t])
        t=t+1
    return (summa/len(slovo))

def print_matrix(arr_pi):                                                               #функция для вывода матрицы числа п
    for arr in arr_pi:
        for el in arr:
            print(el, end=' ')
        print()

def pi_matrix(pi):                                                                      #функция для создания матрицы числа п
    arr_2d=[]
    a=-20
    for i in range(20):
        internal_arr=[]
        a=a+20
        for j in range(20):
            if pi[j]!='.':
                internal_arr.append(pi[j+a])
        arr_2d.append(internal_arr)

    return arr_2d

tablica=pi_matrix(pi)

for slovo in f:                                                                         #вывод результата
    print(hash(slovo))