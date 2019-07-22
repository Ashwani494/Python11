class Computer:
    def company_name(self):
        print("HP")
    '''
    __init__ is constructor which is invoked automatically
    when the object of class is created
    '''
    def __init__(self):
        print("Mein to run kar gaya")


c = Computer()
c.company_name()
c2= Computer()