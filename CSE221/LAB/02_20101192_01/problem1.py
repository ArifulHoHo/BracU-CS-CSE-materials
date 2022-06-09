def isPalindrome(text):
    result = "False"
    x = 0
    y = len(text) - 1
    while x < y:
        if text[x] != text[y]:
            result = "False"
            break
        else:
            result = "True"
        x += 1
        y -= 1
    return result


def isParity(n):
    try:
        int(n)
    except:
        return "None"
    if int(n) % 2 == 0:
        return "even"
    else:
        return "odd"


def percentage(n):
    return str(int((n / 5) * 100))


f = open("input.txt", "r")
f2 = open("output.txt", "w")
f3 = open("record.txt", 'w')
parity_array = []
palindrome_array = []

string = f.readline()

while string != "":

    arry = string.split()
    parity = isParity(arry[0])
    palindrome = isPalindrome(arry[1])
    parity_array.append(parity)
    palindrome_array.append(palindrome)
    if parity == "None":
        if palindrome == "True":
            output = arry[0] + " cannot have parity and " + arry[1] + " is a palindrome."
        else:
            output = arry[0] + " cannot have parity and " + arry[1] + " is not a palindrome."
    elif palindrome == "True":
        output = arry[0] + " has " + parity + " parity and " + arry[1] + " is a palindrome."
    else:
        output = arry[0] + " has " + parity + " parity and " + arry[1] + " is not a palindrome."
    f2.write(output + "\n")
    string = f.readline()

odd_count = parity_array.count("odd")
f3.write("Percentage of odd parity: " + percentage(odd_count) + "%\n")

even_count = parity_array.count("even")
f3.write("Percentage of even parity: " + percentage(even_count) + "%\n")

f3.write("Percentage of no parity: " + percentage(5 - even_count - odd_count) + "%\n")

palindrome_count = palindrome_array.count("True")
f3.write("Percentage of palindrome: " + percentage(palindrome_count) + "%\n")

f3.write("Percentage of non-palindrome: " + percentage(5 - palindrome_count) + "%\n")

f2.close()
f.close()
f3.close()
