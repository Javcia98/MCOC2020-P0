# -*- coding: utf-8 -*-
from numpy import *
from time import perf_counter
import matplotlib.pyplot as plt
import numpy as np

lista_N = [1,4,10,12,16,20,30,42,46,50,54,60,65,70,100,120,170,200,240,410,500,550,800,2000,5000,10000]
lista_dt = []
lista_mem = []
name = (f"holahola{1}.txt")  #aqui se pone el nombre del archivo 
fid = open(name,"w")

for N in lista_N:
    
    A = np.random.rand(N,N)
    B = np.random.rand(N,N)
    
    
    t1 = perf_counter()
    C = A@B
    t2 = perf_counter()
    
    dt = t2 - t1
    size = 3*(N**2)*8 #bytes
    lista_dt.append(dt)
    lista_mem.append(size)
    fid.write(f"{N} {dt}  {size}\n")
    
    fid.flush()

fid.close() 


plt.plot(lista_N,lista_dt,"-o",  color='b')
plt.grid(True)
plt.ylabel('Tiempo transcurrido ')
plt.yscale('log')
plt.xscale('log')

tricky = [0.0001, 0.001, 0.01, 0.1, 1, 10, 60, 600]
tricky_txt = ['0.1 ms', '1 ms', '10 ms', '0.1 s', '1 s', '10 s', '1 min', '10 min']

plt.yticks(tricky, tricky_txt) 

trickx = [10,20,50,100,200,500,1000,2000,5000,10000,20000]
trickx_txt = ["","","","","","","","","","",""]
plt.xticks(trickx, trickx_txt)

plt.show() 

plt.plot(lista_N,lista_mem,"-o",  color='b')
plt.grid(True)
plt.xlabel('Tamaño matriz N')
plt.ylabel('Uso memoria')
plt.yscale('log')
plt.xscale('log')


tricky2 = [1000, 10000, 100000, 1000000 , 10000000 , 100000000 , 1000000000 , 10000000000 ]
tricky2_txt = ['1 KB', '10 KB', '100 KB', '1 MB', '10 MB', '100 MB', '1 GB', '10 GB']
plt.yticks(tricky2, tricky2_txt)

trickx = [10,20,50,100,200,500,1000,2000,5000,10000,20000]
trickx_txt = [10,20,50,100,200,500,1000,2000,5000,10000,20000]
plt.xticks(trickx, trickx_txt) 



  





