# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 22:06:37 2024

@author: VIMALATHAS VITHUSAN
"""

import numpy as np

matrix1 = np.array([
                    [2, 3], 
                    [3, 2]
                    ])

matrix2 = np.array([
                    [1, 3], 
                    [5, 2]
                    ])

rows, cols = matrix1.shape

# DECLARE A 2D LIST WITHOUT INITIALIZING
result = [[0] * cols for _ in range(rows)]

for i in range(rows):
    for j in range(cols):
        result[i][j] += matrix1[i, j] * matrix2[i, j]
        

print(result)