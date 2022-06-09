def selection_sort(arr, N, M):
    for i in range(0, N - 1):

        min_index = i
        for j in range(i + 1, N):
            if arr[j] < arr[min_index]:
                min_index = j
        temp = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = temp

    arrayToText(arr, M)


def arrayToText(arr, n):
    f2 = open("output2.txt", 'w')
    for j in range(0, n):
        f2.write(str(arr[j]) + " ")
    f2.write("\n")
    f2.close()


f = open("input2.txt", 'r')
line = f.readline().split()
N = int(line[0])
M = int(line[1])

line = f.readline()
a = line.split()  # split the string 'line' into a list of string values
array = []
for j in range(0, N):
    array.append(int(a[j]))  # convert the string values into integer values

selection_sort(array, N, M)
