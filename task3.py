from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel

app = QApplication([])
my_win = QWidget()
my_win.resize(500, 500)
btn  = QPushButton("Натисни щоб дізнатися переможця")
line = QVBoxLayout()
text = QLabel("Hello")
number = QLabel("?")
line.addWidget(btn, alignment=Qt.AlignCenter)
line.addWidget(text, alignment=Qt.AlignCenter)
line.addWidget(number, alignment= Qt.AlignCenter)
my_win.setLayout(line)

my_win.show()
app.exec_()