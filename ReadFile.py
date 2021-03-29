import re
import numpy as np
import Parse
con=""
string=""
flag=0

def ReadFromFile(fileName):
  fs = open(fileName,'r')
  n = int(fs.readline())
  type = fs.readline()
  type = type.rstrip('\n')
  k=0
  equations = []
  for i in range(0, n):
      equations.append(fs.readline())
  temp=[]
  IntialGuesses=[]
  if type=='seidel'or type=="All":
      temp =fs.read().split(" ")
      IntialGuesses = [int(numeric_string) for numeric_string in temp]
  if type=="All":
      Parse.Parse(equations, "LU",n, [], 0, 0)
      Parse.Parse(equations, "Gaussian-jordan",n, [], 0, 0)
      Parse.Parse(equations, "Gaussian-elimination",n, [], 0, 0)
      Parse.Parse(equations, "seidel", n, IntialGuesses,50,0.00001)
  if type=='seidel':
   Parse.Parse(equations,type,n,IntialGuesses,50,0.00001)








































