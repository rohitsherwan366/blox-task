import random
import time

# Mock functions to simulate bank operations
def send_money(sender_account, receiver_account, amount):
    # Simulating secure communication and authentication
    # ...

    # Simulating two-phase commit
    try:
        # Phase 1: Prepare for the transaction
        # Deduct amount from sender's account
        sender_account.balance -= amount

        # Phase 2: Commit the transaction
        # Transfer amount to receiver's account
        receiver_account.balance += amount

        # Simulating transaction completion
        time.sleep(random.uniform(0.5, 2))

        return True
    except Exception as e:
        # Handle errors and exceptions during the transfer
        print(f"Error occurred during the transfer: {str(e)}")
        return False

# Mock bank account class
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

# Example usage
sender_account = BankAccount("123456", 1000)
receiver_account = BankAccount("987654", 500)

# Transfer money
success = send_money(sender_account, receiver_account, 200)

if success:
    print("Money transfer successful!")
else:
    print("Money transfer failed. Please try again.")
