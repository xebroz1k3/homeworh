class Figura():
    def __init__(self, color) :
        self.color = color
    def S_counter(self):
        return 0
    def check_color(self):
        return self.color
    def P_counter(self):
        return 0
    
class Circle(Figura):
    def __init__(self, color, r):
        self.color = color
        self.r = r
    def S_counter(self):
        return 3,14*self.r**2
    def P_counter(self):
        return 2*3,14*self.r
    
class Square(Figura):
    def __init__(self, color, a):
        super().__init__(color)
        self.a=a
    def S_counter(self):
        return self.a**2
    def P_counter(self):
        return self.a*4
    
class Rect(Figura):
    def __init__(self, color, a, b):
        super().__init__(color)
        self.a = a
        self.b = b
    def S_counter(self):
        return self.a*self.b
    def P_counter(self):
        return 2*(self.a+self.b)
circle = Circle('red', 5)
square =Square('green', 6)
rect = Rect('black', 20, 15)
for i in [circle, square, rect]:
    print(i.check_color())
    print(i.S_counter())
    print(i.P_counter())
