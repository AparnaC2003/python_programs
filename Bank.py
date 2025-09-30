'''
Bank Account Class (OOP)
Question:
Write a Python program to create a class BankAccount that simulates basic banking operations.
Requirements:
The class should have the following attributes:
account_number (int)
name (str)
balance (float, default = 0.0)
The class should include the following methods:
deposit(amount): Adds the specified amount to the account balance.
withdraw(amount): Deducts the specified amount from the balance only if sufficient funds are available; otherwise, display an error message.
display(): Prints the account holder’s name, account number, and current balance.
In the main program:
Create an object of BankAccount.
Perform at least one deposit and one withdrawal operation.
Display the final account details.

eg:
Account Created: 101, Name: Rahul, Balance: 1000.0
Deposit: 500
Withdrawal: 300
Account Details:
Account Number: 101
Account Holder: Rahul
Balance: 1200.0
'''

#anwer

class BankAccount:
    def __init__(self,acc_no,name,balance=0.0):
        self.account_number = acc_no
        self.name = name
        self.balance = balance
    def deposit(self,amount):
        self.balance = self.balance + amount
        print("successful deposit")
    def withdrawal(self,amount):
        if(self.balance<amount):
            print("insuffitient balance....Cannot withdraw money!!!!")
        else:
            self.balance = self.balance - amount
            print("successfull withdrawal")
    def display(self):
        print("Account Number : ",self.account_number)
        print("Name : ",self.name)
        print("Balance : ",self.balance)


print("Account creation :-  ")
ac_no=int(input("enter the account no : "))  
Name=input("enter the name : ")
Balance=float(input("enter the 1st deposit amount : "))

B = BankAccount(ac_no,Name,Balance)
print("For deposit press 1")
print("For withdrawal press 2")
print("For Balance press 3")
print("----------------------------")
flag=int(input())
while flag>=0:
    if flag==1:
        dep=int(input("enter the deposit money : "))
        B.deposit(dep)
        
    elif flag==2:
        wit=int(input("enter the withdrawal money : "))
        B.withdrawal(wit)
    elif flag==3:
        print("------------------------------------------")
        B.display()
    else:
        print("press the correct number.....")

    print("do u want to continue : yes/no")
    goon=input()
    if(goon=="yes"):
        print("For deposit press 1")
        print("For withdrawal press 2")
        print("For Balance press 3")
        flag=int(input())
    else:
        print("Bank transacion successfully completed ....u r logged out....")
        break