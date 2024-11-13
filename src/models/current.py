from models.account import Account
from models.privileges import Privilege

class Current(Account):
    def __init__(
            self,
            name: str,
            balance: float,
            registration_number: int,
            website_url: str,
            pin_number: int,
            privilege: Privilege
    ):
        super().__init__(name, balance, pin_number, privilege)
        self.registration_number = registration_number
        self.website_url = website_url
