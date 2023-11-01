number = int(input("enter any number:"))
sum = 0
for count in range(number):
    count, sum = sum, count+sum
print(f"sum:{sum}")