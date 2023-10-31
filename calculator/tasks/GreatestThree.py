numberOne = int(input("number one:"))
numberTwo = int(input("number two:"))
numberThree = int(input("number three:"))
if numberOne > numberTwo:
    if numberOne > numberThree:
        print(f"{numberOne} is greater then {numberThree} and {numberTwo}")
    else:
        print(f"{numberThree} is greater then {numberOne} and {numberTwo}")
else:
    if numberTwo > numberThree:
        print(f"{numberTwo} is greater then {numberThree} and {numberOne}")
    else:
        print(f"{numberThree} is greater then {numberOne} and {numberTwo}")