class Computer:
    def company_name(self):
        print("HP")

    def computer_config(self,ram,cpu,hdd):
        self.ram=ram
        self.cpu=cpu
        self.hdd=hdd
        print("RAM=",self.ram,"CPU=",self.cpu,"HDD=",self.hdd)

c=Computer()
c1=Computer()
print("First Object name and configuration")
c.company_name()
c.computer_config("2GB","I3","2TB")
print("Second Object name and configuration")
c1.company_name()
c1.computer_config("4GB","I7","2TB")
# self is the object of that class
#Computer.company_name(c)