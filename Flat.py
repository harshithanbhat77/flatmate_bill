class Bill:
    """
    Object that contains the data about a bill,
    such as total amount and period of the bill
    """
    def __init__(self, amount, period):
        self.amount = amount
        self.period = period

class Flatmate:
    """
    Creates a flatmate person who lives in the flat
    and pys a share of the bill
    """
    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate2):
        weight =  self.days_in_house/(self.days_in_house +flatmate2.days_in_house)
        pays_to = bill.amount * weight
        return  pays_to
