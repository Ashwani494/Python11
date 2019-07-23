class Test:
    company_name="HP"
    def msg(self):
        print("Running successfully")
    #constructor--it call automatically when the object is created
    #whose task is to initialize data member
    #__init__ is special method
    def __init__(self):
        self.cpu="core13"
        self.ram=4


    '''def __init__(self):
        print("without parameter")'''


t1=Test()
print(t1.cpu,t1.company_name)
t1.cpu="i7"
t1.company_name="Dell"
print(t1.cpu,t1.company_name)
t2=Test()
print(t2.cpu,t2.company_name)

