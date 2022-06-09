def arrayToText(arr, n):
    f2 = open("output3.txt", 'w')
    for j in range(0, n):
        f2.write(str(arr[j]) + " ")
    f2.write("\n")
    f2.close()


def insertionSort(A,B,N):

    for i in range(0,len(A)-1):
        temp = A[i+1]
        temp1 = B[i+1]
        j = i
        while j >= 0:
            if A[j] < temp:
                A[j+1] = A[j]
                B[j+1] = B[j]
                j = j - 1
            else:

                break
        A[j+1] = temp
        B[j+1] = temp1

    arrayToText(B,N)

f = open("input3.txt", 'r')
N = int(f.readline())

Id = f.readline().split()

line = f.readline()
a = line.split()  # split the string 'line' into a list of string values
marks = []
for j in range(0, N):
    marks.append(int(a[j]))  # convert the string values into integer values

insertionSort(marks,Id,N)

