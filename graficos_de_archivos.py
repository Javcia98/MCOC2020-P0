# -*- coding: utf-8 -*-
from numpy import *
from time import perf_counter
import matplotlib.pyplot as plt
import numpy as np
plt.figure(figsize=(10,5))
lista_mem = [24, 384, 2400, 3456, 6144, 9600, 21600, 42336, 50784, 60000, 69984, 86400, 101400, 117600, 240000, 345600, 693600, 960000, 1382400, 4034400, 6000000, 7260000, 15360000, 96000000, 600000000, 2400000000]
lista_N = [1,4,10,12,16,20,30,42,46,50,54,60,65,70,100,120,170,200,240,410,500,550,800,2000,5000,10000]

def info_archivo(nombre):
    archivo = open(nombre)

    l = []
    l = [ line.split() for line in archivo]

    lista_dt = []

    for lista in l:
        dt = float(lista[1])
        lista_dt.append(dt)
    archivo.close()
    
    return (lista_dt)

dt1 = info_archivo("matmul11.txt")
dt2 = info_archivo("matmul2.txt")
dt3 = info_archivo("matmul3.txt")
dt4 = info_archivo("matmul4.txt")
dt5 = info_archivo("matmul5.txt")
dt6 = info_archivo("matmul6.txt")
dt7 = info_archivo("matmul7.txt")
dt8 = info_archivo("matmul8.txt")
dt9 = info_archivo("matmul9.txt")
dt10 = info_archivo("matmul10.txt")

plt.plot(lista_N,dt1,"-o",  color='b')
plt.plot(lista_N,dt2,"-o",  color='r')
plt.plot(lista_N,dt3,"-o",  color='m')
plt.plot(lista_N,dt4,"-o",  color='k')
plt.plot(lista_N,dt5,"-o",  color='g')
plt.plot(lista_N,dt7,"-o",  color='c')
plt.plot(lista_N,dt8,"-o",  color='y')
plt.plot(lista_N,dt9,"-o",  color='b')
plt.plot(lista_N,dt10,"-o",  color='r')

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
plt.title("Rendimiento A@B")
plt.show() 
plt.figure(figsize=(10,5))
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






























