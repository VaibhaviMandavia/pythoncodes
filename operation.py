# collecting two inputs(numbers) from the user and performing the operation of their choice

# collecting two inputs
i = int(input("Enter your first number : "))
j = int(input("Enter your second number : "))
opr = int(input('''Choose from-
                    1. Addition
                    2. Subtraction
                    3. Multiplication
                    4. Division
                    
                your choice(number) : '''))
# checking for conditions
if opr == 1:
    print("The sum of "+str(i)+" and "+str(j)+" is",(i+j))
elif opr == 2:
    print("The difference of "+str(i)+" and "+str(j)+" is",(i-j))
elif opr == 3:
    print("The product of "+str(i)+" and "+str(j)+" is",(i*j))
elif opr == 4:
    print("The quotient of "+str(i)+" and "+str(j)+" is",(i/j))
else: print("invalid option...")
 