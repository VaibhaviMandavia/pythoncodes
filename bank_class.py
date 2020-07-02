# creating class, constructor and method

# creating class
class Bank:
 
    # declaring and initializing variables
    account_num = ""
    balance = 0
    min_balance = 0
    pan_num = ""

    # defining constructor
    def __init__(self,acc_num,bal,min_bal,pan):
        # 'self' represents the instance of the class 
        # using the 'self' keyword we can access the attributes and methods of the class
        self.account_num = acc_num
        self.balance = bal
        self.min_balance = min_bal
        self.pan_num = pan


    # defining class method
    def deposit(self,amount):
        self.balance = self.balance + amount

    
