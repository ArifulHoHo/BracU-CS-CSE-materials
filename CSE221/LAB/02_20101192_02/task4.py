def mergeSort(A,):
    if len(A) == 1:
        return
    mid = len(A)//2
    L = A[:mid]
    R = A[mid:]
    mergeSort(L)
    mergeSort(R)
    i = 0
    j = 0
    k = 0
    while i < len(L) and j< len(R):
        if L[i] < R[j]:
            A[k] = L[i]
            i = i+1
        else:
            A[k] = R[j]
            j=j+1
        k=k+1
    if i < len(L):
        A[k] = L[i]
        i = i+1
        k=k+1
    if j < len(R) :
        A[k] = R[j]
        j = j+1
        k=k+1

f = open("input4.txt", 'r')
N = int(f.readline())

line = f.readline()
a = line.split()  # split the string 'line' into a list of string values
array = []
for j in range(0, N):
    array.append(int(a[j]))  # convert the string values into integer values

mergeSort(array)

f2 = open("output4.txt", 'w')
for j in range(0, N):
    f2.write(str(array[j]) + " ")
f2.write("\n")
f2.close()


