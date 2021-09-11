import person
import bank
import bankaccount
from abc import ABC, abstractmethod

class BankProcessor(ABC):
    def __init__(self):
        self.account = None

    @abstractmethod
    def check_account(self, _bank: bank.Bank, _person: person.Person):
        for acc in _bank.accounts:
            if (acc.get_name() == _person.get_name()):
                self.account = acc
                return True
        return False

class BankProcessorDeposit(BankProcessor):    
    def deposit_amount(self, _amount_deposit: float, _bank: bank.Bank, _person: person.Person):
        if (self.check_account(_bank, _person) and _person.money >= _amount_deposit):
            _person.pay_money(_amount_deposit)
            self.account.deposit(_amount_deposit)
            _bank.display_account(self.account)
            _bank.calculate_total()

class BankProcessorWithdraw(BankProcessor):    
    def withdraw_amount(self, _amount_withdraw: float, _bank: bank.Bank, _person: person.Person):
        if (self.check_account(_bank, _person) and self.account.get_balance() >= _amount_withdraw):
            self.account.withdraw(_amount_withdraw)
            _person.recieve_money(_amount_withdraw)
            _bank.display_account(self.account)
            _bank.calculate_total()