class Account:
    def get_User_Info(self):
        print("User Data")

class Saving(Account):
    def intrest(self):
        print("Interest milega")

class Current(Account):
    def nointerest(self):
        print("kuch byaj nahi milega")

s= Saving()
s.get_User_Info()
s.intrest()

c=Current()
c.get_User_Info()
c.nointerest()