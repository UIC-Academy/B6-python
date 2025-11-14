import uuid
from datetime import datetime


class Transaction:
    def __init__(
        self,
        account_id: uuid.UUID,
        type: str,
        amount: int,
        status: str,
        datetime: datetime,
    ) -> None:
        self.id = uuid.uuid4()
        self.type = type
        self.account_id = account_id
        self.amount = amount
        self.status = status
        self.datetime = datetime
        
    def to_dict(self):
        return {
            "id": str(self.id),
            "account_id": str(self.account_id),
            "type": self.type,
            "amount": self.amount,
            "status": self.status,
            "created_at": self.datetime
        }

    def __str__(self) -> str:
        return f"Transaction<sender={self.sender_name}, amount={self.amount}>"