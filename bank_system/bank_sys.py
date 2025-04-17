# Banking system with classes

class BankAccount:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self._balance = 0

    @property
    def balance(self):
        return self._balance
    
    def deposit(self, amount):
        if amount <= 0:
            return "Amount must be positive"
        else:
            self._balance += amount
            return "Successfully added!"

    def withdraw(self, amount):
        if amount <= 0:
            return "Amount must be positive"
        elif amount > self._balance:
            return "Innsufficient funds"
        else:
            self._balance -= amount
            return "Successfully withdrawn!"

class BankSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self, name, password):
        if not name in self.accounts:
            self.accounts[name] = BankAccount(name, password)
            return True
        else:
            return False

    def login(self, name, password):
        if name in self.accounts and self.accounts[name].password == password:
            return True
        else:
            return False
        
    def transfer(self, sender, recipient, amount):
        withdraw = sender.withdraw(amount)
        if withdraw == "Amount must be positive" or withdraw == "Innsufficient funds":
            print(withdraw)
        else:
            print(withdraw)
            print(self.accounts[recipient].deposit(amount))

bank = BankSystem()

def main():
    print("*** Welcom To Bank Of America ***")

    while True:
        print("----------------")
        print("1.Log In")
        print("2.Create Account")
        print("3.Exit")
        print("----------------")

        choice = input("Choose one option: ")

        if choice == "1":
            name = input("Write your name: ")
            password = input("Write your password: ")
            account = bank.login(name, password)

            if account:
                handling_account(bank.accounts[name])
            else:
                print("Invalid credentials!")

        elif choice == "2":
            name = input("Write your name: ")
            password = input("Write your password: ")
            account = bank.create_account(name, password)

            if account:
                print("Account created successfully!")
            else:
                print("Account already exists!")

        elif choice == "3":
            print()
            print("Goodbye!")
            print()
            break
        else:
            print("Choose between (1-3)")

def handling_account(account):
    print()
    print(f"*** Welcom To Your Account {account.name.capitalize()}!")
    while True:
        print("----------------")
        print(f"Balance: ${account.balance}")
        print("1.Deposit")
        print("2.Withdraw")
        print("3.Transfer")
        print("4.Log Out")
        print("----------------")

        choice = input("Choose one option: ")

        if choice == "1":
            amount = input("Enter your amount: $")
            try:
                num = float(amount)
                print(account.deposit(num))

            except ValueError:
                print("Invalid input")

        elif choice == "2":
            amount = input("Withdraw amount: $")
            try:
                num = float(amount)
                print(account.withdraw(num))

            except ValueError:
                print("Invalid input")

        elif choice == "3":
            num = 1
            friends = []
            print()
            print("Send to:")
            for friend in bank.accounts:
                if friend == account.name:
                    continue
                else:
                    print(f"{num}.{friend}")
                    num += 1
                    friends.append(friend)
            
            choice = input("Choose a friend by number: ")

            try:
                friend_index = int(choice) - 1
                amount = input("Amount to send: $")
                try:
                    amount = int(amount)
                    recipient = friends[friend_index]
                    bank.transfer(account, recipient, amount)
                

                except ValueError:
                    print("Invalid input")

            except ValueError:
                print("Use numbers only!")


        elif choice == "4":
            print()
            print(f"Have a nice day {account.name.capitalize()}!")
            print()
            break
        else:
            print("Choose between (1-4)")


if __name__ == '__main__':
    main()