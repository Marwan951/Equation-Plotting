import sys
import re
import math
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PySide2.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget


class FunctionPlotter(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Equation Plotter")
        self.setGeometry(500, 200, 1100, 700)

        # Create a layout for the input widgets (labels, line edits, and the button)
        input_layout = QVBoxLayout()

        self.input_label = QLabel("Enter a function of x:")
        self.input_text = QLineEdit()

        self.min_label = QLabel("Enter min value of x:")
        self.min_text = QLineEdit()

        self.max_label = QLabel("Enter max value of x:")
        self.max_text = QLineEdit()

        self.plot_button = QPushButton("Plot the line")
        self.plot_button.clicked.connect(self.plot)

        input_layout.addWidget(self.input_label)
        input_layout.addWidget(self.input_text)
        input_layout.addWidget(self.min_label)
        input_layout.addWidget(self.min_text)
        input_layout.addWidget(self.max_label)
        input_layout.addWidget(self.max_text)
        input_layout.addWidget(self.plot_button)

        # Create a layout for the error messages
        self.error_layout = QVBoxLayout()

        # Create a layout for the plot
        self.plot_layout = QVBoxLayout()
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.plot_layout.addWidget(self.canvas)

        # Create a central widget and set the layout
        central_widget = QWidget()
        central_layout = QVBoxLayout()
        central_layout.addLayout(input_layout)
        central_layout.addLayout(self.error_layout)
        central_layout.addLayout(self.plot_layout)
        central_widget.setLayout(central_layout)
        self.setCentralWidget(central_widget)

    def validate_input(self, function, x_min, x_max):
        """
        Description: Validate the entry data
        param: function, x_min, x_max:
        return: Boolean
        """
        # Empty field
        if not function:
            self.display_error("Enter a function.")
            return False

        # Check the valid characters
        if not re.match(r"^[0-9+\-*/^x\s.()]+$", function):
            self.display_error("Invalid characters.")
            return False

        # Validate min & max numbers
        try:
            float(x_min)
            float(x_max)
        except ValueError:
            self.display_error("Invalid min or max value, try again.")
            return False

        return True

    def display_error(self, message):
        """
        Description: Display an error message
        param message: Message
        """
        error_label = QLabel(message)
        error_label.setStyleSheet("color: Red")
        self.plot_layout.addWidget(error_label)

    def plot(self):
        """
        Description: plot the equation line after validating the entry data
        return
        """
        function = self.input_text.text()
        x_min = self.min_text.text()
        x_max = self.max_text.text()

        # Validate entry data
        if not self.validate_input(function, x_min, x_max):
            return None

        x = []
        y = []

        # Evaluate the function for each x value in the range
        start = int(float(x_min) * 10)
        end = int(float(x_max) * 10)
        for i in range(start, end + 1):
            x_value = i / 10.0
            x.append(x_value)

            try:
                y_value = eval(function.replace('^', '**').replace('x', str(x_value)))
                y.append(y_value)
            except (SyntaxError, TypeError, ZeroDivisionError, ValueError):
                self.display_error("Invalid function.")
                return

        # Clear the plot layout
        for i in reversed(range(self.plot_layout.count())):
            item = self.plot_layout.itemAt(i)
            if isinstance(item.widget(), QLabel):
                item.widget().deleteLater()

        # Plot the function
        self.figure.clear()
        plt.plot(x, y)
        plt.xlabel('x')
        plt.ylabel('f(x)')
        self.canvas.draw()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    plotter = FunctionPlotter()
    plotter.show()
    sys.exit(app.exec_())


