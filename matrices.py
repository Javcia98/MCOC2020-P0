# -*- coding: utf-8 -*-
import scipy as sp

N = 3

A = sp.rand(N,N)
B = sp.rand(N,N)

print(f"A = \n{A}")
print(f"B = \n{B}")

Ma = sp.matrix(A)
Mb = sp.matrix(B)

Forma1=A*B
Forma2=Ma*Mb

print (Forma1[0,0])
print (Forma2[0,0])
