'''
instance variable--variable declared inside method
'''


class Car:
    wheel=4   # class varaible or static variable
    def carinfo(self,speed,mil):
        self.speed=speed
        self.mil=mil
        #self.noofgear=noofgear

        print("Speed=",self.speed,"milage=",self.mil)

    def __init__(self):
        self.head=2
        print("headlight=",self.head)

maruti=Car()
maruti.head=4
maruti.wheel=5
#maruti.noofgear=6
print("Wheel=",maruti.wheel,maruti.head)
maruti.carinfo(220,18)
toyta=Car()
print("Wheel=",toyta.wheel,toyta.head)
toyta.carinfo(300,40)
