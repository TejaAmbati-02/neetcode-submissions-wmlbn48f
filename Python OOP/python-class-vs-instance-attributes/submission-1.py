class BankAccount: 
    # TODO: Add class and instance attributes at their appropriate places
    total_accounts = 0
    
    def __init__(self, name, balance) -> None:
        self.name = name
        self.balance = balance
        BankAccount.total_accounts +=1

alice_account = BankAccount("Alice", 1000)
bob_account = BankAccount("Bob", 2000)

print(f"{alice_account.name}'s balance: {alice_account.balance}")
print(f"{bob_account.name}'s balance: {bob_account.balance}")

print(f"Total Accounts: {BankAccount.total_accounts}")