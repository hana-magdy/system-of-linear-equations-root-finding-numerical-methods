con=""
string=""
flag=0
n=0
x=[]

def Gaussian_elimination(a):
    global string
    global n
    global x
    n=len(a)
    x = [0 for i in range(n)]
    global flag
    for i in range(n):
        if a[i][i] == 0.0:
            string="Divide by zero detected!"
            f = open("output.txt", "w")
            f.write("Divide by zero detected!")
            f.close()
        for j in range(i + 1, n):
            ratio = a[j][i] / a[i][i]
            for k in range(n + 1):
              a[j][k] = a[j][k] - ratio * a[i][k]
    if(a[n-1][n-1]==0 and a[n-1][n]==0):
        string="infinite number of solutions"
        f = open("output.txt", "w")
        f.write("infinite number of solutions")
        f.close()

    elif(a[n-1][n-1]==0 and a[n-1][n]!=0):
        string="No solutions"
        f = open("output1.txt", "w")
        f.write("No solutions")
        f.close()
        flag=1

    if(flag!=1):
        x[n - 1] = a[n - 1][n] / a[n - 1][n - 1]
        for i in range(n - 2, -1, -1):
            x[i] = a[i][n]
            for j in range(i + 1, n):
                x[i] = x[i] - a[i][j] * x[j]
            x[i] = x[i] / a[i][i]



    return x