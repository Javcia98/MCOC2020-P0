# -*- coding: utf-8 -*-
import numpy as np


def mimatmul(A,B):      
    result = []
    matrix = []
    for i in range(len(A)):
        result.append([])
        for j in range(len(B[0])):
            result[i].append(0) 
  

    for i in range(len(A)): 
  
    
        for j in range(len(B[0])): 
  
        
            for k in range(len(B)): 
                result[i][j] += A[i][k] * B[k][j] 
  
    for r in result: 
        matrix.append(r)
    return matrix








