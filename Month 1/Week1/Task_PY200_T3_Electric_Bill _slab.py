unit = int (input("Enter the uinit electricity used: "))

bill = 0
fixed_charge = 50 if unit>0 else 0

if unit<=100:
    bill = unit*2

elif unit<=200:
    bill = (100*2) + (unit-100)*3

elif unit<=500:
    bill = (100*2) + (100*3) + (unit-200)*5

else:
    bill = (100*2) + (100*3) + (300)*5 + (unit-500)*8

total_bill = fixed_charge+bill

print(f"Total bill : {total_bill}")