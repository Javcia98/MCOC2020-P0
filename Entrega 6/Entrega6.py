# -*- coding: utf-8 -*-
import numpy as np
import scipy.linalg as splinalg
from time import perf_counter
from numpy import zeros,fill_diagonal,float32

def matriz_laplaceana(N,dtype=float32):
    A=zeros((N,N), dtype=dtype)
    fill_diagonal(A,2)
    for i in range(N):
        for j in range(N):
            if (abs(i-j)==1):
                A[i,j]=-1       
    return A

lista_N =  [
    2, 5, 10,
    12, 15, 20,
    30, 40, 45, 50, 55,
    60, 75, 100,
    125, 160, 200,
    250, 350, 500,800,
    1000, 2000, 5000,10000]

Ncorridas = 5
names = ["A_invB.txt", "A_invB_npSolve.txt","A_invB_spSolve.txt", "A_invBspSolve_symmetric.txt", "A_invB_spSolve_pos.txt",
         "A_invB_spSolve_pos_overwrite_a.txt","A_invB_spSolve_pos_overwrite_b.txt"]

files = [open(name, "w") for name in names]

for N in lista_N:
    
    dts =np.zeros((Ncorridas,len(files)))
    
    for i in range(Ncorridas):
        
        
        #Invirtiendo y multiplicando
        A = matriz_laplaceana(N)
        B = np.ones(N)
        t1 = perf_counter()
        A_inv = np.linalg.inv(A)
        A_invB = A_inv@B
        t2 = perf_counter()
        dt = t2-t1
        dts[i][0] = dt
        
        #Ocupando np.linalg.solve(A,B)
        
        A = matriz_laplaceana(N)
        B = np.ones(N)
        t1 = perf_counter()
        A_invB = np.linalg.solve(A,B)
        t2 = perf_counter()
        dt = t2-t1
        dts[i][1] = dt
        
        #Ocupando sp.linalg.solve(A,B)
        
        A = matriz_laplaceana(N)
        B = np.ones(N)
        t1 = perf_counter()
        A_inv = splinalg.solve(A,B)
        t2 = perf_counter()
        dt = t2-t1
        dts[i][2] = dt
        
        #Ocupando A_invBspSolve_symmetric
        
        A = matriz_laplaceana(N)
        B = np.ones(N)
        t1 = perf_counter()
        A_inv = splinalg.solve(A,B,sym_pos=True)
        t2 = perf_counter()
        dt = t2-t1
        dts[i][3] = dt
        
        #Ocupando A_invB_spSolve_pos
        
        A = matriz_laplaceana(N)
        B = np.ones(N)
        t1 = perf_counter()
        A_inv = splinalg.solve(A,B,assume_a="pos")
        t2 = perf_counter()
        dt = t2-t1
        dts[i][4] = dt
        
        
        #Ocupando overwrite_a
        
        A = matriz_laplaceana(N)
        B = np.ones(N)
        t1 = perf_counter()
        A_inv = splinalg.solve(A,B,assume_a="pos", overwrite_a=True)
        t2 = perf_counter()
        dt = t2-t1
        dts[i][5] = dt
        
        #Ocupando overwrite_b
        
        A = matriz_laplaceana(N)
        B = np.ones(N)
        t1 = perf_counter()
        A_inv = splinalg.solve(A,B,assume_a="pos", overwrite_b=True)
        t2 = perf_counter()
        dt = t2-t1
        dts[i][6] = dt
        

                                
    dts_mean = [np.mean(dts[:,j]) for j in range(len(files))]
    
    
    for j in range(len(files)):
        files[j].write(f"{N} {dts_mean[j]}\n")
        files[j].flush()

[file.close() for file in files]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        