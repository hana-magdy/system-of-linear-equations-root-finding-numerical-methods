import re
import numpy as np
import LU as temp
import Gauss_Jordan
import Gaussian_elimination
import seidel
con = ""
string = ""
flag = 0

def Parse(equations,type,n,IntialGuesses,ea,it): # It will read the entire file

  global con
  global a
  global x
  a = np.zeros((n, n + 1))
  x = np.zeros(n)
  k=0
  alphabets = {}
  while k < n:
    con = equations[k]
    con=con.replace(' ','')
    for element in con:
       if element.isalpha():
          alphabets[element] = 0
    k += 1
  j = 0
  for i in alphabets:
          alphabets[i] = j
          j += 1
  k = 0
  while k < n:
      con = equations[k]
      con=con.replace(' ','')
      count=0
      while(count < len(con)):
         if con[count].isalpha() and ((con[count-2].isdigit() == False and con[count-1].isdigit() == False) or (count == 0)):
                con = con[:count] + '1*' + con[count:]
         count += 1
      count = 0
      z = re.findall(r"[+-]?\d+(?:\.\d+)?", con)
      f=0
      for element in con:
          if element.isalpha() and (con[count-2].isdigit() or con[count-1].isdigit()):
              a[k][alphabets[element]]=z[f]
              f += 1
          if count+1 >= len(con) and element.isdigit():
              a[k][n] = -1*float(z[f])
              f += 1
          elif count+1 < len(con) and element.isdigit():
              if con[count + 1] != "*" and con[count + 1] != "." and con[count + 1].isdigit()==False and con[count + 1].isalpha()==False:
                a[k][n] = -1*float(z[f])
                f += 1
          count += 1
      k += 1

  if type == 'LU':
      arr1=temp.LU(a)
      f = open("LU.txt", "w")
      for i in range (0 , len(arr1)):
         f.write(str(arr1[i]))
         f.write(" ")
      f.close()
      return arr1,string
  elif type=="Gaussian-jordan":
      arr2 = Gauss_Jordan.Gaussian_jordan(a)
      f = open("jordan.txt", "w")
      for i in range(0, len(arr2)):
          f.write(str(arr2[i]))
          f.write(" ")
      f.close()


  elif type=='Gaussian-elimination':
      arr3 =Gaussian_elimination.Gaussian_elimination(a)
      f = open("elimination.txt", "w")
      for i in range(0, len(arr3)):
          f.write(str(arr3[i]))
          f.write(" ")
      f.close()

  elif type == 'seidel':
      results=[]
      errors=[]
      seidel.seidel(a,IntialGuesses,ea,it)

      f = open("seidel.txt", "w")
      for i in range(0, len(results)):
          f.write(str(i))
          f.write(" ")
          for j in range (0,len(a)):

              f.write(str(results[i][j]))
              f.write(" ")
          for j in range(0, len(a)):
           if(i>0):
              f.write(str(errors[i-1][j]))
              f.write(" ")
          f.write("\n")
      f.close()

















































