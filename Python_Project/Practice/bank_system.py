from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, name, account_number, pin, balance=0):
        self.name = name
        self.account_number = account_number
        self.__pin = pin
        self._balance = balance

    def validate_pin(self, pin):
        return self.__pin == pin

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount
        print(f"✅ Deposited ₹{amount}")

    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("❌ Insufficient balance")
        self._balance -= amount
        print(f"✅ Withdrawn ₹{amount}")

    def get_balance(self):
        return self._balance

    @abstractmethod
    def calculate_interest(self):
        pass


class SavingsAccount(Account):
    INTEREST_RATE = 0.04

    def calculate_interest(self):
        interest = self._balance * self.INTEREST_RATE
        self._balance += interest
        print(f"💰 Interest added: ₹{interest}")


class CurrentAccount(Account):
    def calculate_interest(self):
        print("⚠ No interest for Current Account")


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_type, name, pin):
        acc_no = len(self.accounts) + 1001
        if account_type == "savings":
            account = SavingsAccount(name, acc_no, pin)
        else:
            account = CurrentAccount(name, acc_no, pin)

        self.accounts[acc_no] = account
        print(f"🎉 Account created successfully. Account No: {acc_no}")

    def login(self, acc_no, pin):
        account = self.accounts.get(acc_no)
        if not account or not account.validate_pin(pin):
            raise ValueError("❌ Invalid Account Number or PIN")
        return account


def main():
    bank = Bank()

    while True:
        print("\n====== BANK MENU ======")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter choice: ")

        try:
            if choice == "1":
                name = input("Enter Name: ")
                acc_type = input("Account Type (savings/current): ").lower()
                pin = int(input("Set 4-digit PIN: "))
                bank.create_account(acc_type, name, pin)

            elif choice == "2":
                acc_no = int(input("Enter Account Number: "))
                pin = int(input("Enter PIN: "))
                account = bank.login(acc_no, pin)

                while True:
                    print("\n--- Account Menu ---")
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. Balance")
                    print("4. Calculate Interest")
                    print("5. Logout")

                    opt = input("Choose option: ")

                    if opt == "1":
                        amt = float(input("Enter amount: "))
                        account.deposit(amt)

                    elif opt == "2":
                        amt = float(input("Enter amount: "))
                        account.withdraw(amt)

                    elif opt == "3":
                        print(f"💳 Balance: ₹{account.get_balance()}")

                    elif opt == "4":
                        account.calculate_interest()

                    elif opt == "5":
                        print("👋 Logged out")
                        break

            elif choice == "3":
                print("🙏 Thank you for using Bank System")
                break

            else:
                print("❌ Invalid choice")

        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()
