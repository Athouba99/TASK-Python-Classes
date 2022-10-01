class Wallet:
    def __init__(self, money): #money 
       self.money = money 


    def credit(slef,amount):
       
       self.money =+ amount 
       return credit 

    def debit(self,amount):
       self.mony =- debit
       return debit

default = 0 

wallet = Wallet(6)
wallet = Wallet(default)  # This should default money inside the wallet to 0
print(wallet)


class Person:
    # Implement the code here
   def __init__(self, name,location,money):
    self.name = name 
    self.location = location
    self.wallet =  Wallet(money)

    def moveTo(self,point):
        self.location = point 
        print("you changed your location to {point}")

person = Person("Moh", 5, 50)


class Vendor(Person):
    # implement Vendor!
    def __init__(self,name,range,price,location,money):
        super().__init__(name,location,money)
        self.range = 5 
        self.price = 1

    def sellTo(self,customer, number_of_icecreams):
        self.location = update()
        vendor_money = money
    print("you sold 15")


vendor = Vendor("Abdallah", 3, 6,8,20)


class Customer(person):
    # plan on blue note
    def __init__(self,name,location,money): 
        super().__init__(name,location,money) # for inheritance
        

    def _is_in_range(self,vendor):
        D = vendor.location - self.location # to check the range 
        if D > vender.range:
            return True
        else:
            return False

    def _have_enough_money(self,vendor, number_of_icecreams):
        # check if the customer have money to buy ice cream from the vender 
        # prints the message saying if the customer has enough mony or not    

        if self.waller.money >= vendor.price * number_of_icecreams:
            return True
        else:
            return False 
    

    def request_icecream(self,vendor, number_of_icecreams):
        # checks if the customer is in the venders range and has enough money for the ice cream , there is a requst is sent to the vendor.
        # print a message saying that a request has been done made.  
        if self._is_in_range(vender) and self._have_enough_money(vendor, number_of_icecreams):
            print ("your request has been made")
            return vender.sellTo(self, number_of_icecreams)

customer = Customer("Abdallah", 3, 6)