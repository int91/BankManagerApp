
class Person:
    def __init__(self, _name: str, _age: int, _gender: str, _money: float):
        self.name: str = _name
        self.age: int = _age
        self.gender: str = _gender
        self.money: float = _money

    def get_name(self) -> str: return self.name
    def get_age(self) -> int: return self.age
    def get_gender(self) -> str: return self.gender

    def pay_money(self, pay_amount) -> float: self.money -= pay_amount
    def recieve_money(self, rec_amount) -> float: self.money += rec_amount