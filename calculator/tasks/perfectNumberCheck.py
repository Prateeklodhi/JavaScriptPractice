# number = int(input("Number:"))
for number in range(8200):
    count = 1
    sum = 0
    while(count<number):
        if number % count==0:
            sum+=count
        count+=1

    if sum==number:
        print(f"{number} is perfect number.")
    else:
        print(f"{number} is not perfect number")