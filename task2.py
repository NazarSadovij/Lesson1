class Title():
    def __init__ (self, text, x, y):
        self.text = text
        self.x = x
        self.y = y
        self.appearance = True
    def print_info(self):
        print (self.text, self.x, self.y)
    
    def hide(self):
        self.appearance = False

    def show(self):
        self.appearance = True
    

text = Title("Press me", 20, 20)
text.print_info()