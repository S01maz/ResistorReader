from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from buttons import ButtonWidget
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ResistorCal")
        self.setMinimumSize(800, 400)
        
        # Palette
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor("#14213d"))
        self.setPalette(palette)

        self.buttons = ButtonWidget()
        
        v_layout = QVBoxLayout()
        v_layout.setSpacing(20)
        
        layout1, layout2, layout3 = self.create_button_layouts()
        v_layout.addLayout(layout1)
        v_layout.addLayout(layout2)
        v_layout.addLayout(layout3)
        
        container = QWidget()
        container.setLayout(v_layout)
        self.setCentralWidget(container)
        
    def create_button_layouts(self):
        # layout b4
        layout1 = QHBoxLayout()
        layout1.setSpacing(10)
        for btn in [self.buttons.btn1, self.buttons.btn2, self.buttons.btn3, self.buttons.btn4]:
            layout1.addWidget(btn)
        layout1.addStretch()
        layout1.addWidget(self.buttons.res4)

        # layout b5
        layout2 = QHBoxLayout()
        layout2.setSpacing(10)
        for btn in [self.buttons.btn5, self.buttons.btn6, self.buttons.btn7, self.buttons.btn8, self.buttons.btn9]:
            layout2.addWidget(btn)
        layout2.addStretch()
        layout2.addWidget(self.buttons.res5)

        # layout b6
        layout3 = QHBoxLayout()
        layout3.setSpacing(10)
        for btn in [self.buttons.btn10, self.buttons.btn11, self.buttons.btn12,
                    self.buttons.btn13, self.buttons.btn14, self.buttons.btn15]:
            layout3.addWidget(btn)
        layout3.addStretch()
        layout3.addWidget(self.buttons.res6)

        return layout1, layout2, layout3
        

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()