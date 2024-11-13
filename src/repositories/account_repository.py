from models.account import Account

   
class AccountRepository:
    # Class attribute to store all the elements
    accounts: list[Account] = []
    account_counter: int = 1000

    # Method to generate a new account number
    @classmethod
    def generate_account_number(cls):
        cls.account_counter += 1
        return cls.account_counter

    # Method to save Account
    @classmethod
    def save_account(cls, account: Account):
        cls.accounts.append(account)

    # Method to get all accounts
    def get_accounts(self):
        return self.accounts
