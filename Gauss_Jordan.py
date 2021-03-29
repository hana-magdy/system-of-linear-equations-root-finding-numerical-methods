# Applying Gauss Jordan Elimination
flag=0
string=""
n=0
x=[]
def Gaussian_jordan(a):
    global n
    global string
    global x
    n=len(a)
    x = [0 for i in range(n)]
    global flag
    for i in range(n):
        if a[i][i] == 0.0:
         string='Divide by zero detected!'

        for j in range(n):
            if i != j and a[n - 1][n - 1] != 0:
              ratio = a[j][i] / a[i][i]
              for k in range(n + 1):
                    a[j][k] = a[j][k] - ratio * a[i][k]

    if (a[n - 1][n - 1] == 0 and a[n - 1][n] == 0):
        string = 'infinite number of solutions'
        flag = 1

    elif (a[n - 1][n - 1] == 0 and a[n - 1][n] != 0):
        string = 'No solutions'
        flag = 1

    if (flag != 1):


      for i in range(n):
        x[i] = a[i][n] / a[i][i]


    return x
