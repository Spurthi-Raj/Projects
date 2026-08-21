

class BankAccount():

    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self,amt_deposite):
        if amt_deposite > 0:
            self.balance += amt_deposite
            print(f"INR{amt_deposite} deposited successfully" )
        else:
            print("Invalid deposit amount.")


        
    def withdraw(self,amt_withdraw):
        if amt_withdraw <=0 :
            print("Invalid withdrawal amount.")

        elif amt_withdraw > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amt_withdraw
            print(f"₹{amt_withdraw} withdrawn successfully.")


    def balance_check(self):
        print(f"Current Balance: ₹{self.balance}")


print("Welcome To  Banking System")
name = input("Enter Account Holder Name: ")
acc_no = input("Enter Account Number: ")

bank = BankAccount(acc_no,name)
while True:
    print("\n 1:Deposit")
    print("2:Withdraw")
    print("3:Check Balance")
    print("4:Exit")

    choice = input("Enter your choice: ")


    if choice == "1":
        amount = float(input("Enter deposite amount :"))
        bank.deposit(amount)

    elif choice == "2":
        amount = float(input("Enter withdrawal amount : "))
        bank.withdraw(amount)

    elif choice == "3":
        bank.balance_check()

    elif choice == "4":
        print("Thank you for using the bank system.")
        break

    else:
        print("Invalid choice. Please try again.")

