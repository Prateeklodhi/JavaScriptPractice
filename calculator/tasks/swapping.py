numberOne = int(input("number one:"))
numberTwo = int(input("number two:"))
# with three variables
temp = numberOne
numberOne = numberTwo
numberTwo = temp
print(f"Number one:{numberOne} and Number Two:{numberTwo}")
# without two variables
numberOne = numberOne - numberTwo
numberTwo = numberOne + numberTwo
numberOne = numberTwo - numberOne
print(f"Number one:{numberOne} and Number Two:{numberTwo}")