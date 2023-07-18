# Equation Plotting
Equation Plotting is an easy-to-use desktop application that enables users to visualize mathematical equations and functions using Python libraries, making it easy to create interactive and aesthetically pleasing diagrams for various scientific and mathematical applications.

This repository contains a Python application for plotting mathematical equations and functions. The program utilizes the matplotlib library to create interactive line plots. The application is built using PySide2, a Python binding for the Qt framework, to provide a simple graphical user interface (GUI) for entering function parameters and displaying the plotted results.

# Installation
To run this application, you need to have Python and the following libraries installed:

1. matplotlib
2. PySide2
3. pytest (only if you want to test the application)

You can install these dependencies using pip: "pip install matplotlib PySide2"

# How to use 
1. Clone the repository to your local machine.
2. Make sure you have the required dependencies installed as mentioned.
3. Run the Equation_Plotting.py script to launch the application.
4. Enter a mathematical function in terms of x using valid characters (numbers, operators, parentheses) into the input field.
5. Enter the minimum and maximum values for the x-axis range.
6. Click the "Plot the line" button to visualize the graph.
7. If there are any errors in the input, an error message will be displayed below the plot area.
8. You can try different functions and x-axis ranges by entering new values and clicking the "Plot the line" button again.   

# Example Usage

->[Import the required classes and libraries]

import sys
from Equation_Plotting import FunctionPlotter
from PySide2.QtWidgets import QApplication
if __name__ == '__main__':
    app = QApplication(sys.argv)
    plotter = FunctionPlotter()
    plotter.show()
    sys.exit(app.exec_())
  
# Testing the application (Optional)
-If you want to run the test cases, ensure that you have the pytest library installed: 
 "pip install pytest"
-Then, execute the test file test_Equation_Plotting.py: 
 pytest test_Equation_Plotting.py

 The tests will verify the functionality of the FunctionPlotter class for plotting valid and invalid functions, as well as checking for appropriate error messages.

# Contributors
Marwan Salah (@Marwan951)
