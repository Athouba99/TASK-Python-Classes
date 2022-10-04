
class Wallet: # class 
    def __init__(self, money): #money,constructor function  
       self.money = money #propty 

    # def __str__(self):
    #     return f"this wallet has {self.money}"

    def credit(self,amount):       
       self.money += amount 
    #    print (f"the new amount of money if is {self.money}")
    #    return credit 

    def debit(self,amount):
       self.money -= amount
    #    return debit

# default = 0 
# wallet = Wallet(6)
# wallet = Wallet(default)  # This should be the default money inside the wallet to 0
# print(wallet)


class Person:
    # Implement the code here
   def __init__(self, name,location,money):
    self.name = name 
    self.location = location
    self.wallet =  Wallet(money)

    def moveTo(self,point):
        self.location = point 
        # print("you changed your location to {point}")

# person = Person("Moh", 5, 50)


class Vendor(Person):
    # implement Vendor!
    def __init__(self,name,range,price,location,money):
        super().__init__(name,location,money)
        self.range = 5 
        self.price = 1

    def sellTo(self,customer, number_of_icecreams):
        self.location = customer.location 
        self.wallet.credit(number_of_icecreams * self.price)
        customer.wallet.debit(number_of_icecreams * self.price)

    # print("you sold 15")


# vendor = Vendor("Abdallah", 3, 6,8,20)


class Customer(Person):
    # plan on blue note
    def __init__(self,name,location,money): 
        super().__init__(name,location,money) # for inheritance
        

    def _is_in_range(self,vendor):
        D = abs(self.location - vendor.location)   # to check the range 
        if D >= vendor.range:
            print (f"this vendor {vendor.name} is within {self.name} range")
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
        if self._is_in_range(vendor) and self._have_enough_money(vendor, number_of_icecreams):
            # print ("your request has been made,thank you ")
            vendor.sellTo(self, number_of_icecreams)

# customer = Customer("Abdallah", 3, 6)

# Vendor_x = Vendor("Saja",4,2) # making new vendor with location and money amount

nearby_customer = Customer("Lulu",3,16) #making new customer with location and money amount

distant_customer = Customer ("Sarah", 20, 3) # making new customer with location and money amount 

broke_customer = Customer("Ali", 1, 27)

