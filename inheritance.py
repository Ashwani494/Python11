'''
Deriving a new class from the base class is known as inheritance
types of inheritance:
1. single level inheritance
2. multilevel inheritance
3. hierarchical inheritance
4.multiple inheritance
5.hybrid inheritance

It provides the code resuability.
'''


#room is base class or parent class

class Room:
    def get_room_dimension(self,l,b):
        self.l=l
        self.b=b

    def calarea(self):
        print("area=",self.l*self.b)


# guestroom is derived class or child class
class GuestRoom(Room):

    def roomtype(self):
        print("Guest Room")


'''r1=Room()
r1.get_room_dimension(20,30)
r1.calarea()'''

r2 = GuestRoom()
r2.get_room_dimension(20, 299)
r2.calarea()
r2.roomtype()