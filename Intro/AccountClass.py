

'''def set_name():
    print("Customer name: " + name)


def set_balance(balance=None):
    print("Account balance: " + balance)
'''


class Account_Class:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

       # @staticmethod

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_balance(self, balance):
        self.balance = balance

    def get_balance(self):
        return self.balance

   # def set_name(self, name):
   #      self.name = name
   #
   #  def get_name(self):
   #      return self.name
   #
   #  def set_balance(self, balance):
   #      self.balance = balance
   #
   #  def get_balance(self):
   #      return self.balance

