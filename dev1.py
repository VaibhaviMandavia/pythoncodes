from bank_class import Bank

# creating an object for Bank class and passing arguments to its constructor
c1 = Bank("c1",1000,100,"p1")
c2 = Bank("a2",10000,10,"p2")

# accessing variables and methods through objects

# calling deposit function through object c1 and passing arguments
c1.deposit(100)

print("your balance is:",c1.balance)