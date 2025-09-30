a = int(input("Enter first number"))
b = int(input("Enter second number"))

for i in range(1, a+1):          
    for j in range(1, b+1):        
        print(f"{i * j:2}",end=" ")   
    print()                     
