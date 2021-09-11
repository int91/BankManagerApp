import bank
import person
import bankregister
import bankprocessor

def main():
    br = bankregister.BankRegisterer()
    bpd = bankprocessor.BankProcessorDeposit()
    bpw = bankprocessor.BankProcessorWithdraw()
    WorldBank = bank.Bank("Neo Bank", 9.99, 24.99)
    mar = person.Person("Markus", 22, "Male", 1999.99)
    br.register(WorldBank, mar)
    bpd.deposit_amount(199.99, WorldBank, mar)
    bpd.deposit_amount(121.54, WorldBank, mar)
    bpd.deposit_amount(89.99, WorldBank, mar)
    bpd.deposit_amount(310.54, WorldBank, mar)
    bpd.deposit_amount(101.39, WorldBank, mar)
    bpd.deposit_amount(67.89, WorldBank, mar)
    bpd.deposit_amount(415.65, WorldBank, mar)
    bpw.withdraw_amount(100.00, WorldBank, mar)
    print(f"Mar's Money Left Over: ${mar.money}")
    pass

if __name__ == '__main__':
    main()