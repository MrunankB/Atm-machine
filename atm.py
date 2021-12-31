class Atm:
    def __init__(self, pin, card):
        self.pin = pin
        self.card = card
    
    def withdrawal(self, amt):
        new_amt = 50000 - amt
        print('Collect the cash... Your new balance is ', new_amt)

    def check_balance(self):
        print('Your balance is 50,000')

def main():
    card = input("Enter your Card Number: ")
    pin = input("Enter your pin number: ")

    usr = Atm(pin, card)
    choice = input("Enter w for withdrawal and c to check your balance: ")

    if(choice == 'w'):
        amt = int(input("How much do you want to withdraw? "))
        usr.withdrawal(amt)
    elif(choice == 'c'):
        usr.check_balance()

main()
    