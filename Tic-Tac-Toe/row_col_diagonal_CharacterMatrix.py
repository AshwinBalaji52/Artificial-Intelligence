# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 18:20:10 2021

@author: dell
"""

import sys
gameplay = [['X','X','X'],
            ['O','X','O'],
            ['O','X','X']]

result = [['_','_','_'],
          ['_','_','-'],
          ['_','_','_']]

principal_diagonal = []
secondary_diagonal=[]
diagonal = []
for i in range(len(gameplay)):
    for j in range(len(gameplay)):
        if(i==j):
            #pd = []
            principal_diagonal.append(gameplay[i][j])
            print(i,j)
        elif((i+j)==2):
            secondary_diagonal.append(gameplay[i][j])
            print(i,j)
print(principal_diagonal)
print(secondary_diagonal)
        
        #elif((i+j)==(len(gameplay)-1)):
            #diagonal.append(gameplay[i][j])
            #print(diagonal)
            





'''
"Row"
for i in range(len(gameplay)):
    for j in range(len(gameplay[i])):
        if(gameplay[i][j]==gameplay[i][j+1]==gameplay[i][j+2]):
            print("Wohooo .... ",gameplay[i][j],"Wins !!!")
            print(i,j)
            print(i,j+1)
            print(i,j+2)
            sys.exit()
        else:
            break
'''
'''
"COLUMN"
result = [[gameplay[j][i] for j in range(len(gameplay))] for i in range(len(gameplay[0]))]
print(result)
for i in range(len(result)):
    for j in range(len(result[i])):
         if(result[i][j]==result[i][j+1]==result[i][j+2]):
            print("Wohooo .... ",result[i][j],"Wins !!!")
            print(i,j)
            print(i,j+1)
            print(i,j+2)
            sys.exit()
         else:
            break
'''

