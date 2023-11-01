number = int(input("enter any number:"))
prime = 2
flag=1
if number==2:
    print(f"this {number} is prime")
elif number==1:
    print(f"this {number} is prime")
elif number==3:
    print(f"this {number} is prime")
else:
    while(prime < number):
        if number%prime == 0:
            flag = 0
            break;
        prime+=1
    if flag==1:
        print(f"this {number} is prime")
    else:
        print(f"this {number} is not prime")
