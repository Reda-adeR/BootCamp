
def sum(x):
    res = 0
    for i in range(1,5):
        xstr = x*i
        res += int(xstr)
    return res

print(sum(input("Enter a number: ")))