class Button(object):
    def __init__(self, data, x, y, rW, rH, fill, text=""):
        self.w = data.width//2
        self.x= x
        self.y = y
        self.rW = rW
        self.rH =rH
        self.fill = fill
        self.text = text
        
    def draw(self, canvas):
        x,y,rW, rH = self.x, self.y ,self.rW, self.rH
        canvas.create_rectangle(x-rW, y-rH, x+rW, y+rH, fill=self.fill)
        canvas.create_text(x,y, text=self.text, font="Arial 36 bold")
        
        
    def clickInButton(self, eX, eY):
        x, rW, y, rH = self.x, self.rW, self.y ,self.rH
        if ((x-rW<= eX<=x+rW) and (y-rH<=eY<=y+rH)):
            return True
        return False 
        
class abstract(Button):
    def __init__(self, data, x, y, text):
        super().__init__(data, x,y, rW=data.width//6, rH=30, fill="springgreen", text=text)
        
class blank(Button):
    def __init__(self, data, x, y, text, fill):
        super().__init__(data, x,y, rW=data.width//6, rH=30, fill=fill, text=text)
        

        
        
class No(Button):
    def __init__(self, data, x,y):
        super().__init_(data, x, y,rW=data.width//6, rH=30, fill="springgreen", text="No")
    