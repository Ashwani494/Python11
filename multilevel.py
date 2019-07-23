class X:
    def data(self):
        print("mein x class ka hoon")

class Y(X):
    def msg(self):
        print("mein Y class ka hoon")

class Z(Y):
    def sbkuch(self):
        print("mein Z class ka hoon")

r=Z()
r.data()
r.msg()
r.sbkuch()
