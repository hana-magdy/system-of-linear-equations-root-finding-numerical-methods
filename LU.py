string=""
x=[]
n=0
flag=0


def LU(A):
    global string
    global flag
    global x
    global n
    n = len(A)
    temp = [[0 for i in range(0, n+1)] for i in range(n)]
    for i in range(0, n):
        for j in range(0, n+1):
            temp[i][j] = A[i][j]

    for i in range(n):
        if temp[i][i] == 0.0:
            string = "Division by zero is detected."
            flag = 1
            break;
        for j in range(n):
            if i != j and temp[n - 1][n] != 0:
                ratio = temp[j][i] / temp[i][i]
                for k in range(n+1):
                    temp[j][k] = temp[j][k] - ratio * temp[i][k]

    if (temp[n - 1][n - 1] == 0 and temp[n - 1][n] == 0):
        string = 'infinite number of solutions'
        flag = 1


    elif (temp[n - 1][n - 1] == 0 and temp[n - 1][n] != 0):
        string = 'No solutions'
        flag = 1


    if flag !=1:
        b = [0 for i in range(n)]
        for i in range(0, n):
                b[i] = A[i][n]


        L = [[0 for i in range(n)] for i in range(n)]
        for i in range(0, n):
            L[i][i] = 1


        U = [[0 for i in range(0, n)] for i in range(n)]
        for i in range(0, n):
            for j in range(0, n):
                U[i][j] = A[i][j]

        for i in range(0, n):
            if U[i][i] == 0.0:
                string="Division by zero is detected"
            for k in range(i + 1, n):

                c = -U[k][i] / float(U[i][i])
                L[k][i] = c * -1
                for j in range(i, n):
                    U[k][j] += c * U[i][j]


        for k in range(i + 1, n):
            U[k][i] = 0

        n = len(L)



        y = [0 for i in range(n)]
        for i in range(0, n, 1):
            y[i] = b[i]
            for k in range(0, i, 1):
                y[i] -= y[k] * L[i][k]



        n = len(U)


        x = [0 for i in range(n)]
        for i in range(n - 1, -1, -1):
            if U[i][i] == 0.0:
                string="Division by zero is detected"
            x[i] = y[i]
            for k in range(n - 1, i, -1):
                j = k - 1
                x[i] -= x[j + 1] * U[i][j + 1]
            x[i] /= U[i][i]


        return x
    else:
        z=[]
        return z