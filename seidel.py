import array as arr
import numpy as np
import matplotlib.pyplot as plt
import copy
results=[]
steps=[]
terrors=[]
n=0
string=""
flag=0


def seidel(a, x,ea,it):
   global flag
   global string
   global results
   global steps
   global terrors
   global n

   n = len(a)

   temp = [[0 for i in range(0, n+1)] for i in range(n)]

   for i in range(0, n):
       for j in range(0, n+1):
           temp[i][j] = a[i][j]


   for i in range(n):
       sum = 0
       for j in range(0, n - 1):
        sum += temp[i][j]
       sum -= temp[i][i]
       if temp[i][i] < sum:
        string = "the system of equations don't imply gauss seidel condition.(input matrix is not diagonal dominant)"
        flag=1

       if temp[i][i] == 0.0:
        string = "Division by zero is detected."

        flag=1
        break;
       for j in range(n):
           if i != j and temp[n - 1][n] != 0:

               ratio = temp[j][i] / temp[i][i]
               for k in range(n+1):
                   temp[j][k] = temp[j][k] - ratio * temp[i][k]

   if (temp[n - 1][n - 1] == 0 and temp[n-1][n] == 0):
       string = 'infinite number of solutions'
       flag = 1


   elif (temp[n - 1][n - 1] == 0 and temp[n-1][n] != 0):
       string = 'No solutions'
       flag = 1


   index = 0
   if(flag!=1):
    b = [0 for i in range(n)]
    results = []
    for i in range(0, n):
        b[i] = a[i][n]



    condition=True
    step=0
    results.append(copy.deepcopy(x))
    while condition:
       steps.append(step)
       step += 1
       errors=[]
       flag=0

       for j in range(0, n):

         d = b[j]


         for i in range(0, n):
             if (j != i):
                 d -= a[j][i] * x[i]

         old=x[j]
         for i in range(n):
             if a[i][i] == 0.0:
                 string="Division by zero is detected"
         x[j] = d / a[j][j]
         xaxis = np.linspace(0, 5, 10)
         yaxis = x[j]
         e=abs(old-x[j])/x[j]
         errors.append(e)
       results.append(copy.deepcopy(x))
       terrors.append(copy.deepcopy(errors))
       index+=1
       condition=False
       for k in range(0,n):
           if errors[k] > ea:
            condition=True
            break
       if step > it:
          break


    y = [0 for i in range(0, len(results))]
    xlim = np.linspace(0, step, len(results))

    for i in range(0, n):
        for j in range(0, len(results)):

            y[j] = results[j][i]

        plt.plot(xlim, y, label="x" + str(i))

    plt.legend()
    plt.show(block=False)

    return results,terrors










