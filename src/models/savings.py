import datetime
from models.account import Account
from models.privileges import Privilege

class Savings(Account):
    def __init__(
            self,
            name: str,
            balance: float,
            date_of_birth: datetime.datetime,
            gender: str,
            pin_number: int,
            privilege: Privilege
    ):
        super().__init__(name, balance, pin_number, privilege)
        self.date_of_birth = date_of_birth
        self.gender = gender
