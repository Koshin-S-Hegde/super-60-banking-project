import datetime
from typing import Any


class TransactionRecord:
    account_number: int
    amount: float
    transaction_type: Any
    date: datetime.datetime
    to_account: int|None

    def __init__(
            self,
            account_number: int,
            amount: float,
            transaction_type: Any,
            date: datetime.datetime,
            to_account: int|None,
    ) -> None:
        self.account_number = account_number
        self.amount = amount
        self.transaction_type = transaction_type
        self.date = date
        self.to_account = to_account


class TransactionManager:
    __transaction_log: list[TransactionRecord] = []

    @classmethod
    def log_transaction(
            cls,
            account_number: int,
            amount: float,
            transaction_type: Any,
            to_account: int|None = None
    ) -> None:
        cls.__transaction_log.append(TransactionRecord(
            account_number,
            amount,
            transaction_type,
            datetime.datetime.now(),
            to_account
        ))
