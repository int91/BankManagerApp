import person
import bankaccount

class Bank():
    def __init__(self, _name: str, _deposit_min: float, _join_fee: float):
        self.name: str = _name
        self.deposit_min: float = _deposit_min
        self.join_fee: float = _join_fee
        self.total_invault: float = 0
        self.accounts = []

    def calculate_total(self) -> float:
        self.total_invault = 0
        for ac in self.accounts:
            self.total_invault += ac.get_balance()
        return self.total_invault

    def add_account(self, _accname, _person: person.Person):
        self.accounts.append(bankaccount.CheckingAccount(_person.get_name(), _person.get_name(), _person.get_age(), _person.get_gender(), "0123"))
    
    def display_account(self, account):
        accname = account.get_accname()
        name = account.get_name()
        bal = account.get_balance()
        age = account.get_age()
        gen = account.get_gender()
        print(f"Account Name: {accname}")
        print(f"Account Balance: {bal} \n")
        print(f"Holder Name: {name}")
        print(f"Age: {age}")
        print(f"Gender: {gen}")
        

    def get_name(self):
        return self.name
    
    def get_totalvalue(self) -> float: return self.total_invault

