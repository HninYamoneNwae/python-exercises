i=0
numbers=[]
while i<6:
    print(f"at the top i is {i}")
    numbers.append(i)
    i=i+1
    print("Numbersnow:",numbers)
    print(f"At the bottom i is {i}")
print("The numbers: ")
for num in numbers:
    print(num)
