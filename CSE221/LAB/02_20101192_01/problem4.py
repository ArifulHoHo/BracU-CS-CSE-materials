f = open("input4.txt", 'r')
matrix_A = []
matrix_B = []

N = int(f.readline())
matrix_C = []

for i in range(0,N):
    matrix_C.append([0]*N)


# Creating matrix A by reading input from text file
for i in range(0, N):
    line = f.readline()
    a = line.split()        # split the string 'line' into a list of string values
    b = []
    for j in range(0,N):
        b.append(int(a[j])) # convert the string values into integer values
    matrix_A.append(b)

line = f.readline()
# Creating matrix B by reading input from text file
for i in range(0, N):
    line = f.readline()
    a = line.split()
    b = []
    for j in range(0, N):
        b.append(int(a[j]))
    matrix_B.append(b)

f.close()
print(N)
print(matrix_B)
print(matrix_A)
for i in range(0, N):
    for j in range(0, N):
        for k in range(0, N):
            matrix_C[i][j] += matrix_A[i][k] * matrix_B[k][j]
        print(matrix_C)

f2 = open("output4.txt",'w')
for i in range(0,N):
    for j in range(0,N):
        integer = str(matrix_C[i][j])
        f2.write(integer+" ")
    f2.write("\n")

f2.close()

