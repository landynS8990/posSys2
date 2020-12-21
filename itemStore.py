from enum import Enum

class PaymentType(Enum):
    Cash = 0
    Debit_Card = 1
    Credit_Card = 2

class ItemCategory(Enum):
    OTHER = 0
    MEAT = 1
    FRUIT = 2
    VEGETABLE = 3
