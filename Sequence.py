#Without using any string methods, try to print the following:
#123....n
n=int(input("Enter an integer: "))
if 1 <= n <= 150:
    for i in range(1, n+1):
        print(i, end="")
else:
    print("Number is out of range. It should be between 1 and 150.")


