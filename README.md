# a simple ATM controller

## This program is composed of four files:

### Bank.py: 
* a bank class, which contains cards that can hold multiple accounts each
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
### ATMController.py: 
* the controller class, which serves as a mediator between the user and the bank
* 
### CashBin.py: 
* a temporary cash bin class that would hold the amount the user wants to deposit, or contain the amount they withdrew

### demo.py: 
* contains the test cases for testing the ATMController

## fork repository:

git clone https://github.com/christinekwon/atm.git

## run program:

python3 demo.py --type standard

switch up the --type arg to run a specific test

* standard: run the standard insert card / validate pin --> select account --> check balance --> deposit money --> withdraw money sequence
* pin: test edge cases regarding the pin
* withdraw: test edge cases regarding withdraw
* account: test edge cases regarding account selection
* all: run all tests