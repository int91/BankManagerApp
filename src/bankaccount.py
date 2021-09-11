
class BankAccount:
    def __init__(self, _accname: str, _name: str, _age: int, _gender: str):
        self.accname: str = _accname
        self.name: str = _name
        self.age: int = _age
        self.gender: str = _gender
        self.balance: float = 0
    
    def deposit(self, _amount) -> float: self.balance += _amount
    def withdraw(self, _amount) -> float: self.balance -= _amount
    def get_name(self) -> str: return self.name
    def get_accname(self) -> str: return self.name
    def get_age(self) -> int: return self.age
    def get_gender(self) -> str: return self.gender
    def get_balance(self) -> float: return self.balance