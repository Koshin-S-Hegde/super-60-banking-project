from repositories.account_repository import AccountRepository
from models.privileges import Privilege

class Account:
    def __init__(
            self,
            name: str,
            balance: float,
            pin_number: int,
            privilege: Privilege
    ):
        self.account_number = AccountRepository.generate_account_number()
        self.name = name
        self.balance = balance
        self.pin_number = pin_number
        self.privilege = privilege
        self.is_active = True
        self.closed_date = None
