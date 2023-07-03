class MyClass:
    def __init__(self, attribute1):
        self.attribute1 = attribute1

    def __hash__(self):
        return hash(self.attribute1)
    
    def __repr__(self) -> str:
        return f'{self.__class__}({self.attribute1})'

obj = MyClass(1)

s = {obj}

obj.attribute1 = 2

s.add(obj)
s.union()
print(s)

print(obj in s)  # Returns False