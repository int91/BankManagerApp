import person
import bank

class BankRegisterer():

    def canregister(self, _bank: bank.Bank, _person: person.Person) -> bool:
        return _person.money >= _bank.join_fee

    def register(self, _bank: bank.Bank, _person: person.Person):
        if self.canregister(_bank, _person):
            _person.money -= _bank.join_fee
            _bank.add_account(_person.get_name(), _person)