class Widget:
    def __init__ (self, x, y, text):
        self.x = x
        self.y = y
        self.text = text
    def print_info(self):
        print(self.text)


class Button(Widget):
    def __init__ (self, x, y, text):
        super().__init__(x, y, text)
        self.is_clicked = False

    def click(self):
        is_clicked = True

