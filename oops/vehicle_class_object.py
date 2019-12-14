class Vehicle:
    vehicle_name = "volkswagen"
    power = "4cv"
    i_amt = 10
    def __init__(self,color,price,number,owner,milage):
        self.color = color
        self.price = price
        self.number = number
        self.owner=owner
        self.milage = milage

    def display(self):
        print(self.color,self.price,self.number,self.owner,self.milage)

    def discount(self,d_amt=0):
        if d_amt == 0:
            d_amt = self.get_damount()
            if d_amt == 0:
                print("sorry no discount")
            if d_amt>self.price:
                self.failure()
                return
            self.price = self.disc(self.price,d_amt)
            self.success()

    def modify(self,color="",price=0,number=0,owner="",milage=0):
        if color!="":
            self.color=color
        if price!=0:
            self.price=price
        if number!=0:
            self.number=number
        if owner!="":
            self.owner=owner
        if milage!=0:
            self.milage=milage
        self.success()


    @staticmethod
    def get_damount():
        d_amount=int(input("enter some discount amount"))
        return d_amount
    @staticmethod
    def failure():
        print("unsuccessfull")

    @staticmethod
    def disc(a, b):
        return a - b

    @staticmethod
    def success():
        print("successfully done")

    @classmethod
    def change_pow(cls, new=""):
        if new == "":
            cls.power = new
        cls.success()



V1=Vehicle("RED",200000,8989,"BINKU",1000)
V1.display()
V1.discount()
V1.display()