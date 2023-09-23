class Button():
    def __init__(self, title, x, y):
        self.title = title
        self.x = x
        self.y = y
        self.appearance = True
    def hide(self):
        self.appearance = False

    def show(self):
        self.appearance = True
        

btn1 = Button("Press me", 20, 20)
btn1.hide()
print(btn1.appearance)    