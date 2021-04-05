from CashBin import CashBin
from Bank import Bank

class ATMController:

    def __init__(self, bank, cash_bin):
        self.bank = bank
        self.cash_bin = cash_bin

        # the following variables do not have values until a card is inserted and verified
        self.card_number = None
        self.accounts = {}
        self.selected_acct = None

    # when the card is inserted, determine if the card number and corresponding pin number are valid
    def insert_card(self, card_number, pin_attempt):
        val, message = self.bank.check_pin(card_number, pin_attempt)
        if val:
            self.card_number = card_number
            self.accounts = val
            return 1, "welcome back! here are your available accounts: \n" + str(list(self.accounts.keys())) + "\nplease select the account you wish to use."
        else:
            return 0, message

    # update contents of cash bin with specified dollar amount
    def update_cash_bin(self, amount):
        self.cash_bin.set_amount(amount)
    
    # return the amount currently in the cash bin
    def get_cash_bin_amt(self):
        return self.cash_bin.get_amount()
        
    # based on the user input, select an account and save it to a variable
    def select_account(self, account_name):
        if account_name in self.accounts:
            self.selected_acct = account_name
            return 1, "selected account: " + str(self.selected_acct)
        else:
            return 0, "ERROR: enter a valid account name!"

    # check the balance of the account that the user has currently selected
    def check_balance(self):
        if not self.select_account:
            return 0, "ERROR: select an account first!"
        else:
            return self.accounts[self.selected_acct], "balance of account " + str(self.selected_acct) + ": " + str(self.accounts[self.selected_acct])
    
    # deposit the amount in the cash bin to the currently selected account
    def deposit(self):
        deposit_amt = self.cash_bin.get_amount()
        if not self.selected_acct:
            return 0, "ERROR: select an account first!"
        else:
            self.bank.update_balance(self.card_number, self.selected_acct, deposit_amt)
            self.update_cash_bin(0)
            return 1, "successfully deposited " + str(deposit_amt) + " dollars to account " + str(self.selected_acct) + "."

    # with draw a specified amout of money from the currently selected account, 
    # and place into the cash bin
    def withdraw(self, amount):
        if not self.selected_acct:
            return 0, "ERROR: select an account first!"
        elif amount <= 0:
            return 0, "ERROR: enter a valid amount to withdraw!"
        else:
            val, message = self.bank.update_balance(self.card_number, self.selected_acct, -amount)
            if val:
                self.update_cash_bin(amount)
                return 1, "successfully withdrew " + str(amount) + " dollars from account " + str(self.selected_acct) + ". please check the cash bin."
            else:
                return 0, message

    # return the list of accounts pertaining to the current card user
    def get_accounts(self):
        return self.accounts

    # once the user is finished, allow them to 'log out' by initializing the card/account information in the atm
    def log_out(self):
        self.card_number = None
        self.accounts = {}
        self.selected_acct = None