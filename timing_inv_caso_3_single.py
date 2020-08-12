# -*- coding: utf-8 -*-
import numpy as np
from time import perf_counter
from scipy import linalg
import matplotlib.pyplot as plt
from numpy import zeros, float16, float32, float64

def matriz_laplaciana(N, dtype=float32):
    A = zeros((N,N), dtype=dtype)
    
    for i in range(N):
        for j in range(N):
            if i == j:
                A[i,j] = 2
            if i+1 == j:
                A[i,j] = -1
            if i - 1 == j:
                A[i,j] = -1
    return A

lista_N =  [2, 5, 10,12, 15, 20, 30, 40, 45, 50, 55, 60, 75, 100]

lista_mem = []
lista_dt_scipyT = []


for N in lista_N:
    A = matriz_laplaciana(N)
    
    t1 = perf_counter()
    I = linalg.inv(A,overwrite_a=True)
    t2 = perf_counter()
    dt = t2-t1
    lista_dt_scipyT.append(dt)
    
    size =2*(N**2)*32
    lista_mem.append(size)
    
print (lista_dt_scipyT)

print(lista_mem)


