class MovingCircle(object):
    def __init__(self, x, y, r, fill):
        self.x = x
        self.y = y
        self.r =r 
        self.fill= fill
        
    def draw(self, canvas):
        x,y,r = self.x, self.y, self.r
        canvas.create_oval(x-r, y-r, x+r, y+r, fill=self.fill)
        
    def clickInButton(self, eX, eY):
        x, r, y = self.x, self.r, self.y 
        if ((x-r<= eX<=x+r) and (y-r<=eY<=y+r)):
            return True
        return False
     
    def move(self, direction):
        self.x+=(5*(direction))
        
    def collide(self, other):
        if ((self.x==other.x) and (self.y==other.y)):
            return True 
        return False
        
class Blue(MovingCircle):
    def __init__(self, x, y):
        super().__init__(x, y, r=50, fill="blue")
        
class Alphabet(MovingCircle):
    def __init__(self, x, y):
        super().__init__(x, y, r=20, fill="pink")
        
    
class Red(MovingCircle):
    def __init__(self, x, y):
        super().__init__(x, y, r=50, fill="red")
    
class Yellow(MovingCircle):
    def __init__(self, x, y):
        super().__init__(x, y, r=50, fill="yellow")
        
class Orange(MovingCircle):
    def __init__(self, x, y):
        super().__init__(x, y, r=50, fill="orange")
 
class Green(MovingCircle):
    def __init__(self, x, y):
        super().__init__(x, y, r=50, fill="green")
        
class Purple(MovingCircle):
    def __init__(self, x, y):
        super().__init__(x, y, r=50, fill="purple")
 
    
   