import pytest
from IPython.external.qt_for_kernel import QtCore
from Equation_Plotting import FunctionPlotter
from PySide2.QtWidgets import QApplication


@pytest.fixture(scope='session')
def app(request):
    # Check if a QApplication instance already exists
    Q_app = QApplication.instance()
    if Q_app is None:
        # If it doesn't, create a new instance
        Q_app = QApplication([])
        # Register a finalizer to quit the QApplication when all tests are done
        request.addfinalizer(Q_app.quit)
    return Q_app


def test_plot_valid_function(app):
    plotter = FunctionPlotter()

    # Enter a valid function
    plotter.input_text.setText('2*x^2 + 3*x + 4')
    plotter.min_text.setText('-10')
    plotter.max_text.setText('10')

    # Simulate button click
    plotter.plot_button.clicked.emit()

    # Assert that no error message is displayed
    assert plotter.plot_layout.count() == 1


def test_plot_invalid_function(app):
    plotter = FunctionPlotter()

    # Enter an invalid function (missing operator)
    plotter.input_text.setText('2*x^2 3*x + 4')
    plotter.min_text.setText('-10')
    plotter.max_text.setText('10')

    # Simulate button click
    plotter.plot_button.clicked.emit()

    # Assert that an error message is displayed
    assert plotter.plot_layout.count() == 2


def test_plot_invalid_x_range(app):
    plotter = FunctionPlotter()

    # Enter a valid function with an invalid x range
    plotter.input_text.setText('x')
    plotter.min_text.setText('10')
    plotter.max_text.setText('a')

    # Simulate button click
    plotter.plot_button.clicked.emit()

    # Assert that an error message is displayed
    assert plotter.plot_layout.count() == 2
