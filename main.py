from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QLineEdit, QPushButton
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
import sys
import math

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setGeometry(100, 100, 400, 600)

        # Set up display
        self.display = QLineEdit()
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setReadOnly(True)
        self.display.setFixedHeight(100)
        self.display.setFont(QFont("Arial", 24))

        # Set up main layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.display)

        # Grid for buttons
        button_layout = QGridLayout()
        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('.', 3, 1), ('+', 3, 2),
            ('C', 4, 0), ('√', 4, 1), ('^', 4, 2), ('%', 4, 3),
            ('sin', 5, 0), ('cos', 5, 1), ('tan', 5, 2), ('log', 5, 3),
            ('E', 6, 0), ('π', 6, 1), ('(', 6, 2), (')', 6, 3),
        ]

        # Create buttons
        for text, row, col in buttons:
            button = QPushButton(text)
            button.setFixedSize(80, 80)
            button.setFont(QFont("Arial", 16))
            button.clicked.connect(lambda _, t=text: self.on_button_click(t))
            button_layout.addWidget(button, row, col)

        # Create larger equals button
        equals_button = QPushButton("=")
        equals_button.setFixedSize(80, 160)
        equals_button.setFont(QFont("Arial", 16))
        equals_button.clicked.connect(self.calculate)
        button_layout.addWidget(equals_button, 3, 3, 2, 1)  # Spanning two rows

        main_layout.addLayout(button_layout)
        self.setLayout(main_layout)

    def on_button_click(self, text):
        # Handle button functionality
        if text == "C":
            self.display.clear()
        elif text == "√":
            self.display.setText(self.display.text() + "sqrt(")
        elif text == "sin":
            self.display.setText(self.display.text() + "sin(")
        elif text == "cos":
            self.display.setText(self.display.text() + "cos(")
        elif text == "tan":
            self.display.setText(self.display.text() + "tan(")
        elif text == "log":
            self.display.setText(self.display.text() + "log(")
        elif text == "E":
            self.display.setText(self.display.text() + str(math.e))
        elif text == "π":
            self.display.setText(self.display.text() + str(math.pi))
        else:
            self.display.setText(self.display.text() + text)

    def calculate(self):
        # Evaluate expression
        expression = self.display.text()
        try:
            # Replace symbols with Python equivalents
            expression = expression.replace('^', '**')
            expression = expression.replace('sqrt', 'math.sqrt')
            expression = expression.replace('sin', 'math.sin')
            expression = expression.replace('cos', 'math.cos')
            expression = expression.replace('tan', 'math.tan')
            expression = expression.replace('log', 'math.log10')

            result = eval(expression, {"math": math})
            self.display.setText(str(result))
        except Exception:
            self.display.setText("Error")

# Run the application
app = QApplication(sys.argv)
calculator = Calculator()
calculator.show()
sys.exit(app.exec())
