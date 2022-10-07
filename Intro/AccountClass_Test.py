from unittest import TestCase

from Intro.AccountClass import Account_Class

if __name__ == '__main__':
    acct = Account_Class('Essien', 55000)
    acct.set_name("Mmandu")
    print('Customer name: '+acct.get_name())
    print('Account Balance: '+str(acct.get_balance()))

