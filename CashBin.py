class CashBin:

    def __init__(self, amount=0):
        self.amount = amount

    # return the amount of cash currently in the cash bin
    def get_amount(self):
        return self.amount

    # update the amount of cash in the cash bin
    def set_amount(self, amt):
        self.amount = amt