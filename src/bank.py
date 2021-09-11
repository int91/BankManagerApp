import person
import bankaccount

class Bank():
    def __init__(self, _name: str, _deposit_min: float, _join_fee: float):
        self.name: str = _name
        self.deposit_min: float = _deposit_min
        self.join_fee: float = _join_fee
        self.total_invault: float = 0
        self.accounts = []

    def add_account(self, _accname, _person: person.Person):
        self.accounts.append(bankaccount.BankAccount(_person.get_name(), _person.get_name(), _person.get_age(), _person.get_gender()))
    
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
