class A:
    def __init__(self):
        print("I am class a constructor")

class B:
    def __init__(self):
        print("I am class b constructor")
#methode Rsolution order--from left
class C(B,A):
    def __init__(self):
        super().__init__()
        print("I am class c constructor")

ob= C()