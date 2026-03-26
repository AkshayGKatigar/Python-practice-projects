import datetime

class PaymentAccount:

    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.transactions = []

    def add_money(self, amount):
        if amount > 0:
            self.balance += amount

            self.transactions.append(f"{datetime.datetime.now()} - Added: ${amount}")
            print(f"${amount} added succesfully")

        else:
            print("Invalid amount")

    def send_money(self, receiver, amount):
        if amount <= 0:
            print("Invalid amount!")

        elif amount > self.balance:
            print("Insufficient balance")

        else:
            self.balance -= amount
            receiver.balance += amount
            self.transactions.append(f"{datetime.datetime.now()} - Sent: ${amount} to {receiver.name}")

            receiver.transactions.append(f"{datetime.datetime.now()} - Received: ${amount} from {self.name}")

            print(f"${amount} sent to {receiver.name}!")

    def check_balance(self):
        print(f"Current balance: ${self.balance}")

    def show_transactions(self):
        print("\n Transaction History:")

        if not self.transactions:
            print("No transactions yet")

        else:
            for t in self.transactions:
                print(t)

accounts = {}


def create_account():
    name = input("Enter your name:")
    if name in accounts:
        print("Account already exists")

    else:
        accounts[name] = PaymentAccount(name)
        print("Account created succesfully")

def add_money():
    name = input("Enter your name:")

    if name in accounts:
        amount = float(input("Enter your amount to add:"))

        accounts[name].add_money(amount)

    else:
        print("Account not found")

def send_money():
    sender = input("Enter your name:")

    receiver = input("Enter receiver name:")

    if sender in accounts and receiver in accounts:
        amount = float(input("Enter amount to send:"))

        accounts[sender].send_money(accounts[receiver], amount)

    else:
        print("Sender or receiver not found")

def check_balance():
    name = input("Enter your name:")
    if name in accounts:
        accounts[name].check_balance()
    else:
        print("Account not found")


def show_transactions():
    name = input("Enter your name:")
    if name in accounts:
        accounts[name].show_transactions()
    else:
        print("Account not found")

def main():
    while True:

        print("\n======== Payment App =======")

        print("1.Create Account")
        print("2.Add Money")
        print("3.Send Money")
        print("4.Check Balance")
        print("5.Transaction history")
        print("6.Exit")

        choice = input("Choose an option:")

        if choice == "1":
            create_account()

        elif choice == "2":
            add_money()
        
        elif choice == "3":
            send_money()

        elif choice == "4":
             check_balance()
        
        elif choice == "5":
            show_transactions()

        elif choice == "6":
            print("Exiting... Thank you")

            break

        else:

            print("Invalid choice try again.")

if __name__ == "__main__":

    main()
    