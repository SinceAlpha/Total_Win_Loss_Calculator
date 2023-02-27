#Author Darwin Borsato 2023-02-26
#
from datetime import datetime
import sys
from PyQt5.QtWidgets import *
import mainwindow as mw

def main():
    pass


if __name__ == '__main__':
    # Create the application and the main window
    app = QApplication(sys.argv)
    window = mw.MainWindow()

    # Show the window
    window.show()

    # Run the event loop
    sys.exit(app.exec_())
