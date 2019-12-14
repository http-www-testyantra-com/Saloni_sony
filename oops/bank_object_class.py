class Bank:
    Bank_name="ICICI"
    ROI=14
    MBL="Mumbai"
    def __init__(self,Name,Age,Phno,Email,Bal=0):
        self.Name=Name
        self.Age=Age
        self.Phno=Phno
        self.Email=Email
        self.Bal=Bal
    def deposit(self,amt=0):
        if amt == 0:
            amt = self.get_amount()
        self.Bal+=amt
        self.success()
    def withdraw(self,amt=0):
        if amt==0:
            amt = self.get_amount()
            if amt>self.Bal:
                self.failure()
                print("insufficient mooney")
                return
            self.Bal = self.sub(self.Bal,amt)
            self.success()
    def dispaly(self):
        print(self.Name,self.Age,self.Phno,self.Email,self.Bal)

    def modify(self,Name="",Age=0,Phno=0,Email=""):
        if Name!= "":
            self.Name=Name
        self.success()
    @classmethod
    def change_Bname(cls,new=""):
        if new == "":
            cls.Bank_Name=new
        cls.success()
    @classmethod
    def modify_ROI(cls,new=0):
        if new == 0:
            cls.Bank_Name=new
        cls.success()
    @staticmethod
    def get_ROI():
        new = float(input("enter new roi"))
    @staticmethod
    def failure():
        print("transaction failure")
    @staticmethod
    def get_amount():
        amount=int(input("enter the amount"))
        return amount
    @staticmethod
    def success():
        print("successfully done")
    @staticmethod
    def sub(a,b):
        return a-b
class Bank2(Bank):
    def __init__(self,Name,Age,Phno,Email,Pan,Aadhar,Bal=0,):
        super(Bank2,self).__init__(Name,Age,Phno,Email,Bal=0)
        self.Pan = Pan
        self.Aadhar = Aadhar
    def add_aadhar_pan(self,Pan,Aadhar):
        self.Pan = Pan
        self.Aadhar = Aadhar
    def dispaly(self):
        print(self.Name, self.Age, self.Phno, self.Email,self.Pan,self.Aadhar,self.Bal)


reeta = Bank("reeta",24,10910191019,"reeta@gmail.com",10000)
geeta = Bank("geeta",27,109101979689,"geeta@gmail.com",2000)
reeta.dispaly()
Bank.dispaly(reeta)
# reeta.withdraw()
Bank2.add_aadhar_pan(reeta,"iwgfei7979",2871070)
print(reeta.Aadhar)
print(reeta.Pan)
reeta.dispaly()
sam = Bank2("sam",89,8989898,"sam@jam.com","ldj98989",878676)
Bank2.dispaly(sam)
