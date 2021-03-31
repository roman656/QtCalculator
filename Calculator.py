import sys
from PyQt5 import QtWidgets
from UI.CalculatorMainWindow import Ui_CalculatorMainWindow


class Calculator(QtWidgets.QMainWindow):
    def __init__(self):
        super(Calculator, self).__init__()
        self.ui = Ui_CalculatorMainWindow()
        self.ui.setupUi(self)
        self.max_symbols_amount = 15
        self.has_dot = False
        self.input_buffer = "0"
        self.saved_input_buffer = "0"
        self.has_saved_input = False
        self.operation = "None"
        self.prev_answer = "0"
        self.ui.lcd_number_main.display(self.input_buffer)
        self.add_handlers()

    def add_handlers(self):
        self.ui.button_0.clicked.connect(lambda: self.add_number(0))
        self.ui.button_1.clicked.connect(lambda: self.add_number(1))
        self.ui.button_2.clicked.connect(lambda: self.add_number(2))
        self.ui.button_3.clicked.connect(lambda: self.add_number(3))
        self.ui.button_4.clicked.connect(lambda: self.add_number(4))
        self.ui.button_5.clicked.connect(lambda: self.add_number(5))
        self.ui.button_6.clicked.connect(lambda: self.add_number(6))
        self.ui.button_7.clicked.connect(lambda: self.add_number(7))
        self.ui.button_8.clicked.connect(lambda: self.add_number(8))
        self.ui.button_9.clicked.connect(lambda: self.add_number(9))
        self.ui.button_dot.clicked.connect(self.add_dot)
        self.ui.button_ac.clicked.connect(self.reset)
        self.ui.button_del.clicked.connect(self.del_pressed)
        self.ui.button_mul.clicked.connect(lambda: self.select_operation("mul"))
        self.ui.button_div.clicked.connect(lambda: self.select_operation("div"))
        self.ui.button_sum.clicked.connect(lambda: self.select_operation("sum"))
        self.ui.button_sub.clicked.connect(lambda: self.select_operation("sub"))
        self.ui.button_ans.clicked.connect(self.ans_pressed)
        self.ui.button_result.clicked.connect(self.calculate)

    def add_number(self, number):
        if len(self.input_buffer) < self.max_symbols_amount:
            if self.input_buffer == "0":
                self.input_buffer = str(number)
            else:
                self.input_buffer += str(number)

            self.ui.lcd_number_main.display(self.input_buffer)

    def add_dot(self):
        if not self.has_dot and len(self.input_buffer) < self.max_symbols_amount:
            self.has_dot = True
            self.input_buffer += "."
            self.ui.lcd_number_main.display(self.input_buffer)

    def ans_pressed(self):
        self.input_buffer = self.prev_answer
        if "." in self.input_buffer:
            self.has_dot = True
        self.ui.lcd_number_main.display(self.input_buffer)

    def reset(self):
        self.has_dot = False
        self.input_buffer = "0"
        self.saved_input_buffer = "0"
        self.has_saved_input = False
        self.operation = "None"
        self.ui.lcd_number_main.display(self.input_buffer)

    def del_pressed(self):
        if self.input_buffer != "0":
            if len(self.input_buffer) == 1:
                self.input_buffer = "0"
            else:
                if self.input_buffer[-1] == ".":
                    self.has_dot = False
                self.input_buffer = self.input_buffer[:-1]

            if self.input_buffer[-1] == ".":
                self.ui.lcd_number_main.display(self.input_buffer[:-1])
            else:
                self.ui.lcd_number_main.display(self.input_buffer)

    def select_operation(self, operation_name):
        self.saved_input_buffer = self.input_buffer
        self.has_saved_input = True
        self.has_dot = False
        self.input_buffer = "0"
        self.operation = operation_name
        self.ui.lcd_number_main.display(self.input_buffer)

    def calculate(self):
        if self.input_buffer[-1] == ".":
            self.input_buffer = self.input_buffer[:-1]

        if self.saved_input_buffer[-1] == ".":
            self.saved_input_buffer = self.saved_input_buffer[:-1]

        if self.operation == "mul":
            result = float(self.saved_input_buffer) * float(self.input_buffer)
        elif self.operation == "div":
            if float(self.input_buffer) == 0.0:
                return
            else:
                result = float(self.saved_input_buffer) / float(self.input_buffer)
        elif self.operation == "sum":
            result = float(self.saved_input_buffer) + float(self.input_buffer)
        elif self.operation == "sub":
            result = float(self.saved_input_buffer) - float(self.input_buffer)
        else:
            result = float(self.input_buffer)

        result = str(result)[: self.max_symbols_amount]
        if result[-1] == "0" and result[-2] == ".":
            result = result[:-2]
        self.prev_answer = result
        self.reset()
        if "." in result:
            self.has_dot = True
        self.input_buffer = result
        self.ui.lcd_number_main.display(self.input_buffer)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    application = Calculator()
    application.show()

    sys.exit(app.exec())
