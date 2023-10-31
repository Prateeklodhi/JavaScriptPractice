gross_salary = float(input("please enter your gross salary: "))
deduction = float(input("please enter your deduction in salary: "))
tax_rate = float(input("please enter tax rate: "))
tax_rebate = float(input("please enter tax rebate:. "))
taxable_income = gross_salary - deduction
tax = (taxable_income * tax_rate/100) - (tax_rebate/100)
print(f"payable tax ammount is {tax}")