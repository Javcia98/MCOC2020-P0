# -*- coding: utf-8 -*-
import numpy as np
import scipy.linalg as splinalg
from time import perf_counter
from numpy import float64
from matriz_laplaceana import matriz_laplaceana
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import spsolve

lista_N =  [
    2, 5, 10,
    12, 15, 20,
    30, 40, 45, 50, 55,
    60, 75, 100,
   125, 160, 200,
   250, 350, 500,800,1000, 2000,10000]
    

name = (f"ENTREGA7_SOLVE{4}.txt")  #aqui se pone el nombre del archivo 
fid = open(name,"w")

for N in lista_N:
    
    t1 = perf_counter()
    A = matriz_laplaceana(N, float64)
    B = np.ones(N)
    t2 = perf_counter()
    sol = splinalg.solve(A,B,assume_a="pos", overwrite_a=True)
    t3 = perf_counter()
    
    dt_ensamblado_ML = t2 - t1
    dt_solucion_ML = t3 - t2
    
    t4 = perf_counter()
    A2 = csr_matrix(matriz_laplaceana(N))
    B2 = np.ones(N)
    t5 = perf_counter()
    sol = spsolve(A2, B2)
    t6 = perf_counter()
    
    dt_ensamblado_MD = t5 - t4
    dt_solucion_MD = t6 - t5
   
    fid.write(f"{dt_ensamblado_ML}  {dt_solucion_ML}  {dt_ensamblado_MD}  {dt_solucion_MD}\n")
    
    fid.flush()
    
    
    
    
    
    
    
    
    
    
    