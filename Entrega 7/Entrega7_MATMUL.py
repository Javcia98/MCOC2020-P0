# -*- coding: utf-8 -*-
from time import perf_counter
from numpy import zeros,fill_diagonal, float64
from matriz_laplaceana import matriz_laplaceana
from mimatmul import mimatmul
from scipy.sparse import csr_matrix

lista_N =  [
    2, 5, 10,
    12, 15, 20,
    30, 40, 45, 50, 55,
    60, 75, 100,
   125, 160, 200,
   250, 350, 500, 800, 1000, 2000, 5000, 10000]

corridas = 5

for i in range(corridas):
    name = (f"ENTREGA7_MATMUL{0}.txt")  #aqui se pone el nombre del archivo 
    fid = open(name,"w")

    for N in lista_N:
    
        t1 = perf_counter()
        A = matriz_laplaceana(N, float64)
        B = matriz_laplaceana(N, float64)
        t2 = perf_counter()
        C = mimatmul(A,B)
        t3 = perf_counter()
    
        dt_ensamblado_ML = t2 - t1
        dt_solucion_ML = t3 - t2
    
        t4 = perf_counter()
        A2 = csr_matrix(matriz_laplaceana(N,float64))
        B2 = csr_matrix(matriz_laplaceana(N,float64))
        t5 = perf_counter()
        C = A2@B2
        t6 = perf_counter()
    
        dt_ensamblado_MD = t5 - t4
        dt_solucion_MD = t6 - t5
   
        fid.write(f"{dt_ensamblado_ML}  {dt_solucion_ML}  {dt_ensamblado_MD}  {dt_solucion_MD}\n")
    
        fid.flush()

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    