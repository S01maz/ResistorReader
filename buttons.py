from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtWidgets import *
from colorsDic import Colors

class ButtonWidget(QWidget):
    def __init__(self, parent =None):
        super().__init__()
        
        self.color = Colors()
        palette = QPalette()
        self.setStyleSheet("""QComboBox {color:black;}""")
        # Buttons
        # 4 bound
        self.res4 = QLineEdit()
        self.res4.setReadOnly(True)
        self.res4.setFixedSize(200,20)
        self.b4 = []
        
        self.btn1 = QComboBox()
        self.btn1.setPlaceholderText("select a color")
        self.btn1.setFixedSize(120, 20)
        self.btn1.addItems(self.color.color_val.keys())
        self.btn1.currentIndexChanged.connect(lambda: self.update_color(self.btn1))
        self.btn1.currentIndexChanged.connect(self.cal4)
        self.b4.append(self.btn1)

        self.btn2 = QComboBox()
        self.btn2.setPlaceholderText("select a color")
        self.btn2.setFixedSize(120, 20)
        self.btn2.addItems(self.color.color_val.keys())
        self.btn2.currentIndexChanged.connect(lambda: self.update_color(self.btn2))
        self.btn2.currentIndexChanged.connect(self.cal4)
        self.b4.append(self.btn2)

        self.btn3 = QComboBox()
        self.btn3.setPlaceholderText("select a color")
        self.btn3.setFixedSize(120, 20)
        self.btn3.addItems(self.color.color_coe.keys())
        self.btn3.currentIndexChanged.connect(lambda: self.update_color(self.btn3))
        self.btn3.currentIndexChanged.connect(self.cal4)
        self.b4.append(self.btn3)

        self.btn4 = QComboBox()
        self.btn4.setPlaceholderText("select a color")
        self.btn4.setFixedSize(120, 20)
        self.btn4.addItems(self.color.color_tol.keys())
        self.btn4.currentIndexChanged.connect(lambda: self.update_color(self.btn4))
        self.btn4.currentIndexChanged.connect(self.cal4)
        self.b4.append(self.btn4)
        
        # 5 bound
        self.res5 = QLineEdit()
        self.res5.setReadOnly(True)
        self.res5.setFixedSize(200,20)
        self.b5 = []

        self.btn5 = QComboBox()
        self.btn5.setPlaceholderText("select a color")
        self.btn5.setFixedSize(120, 20)
        self.btn5.currentIndexChanged.connect(lambda: self.update_color(self.btn5))
        self.btn5.addItems(self.color.color_val.keys())
        self.btn5.currentIndexChanged.connect(self.cal5)
        self.b5.append(self.btn5)

        self.btn6 = QComboBox()
        self.btn6.setPlaceholderText("select a color")
        self.btn6.setFixedSize(120, 20)
        self.btn6.currentIndexChanged.connect(lambda: self.update_color(self.btn6))
        self.btn6.addItems(self.color.color_val.keys())
        self.btn6.currentIndexChanged.connect(self.cal5)
        self.b5.append(self.btn6)

        self.btn7 = QComboBox()
        self.btn7.setPlaceholderText("select a color")
        self.btn7.setFixedSize(120, 20)
        self.btn7.currentIndexChanged.connect(lambda: self.update_color(self.btn7))
        self.btn7.addItems(self.color.color_val.keys())
        self.btn7.currentIndexChanged.connect(self.cal5)
        self.b5.append(self.btn7)

        self.btn8 = QComboBox()
        self.btn8.setPlaceholderText("select a color")
        self.btn8.setFixedSize(120, 20)
        self.btn8.currentIndexChanged.connect(lambda: self.update_color(self.btn8))
        self.btn8.addItems(self.color.color_coe.keys())
        self.btn8.currentIndexChanged.connect(self.cal5)
        self.b5.append(self.btn8)

        self.btn9 = QComboBox()
        self.btn9.setPlaceholderText("select a color")
        self.btn9.setFixedSize(120, 20)
        self.btn9.currentIndexChanged.connect(lambda: self.update_color(self.btn9))
        self.btn9.addItems(self.color.color_tol.keys())
        self.btn9.currentIndexChanged.connect(self.cal5)
        self.b5.append(self.btn9)
        
        # 6 bound
        self.res6 = QLineEdit()
        self.res6.setReadOnly(True)
        self.res6.setFixedSize(200,20)
        self.b6 = []
        
        self.btn10 = QComboBox()
        self.btn10.setPlaceholderText("select a color")
        self.btn10.setFixedSize(120, 20)
        self.btn10.currentIndexChanged.connect(lambda: self.update_color(self.btn10))
        self.btn10.addItems(self.color.color_val.keys())
        self.btn10.currentIndexChanged.connect(self.cal6)
        self.b6.append(self.btn10)

        self.btn11 = QComboBox()
        self.btn11.setPlaceholderText("select a color")
        self.btn11.setFixedSize(120, 20)
        self.btn11.currentIndexChanged.connect(lambda: self.update_color(self.btn11))
        self.btn11.addItems(self.color.color_val.keys())
        self.btn11.currentIndexChanged.connect(self.cal6)
        self.b6.append(self.btn11)

        self.btn12 = QComboBox()
        self.btn12.setPlaceholderText("select a color")
        self.btn12.setFixedSize(120, 20)
        self.btn12.currentIndexChanged.connect(lambda: self.update_color(self.btn12))
        self.btn12.addItems(self.color.color_val.keys())
        self.btn12.currentIndexChanged.connect(self.cal6)
        self.b6.append(self.btn12)

        self.btn13 = QComboBox()
        self.btn13.setPlaceholderText("select a color")
        self.btn13.setFixedSize(120, 20)
        self.btn13.currentIndexChanged.connect(lambda: self.update_color(self.btn13))
        self.btn13.addItems(self.color.color_coe.keys())
        self.btn13.currentIndexChanged.connect(self.cal6)
        self.b6.append(self.btn13)

        self.btn14 = QComboBox()
        self.btn14.setPlaceholderText("select a color")
        self.btn14.setFixedSize(120, 20)
        self.btn14.currentIndexChanged.connect(lambda: self.update_color(self.btn14))
        self.btn14.addItems(self.color.color_tol.keys())
        self.btn14.currentIndexChanged.connect(self.cal6)
        self.b6.append(self.btn14)

        self.btn15 = QComboBox()
        self.btn15.setPlaceholderText("select a color")
        self.btn15.setFixedSize(120, 20)
        self.btn15.currentIndexChanged.connect(lambda: self.update_color(self.btn15))
        self.btn15.addItems(self.color.color_ppm.keys())
        self.btn15.currentIndexChanged.connect(self.cal6)
        self.b6.append(self.btn15)
        

    def cal4(self):

        val1 = self.color.color_val[self.btn1.currentText()]
        val2 = self.color.color_val[self.btn2.currentText()]
        coef = self.color.color_coe[self.btn3.currentText()]
        tol  = self.color.color_tol[self.btn4.currentText()]

        x = val1 * (10** len(str(val2))) + val2
        y = x * (10** coef)
        #res = y * (tol / 100)
        if coef > 2:
            self.res4.setText(f"{y/1000} KΩ ± {tol} % ")
        else:
            self.res4.setText(f"{y} Ω ± {tol}% ")
    
    def cal5(self):
        val1 = self.color.color_val[self.btn5.currentText()]
        val2 = self.color.color_val[self.btn6.currentText()]
        val3 = self.color.color_val[self.btn7.currentText()]
        coef = self.color.color_coe[self.btn8.currentText()]
        tol  = self.color.color_tol[self.btn9.currentText()]
        
        x = val1 * (10** len(str(val2))) + val2
        y = x *(10**len(str(val3)))+val3
        z = y * (10**coef)
        #res = z * (tol/100)
        if coef > 2:
            self.res5.setText(f"{z/1000} KΩ ± {tol} % ")
        else:
            self.res5.setText(f"{z} Ω ± {tol}% ")
        
    
    def cal6(self):
        val1 = self.color.color_val[self.btn10.currentText()]
        val2 = self.color.color_val[self.btn11.currentText()]
        val3 = self.color.color_val[self.btn12.currentText()]
        coef = self.color.color_coe[self.btn13.currentText()]
        tol  = self.color.color_tol[self.btn14.currentText()]
        ppm  = self.color.color_ppm[self.btn15.currentText()]
        
        x = val1 * (10** len(str(val2))) + val2
        y = x *(10**len(str(val3)))+val3
        z = y * (10**coef)
        #res = z * (tol/100)
        if coef > 2:
            self.res6.setText(f"{z/1000} KΩ ± {tol} % ")
        else:
            self.res6.setText(f"{z} Ω ± {tol}% {ppm} ppm")
        
    def update_color(self, btn):
        color_name = btn.currentText()
        color_code = self.color.color_hex.get(color_name, "#FFFFFF")
        btn.setStyleSheet(f"""
            background-color: {color_code};
            color: black;  
            border-radius: 5px;
        """)