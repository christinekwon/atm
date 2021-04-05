# A Simple ATM Controller

## Fork Repository:

git clone https://github.com/christinekwon/atm.git

## Run Tests:

python3 test.py --type standard

switch up the --type arg to run a specific test

* standard: run the standard insert card / validate pin --> select account --> check balance --> deposit money --> withdraw money sequence
* pin: test edge cases regarding the pin
* withdraw: test edge cases regarding withdraw
* account: test edge cases regarding account selection
* all: run all tests

This program is composed of four files:

### ATMController.py: 
* the controller class, which serves as a mediator between the user and the bank
* insert_card method validates card swipe based on the card number and pin number, and returns the associated accounts
* select_account method allows user to select a specific account based on its name
* check_balance method returns the balance of the selected account
* deposit method transfers money in the cash bin to the selected account
* withdraw method transfers money from the selected account to the cash bin

### Bank.py: 
* a bank class, which contains cards that can hold multiple accounts each
* contains methods for adding a card, getting/updating account & balance information, and checking if a pin is correct
* Bank class structure:
  * cards
    * card number
      * pin
      * accounts
        * account name
          * balance
* typical functions return in the form of (value, message)
  * 'value' is 0 if there is an error, and 'message' will specify why
  * for 'get' functions 'value' can be the desired return value, such as an account balance or a list of accounts
  * for functions that do not need to return any specific information, 'value' will be 1 if there is no error

### CashBin.py: 
* a simple cash bin class that holds the amount the user wants to deposit, or contains the amount they withdrew

### demo.py: 
* contains the test cases for testing the ATMController

