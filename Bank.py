class Bank:

    def __init__(self):
        self.cards = {}
    
    # add a card to the bank, with a user defined pin and account name
    def add_card(self, card_number, pin, account_name):
        if card_number not in self.cards:
            self.cards[card_number] = {
                "pin": pin,
                "accounts": {
                    account_name: 0
                }
            }
            return 1, "card successfully added!"
        else:
            return 0, "ERROR: card already exists!"

    ##### ACCOUNT RELATED METHODS #####

    # add an account to an already existing card
    def add_account(self, card_number, account_name):
        if card_number not in self.cards:
            return 0, "ERROR: invalid card number!"
        else:
            if account_name in self.cards[card_number]['accounts']:
                return 0, "ERROR: account with that name already exists. try a different name!"
            else:
                # initialize account balance to zero
                self.cards[card_number]['accounts'][account_name] = 0
                return 1, "account successfully added!"

    # return the dictionary of accounts
    def get_accounts(self, card_number):
        if card_number not in self.cards:
            return 0, "ERROR: invalid card number!"
        else:
            return 1, self.cards[card_number]['accounts']

    ##### PIN RELATED METHODS #####

    # check if the pin matches the card
    def check_pin(self, card_number, pin_attempt):
        if card_number not in self.cards:
            return 0, "ERROR: invalid card number!"
        else:
            if self.cards[card_number]['pin'] != pin_attempt:
                return 0, "ERROR: wrong pin. try again!"
            else:
                return self.cards[card_number]['accounts'], "welcome!"


    ##### money related methods #####

    # return the balance of a specific account
    def get_balance(self, card_number, account_name):
        if account_name not in self.cards[card_number]['accounts']:
            return 0, "ERROR: not a valid account. try a different name!"
        else:
            return self.cards[card_number]['accounts'][account_name], "balance is: " + str(self.cards[card_number]['accounts'][account_name])

    # update the balance of an account, used to withdraw/deposit money
    def update_balance(self, card_number, account_name, amount):
        if card_number not in self.cards:
            return 0, "ERROR: enter valid card number!"
        else:
            if account_name not in self.cards[card_number]['accounts']:
                return 0, "ERROR: not a valid account. try a different name!"
            else:
                self.cards[card_number]['accounts'][account_name] += amount
                return 1, "balance successfully updated!"