class X:
    def __init__(self):
        pass

    def __repr__(self):
        return "X"
    
    def evaluate(self, value):
        return value

class Int:
    def __init__(self, i):
        self.i = i
    
    def __repr__(self):
        return str(self.i)
    
    def evaluate(self, value):
        return self.i

class Add:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        return repr(self.p1) + " + " + repr(self.p2)
    
    def evaluate(self, value):
        return self.p1.evaluate(value) + self.p2.evaluate(value)

class Mul:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    #checking all 3 instances to be safe
    def __repr__(self):
        repr_p1 = "( " + repr(self.p1) + " )" if isinstance(self.p1, (Add, Sub, Div)) else repr(self.p1)
        repr_p2 = "( " + repr(self.p2) + " )" if isinstance(self.p2, (Add, Sub, Div)) else repr(self.p2)
        return repr_p1 + " * " + repr_p2
    
    def evaluate(self, value):
        return self.p1.evaluate(value) * self.p2.evaluate(value)

class Sub:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        return repr(self.p1) + " - " + repr(self.p2)
    
    def evaluate(self, value):
        return self.p1.evaluate(value) - self.p2.evaluate(value)
    
class Div:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    #checking all 3 instances to be safe
    def __repr__(self):
        repr_p1 = "( " + repr(self.p1) + " )" if isinstance(self.p1, (Add, Sub, Mul)) else repr(self.p1)
        repr_p2 = "( " + repr(self.p2) + " )" if isinstance(self.p2, (Add, Sub, Mul)) else repr(self.p2)
        return repr_p1 + " / " + repr_p2
    
    def evaluate(self, value):
        return self.p1.evaluate(value) / self.p2.evaluate(value)



poly = Add( Add( Int(4), Int(3)), Add( X(), Mul( Int(1), Add( Mul(X(), X()), Int(1)))))
print(poly)