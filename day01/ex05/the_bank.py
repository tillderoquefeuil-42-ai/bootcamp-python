
class Account(object):
    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name
        self.value = 0
        self.__dict__.update(kwargs)

        if hasattr(self, 'value'):
            self.value = 0
        Account.ID_COUNT += 1

    def transfer(self, amount):
        self.value += amount

class Bank(object):
    '''The bank'''

    def __init__(self):
        self.account = []

    def __isAccountType(self, account):
        if not type(account) is Account:
            raise TypeError('account object is not of type -Account-')
        return True

    def __accountHasEnoughMoney(self, account, amount):
        if account.value < amount:
            return False
        return True

    def __accountIsNotCorrupted(self, account):
        attributs = account.__dict__
        # even number of attributes
        if len(attributs) % 2 == 0:
            return False

        # attribute starting with b
        # no attribute starting with zip or addr
        for x in attributs.keys():
            test_b = x[:1]
            test_z = x[:3]
            test_a = x[:4]

            if test_b == 'b':
                return False
            if test_z == 'zip':
                return False
            if test_a == 'addr':
                return False

        # no attribut name, id and value.
        if not 'name' in attributs or not 'id' in attributs or not 'value' in attributs:
            return False
    
        return True

    def __checkAccountIntegrity(self, account):
        self.__isAccountType(account)
        if not self.__accountIsNotCorrupted(account):
            return False
        return True

    def __getAccountById(self, id):
        for x in self.account:
            if x.id == id:
                return x
        return None

    def __getAccountByName(self, name):
        for x in self.account:
            if x.name == name:
                return x
        return None

    def __getAccount(self, arg):
        account = None

        if type(arg) is int:
            account = self.__getAccountById(arg)
        elif type(arg) is str:
            account = self.__getAccountByName(arg)
        return account

    def add(self, account):
        self.__isAccountType(account)
        self.account.append(account)

    def transfer(self, origin, dest, amount):
        '''
            @origin:  int(id) or str(name) of the first account
            @dest:    int(id) or str(name) of the destination account
            @amount:  float(amount) amount to transfer
            @return         True if success, False if an error occured
        '''

        a1 = self.__getAccount(origin)
        a2 = self.__getAccount(dest)

        if  amount < 0:
            return False
        if  not self.__checkAccountIntegrity(a1) or not self.__accountHasEnoughMoney(a1, amount):
            return False
        if  not self.__checkAccountIntegrity(a2):
            return False

        a1.transfer(amount * -1)
        a2.transfer(amount)
        return True


    def fix_account(self, account):
        '''
            fix the corrupted account
            @account: int(id) or str(name) of the account
            @return         True if success, False if an error occured
        '''
        
        a = self.__getAccount(account)

        valid = ['name', 'id', 'value']
        attributs = a.__dict__.keys()
        
        todelete = []
        for x in attributs:
            if not x in valid:
                todelete.append(x)
        for y in todelete:
            delattr(a, y)

        return self.__checkAccountIntegrity(a)





a1 = Account("slim")
a2 = Account("shady")
a3 = Account("chikachika")
a3.wtf = "HEY"

a1.transfer(1000)
a2.transfer(2000)

b = Bank()

b.add(a1)
b.add(a2)
b.add(a3)

print("Transfer between a1 and a2")
result1 = b.transfer(a1.id, a2.name, 200)
print(result1)


print("Fixing a3")
result2 = b.fix_account(a3.name)
print(result2)
