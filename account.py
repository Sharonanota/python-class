class Account:
    def __init__(self,Accntname,Accntnumber,balance, amount):
        self.balance=balance
        self.Accntname = Accntname
        self.Accntnumber = Accntnumber
        self.amount = amount
    
        
    def depost(self):
        
        self.balance += self.amount
        return f"confirmed your new balance is {self.balance}"
    
    def withdrawal(self):
        
        self.amount -= self.balance 
        return f"your new balance is {self.amount}"      