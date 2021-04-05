from Bank import Bank
from ATMController import ATMController
from CashBin import CashBin

import argparse

def cash_bin_to_string(controller):
    return "amount in cash bin: " + str(controller.get_cash_bin_amt())

def print_test_result(val):
    if val: 
        print("TEST PASSED")
    else:
        print("TEST FAILED")

# standard case, demonstrating insert card / validate pin --> select account --> check balance --> deposit money --> withdraw money sequence flow
def standard_test(bank, cash_bin):

    print("\nRUNNING STANDARD TEST")

    card_number = "00000000"
    pin = "1234"
    account_name = "christine0"
    deposit_amt = 500
    withdraw_amt = 300

    controller = ATMController(bank, cash_bin)

    # swipe card with pin
    print("\nswiping card...")
    val, message = controller.insert_card(card_number, pin)
    print(message)
    print_test_result(val)

    # select an account
    print("\nselecting an account...")
    val, message = controller.select_account(account_name)
    print(message)
    print_test_result(val)

    # check account balance
    print("\nchecking the balancing of this account...")
    val, message = controller.check_balance()
    print(message)
    print_test_result(val)

    # depositing money
    print("\ndepositing money into account...")
    # cash_bin.set_amount(deposit_amt)
    controller.update_cash_bin(deposit_amt)
    print(cash_bin_to_string(controller))

    val, message = controller.deposit()
    print(message)
    print_test_result(val)
    val, message = controller.check_balance()
    print(message)
    print(cash_bin_to_string(controller))

    # withdrawing money
    print("\nwithdrawing money from this account...")
    print(cash_bin_to_string(controller))
    val, message = controller.withdraw(withdraw_amt)
    print(message)
    print_test_result(val)
    val, message = controller.check_balance()
    print(message)
    print(cash_bin_to_string(controller))
    print()

# test swiping card with correct and incorrect pins
def pin_test(bank, cash_bin):

    print("\nRUNNING PIN TEST")

    controller = ATMController(bank, cash_bin)
    card_number = "00000000"
    correct_pin = "1234"
    incorrect_pin = "5678"
    account_name = "christine0"

    # check pin validation function with a correct pin
    print("\ninserting card with correct pin...")
    val, message = controller.insert_card(card_number, correct_pin)
    print(message)
    print_test_result(val)

    # check pin validation function with an incorrect pin
    print("\ninserting card with incorrect pin...")
    val, message = controller.insert_card(card_number, incorrect_pin)
    print(message)
    print_test_result(not val)
    print()

# test money withdrawal with valid and invalid amounts
def withdraw_test(bank, cash_bin):

    print("\nRUNNING WITHDRAW TEST")

    controller = ATMController(bank, cash_bin)
    card_number = "00000000"
    pin = "1234"
    acct_name = "christine0"
    withdraw_amt0 = 200
    withdraw_amt1 = 400
    withdraw_amt2 = -200

    print("\nswiping card...")
    val, message = controller.insert_card(card_number, pin)
    print(message)

    # select an account
    print("\nselecting an account...")
    val, message = controller.select_account(acct_name)
    print(message)

    # withdraw a valid amount of moneymoney
    print("\nwithdrawing " + str(withdraw_amt0) + " dollars...")
    print(cash_bin_to_string(controller))
    val, message = controller.withdraw(withdraw_amt0)
    print(message)
    print(cash_bin_to_string(controller))
    print_test_result(val)

    # view balance
    val, message = controller.check_balance()
    print("current account balance: " + str(val) + " dollars")

    # try to withdraw an amount that exceeds the current balance
    print("\nwithdrawing " + str(withdraw_amt1) + " dollars...")
    controller.cash_bin.set_amount(0)
    print(cash_bin_to_string(controller))
    val, message = controller.withdraw(withdraw_amt1)
    print(message)
    print(cash_bin_to_string(controller))
    print_test_result(not val)

    # try to withdraw a negative amount
    print("\nwithdrawing " + str(withdraw_amt2) + " dollars...")
    controller.cash_bin.set_amount(0)
    print(cash_bin_to_string(controller))
    val, message = controller.withdraw(withdraw_amt2)
    print(message)
    print(cash_bin_to_string(controller))
    print_test_result(not val)

    # view balance
    val, message = controller.bank.get_balance(card_number, acct_name)
    print("current account balance: " + str(val) + " dollars")
    print()

# test choosing accounts with wrong and right names
def account_test(bank, cash_bin):
    print("\nRUNNING ACCOUNT TEST")

    controller = ATMController(bank, cash_bin)
    card_number = "00000000"
    pin = "1234"
    acct_name = "christine0"
    wrong_acct_name = "christine2"

    print("\ninserting card...")
    val, message = controller.insert_card(card_number, pin)
    print(message)

    # select an account
    print("\nselecting an account that doesn't exist...")
    val, message = controller.select_account(wrong_acct_name)
    print(message)
    print_test_result(not val)

    print("\nselecting an account that does exist...")
    val, message = controller.select_account(acct_name)
    print(message)
    print_test_result(val)
    print()

def empty_test():
    bank = Bank()
    cash_bin = CashBin()
    controller = ATMController(bank, cash_bin)
    
    card_number = "00000000"
    pin = "1234"
    acct_name = "christine0"

    print("\ninserting card...")
    val, message = controller.insert_card(card_number, pin)
    print(message)
    print_test_result(not val)
    print()

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="add the type of test you wish to run")
    parser.add_argument('--test_type', default='standard', help='options: standard, pin, withdraw, account, empty, all')
    args = parser.parse_args()

    # set up a bank
    print("\ninitializing bank...")
    bank = Bank()

    card_number = "00000000"
    pin = "1234"
    account_name0 = "christine0"
    account_name1 = "christine1"
    cash_bin = CashBin(500)

    # add a card
    val, message = bank.add_card(card_number, pin, account_name0)
    print(message)

    # deposit money
    val, message = bank.update_balance(card_number, account_name0, cash_bin.get_amount())
    cash_bin.set_amount(0)
    print(message)

    # add a second account
    val, message = bank.add_account(card_number, account_name1)
    print(message)

    if args.test_type == 'all':
        standard_test(bank, cash_bin)
        pin_test(bank, cash_bin)
        withdraw_test(bank, cash_bin)

    # standard test
    elif args.test_type == 'standard':
        standard_test(bank, cash_bin)

    # pin test
    elif args.test_type == 'pin':
        pin_test(bank, cash_bin)

    # withdraw test
    elif args.test_type == 'withdraw':
        withdraw_test(bank, cash_bin)

    # account test
    elif args.test_type == 'account':
        account_test(bank, cash_bin)

    # empty bank test
    elif args.test_type == 'empty':
        empty_test()