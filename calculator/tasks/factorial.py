number = int(input("number: "))
factorial = 1
for i in range(1,number+1):
    factorial *= i

print(f"factorial of {number} is : {factorial}")                        