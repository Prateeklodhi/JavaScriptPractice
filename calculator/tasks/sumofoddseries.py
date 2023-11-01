number = int(input("enter any number:"))
sum = 0
for count in range(number):
    if count%2!=0:
        count, sum = sum, count+sum
print(f"sum:{sum}")