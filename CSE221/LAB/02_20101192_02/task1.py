def bubbleSort(arr,n):
    for i in range(n):

        swaps = 0
        for j in range(n - i - 1 ):

            if arr[j] > arr[j + 1]:
                arr[j + 1], arr[j] = arr[j ], arr[j+1]
                swaps += 1
        if swaps == 0:
            return arr
    return arr

# Instead of traversing the entire array multiple times which gives us a time complexity of θ(n^2),
# We now check if any swaps have been made in each iteration. If at any time after the j loop ends and we see that
# no swaps have been made, the program ends there because the array is already sorted. Hence if we assume
# that the base case scenario is when an array is already sorted or nearly sorted, the bubble sort
# checks the number of swaps and ends when swaps made is zero, making the sorting algorithm much faster.

f = open("input1.txt", 'r')
N = int(f.readline())

line = f.readline()
a = line.split()        # split the string 'line' into a list of string values
array = []
for j in range(0,N):
    array.append(int(a[j])) # convert the string values into integer values

bubbleSort(array,N)

f2 = open("output1.txt",'w')
for j in range(0, N):
    f2.write(str(array[j])+" ")
f2.write("\n")
f2.close()
