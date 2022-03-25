#oop style
class customer:
    def __init__(self, name, phone, address, balance, email, password, id = None):
        self.name = name
        self.phone = phone
        self.address = address
        self.balance = balance
        self.email = email
        self.password = password
        self.id = id

    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name

    def getPhone(self):
        return self.phone
    def setPhone(self, phone):
        self.phone = phone

    def getAddress(self):
        return self.address
    def setAddress(self, address):
        self.address = address

    def getBalance(self):
        return self.balance
    def setBalance(self, balance):
        self.balance = balance

    def getId(self):
        return self.id
    def setId(self, id):
        self.id = id

    def getEmail(self):
        return self.email
    def setEmail(self, email):
        self.email = email

    def getPassword(self):
        return self.password
    def setPassword(self, password):
        self.password = password

    def toString(self):
        return "fullName:" + self.name + ", " + \
            "phone:" + self.phone + ", " + \
            "address:" + self.address + ", " + \
            "balance:" + str(self.balance) + ", " + \
            "email:" + self.email + ", " + \
            "password:" + self.password 
