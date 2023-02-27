#Author Darwin Borsato
import os.path
from datetime import datetime
import sys
from PyQt5.QtWidgets import *
import easygui

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the window title
        self.setWindowTitle('CSV GUI')

        # Create a layout for the buttons
        layout = QVBoxLayout()

        # Create the "Create new csv" button and connect it to the create_csv function
        create_button = QPushButton('Create new csv', self)
        create_button.clicked.connect(self.create_csv)
        layout.addWidget(create_button)

        # Create the "Open CSV" button and connect it to the buyin_amount function
        open_csv = QPushButton('Open CSV', self)
        open_csv.clicked.connect(self.open_csv)
        layout.addWidget(open_csv)

        # Create the "Buyin Amount" button and connect it to the buyin_amount function
        buyin_button = QPushButton('Update Buy-ins', self)
        buyin_button.clicked.connect(self.buyin_amount)
        layout.addWidget(buyin_button)

        # Create the "Add Entry" button and connect it to the add_entry function
        add_button = QPushButton('Add Entry', self)
        add_button.clicked.connect(self.add_entry)
        layout.addWidget(add_button)

        # Create the "Exit" button and connect it to the close function
        exit_button = QPushButton('Exit', self)
        exit_button.clicked.connect(self.close)
        layout.addWidget(exit_button)

        # Create a widget to hold the layout and set it as the central widget of the window
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)



    def create_csv(self):
        global name_file
        filename = {}
        # Prompt the user for the name of the CSV file
        file_name, _ = QFileDialog.getSaveFileName(self, 'Save CSV File', '', 'CSV Files (*.csv)')

        # If the user selected a file name, create the CSV file with the headers
        if file_name:
            headers = ['Game', 'Bet Amount', 'Win/Loss Amount', 'Date and Time']
            df = pd.DataFrame(columns=headers)
            df.to_csv(file_name, index=False)

            # Show a message confirming the CSV file was created
            QMessageBox.information(self, 'Message', f'CSV file {file_name} created.')
            filename.update({"Filename": file_name})
            print("test")
            name_file = filename["Filename"]
            name_file = os.path.basename(name_file)
            print(name_file)

            # Ask the user if they want to add an entry
            reply = QMessageBox.question(self, 'Message', 'Do you want to add an entry?',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.add_entry()
            else:
                self.close()

    def open_csv(self):
        global name_file
        name_file = easygui.fileopenbox()
        name_file = os.path.basename(name_file)
        print(name_file)

    #def create_csv(self):

        # # Create the dataframe with the headers
        # df = pd.DataFrame(columns=['Game', 'Bet Amount', 'Win Amount', 'Date and Time'])
        #
        # # Write the dataframe to a CSV file
        # df.to_csv('my_data.csv', index=False)
        #
        # # Ask the user if they want to add an entry
        # reply = QMessageBox.question(self, 'Message', 'CSV file created. Do you want to add an entry?',
        #                              QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        # if reply == QMessageBox.Yes:
        #     self.add_entry()
        # else:
        #     self.close()

    def buyin_amount(self):
        pass
        # # hide the main window before opening the buyin window
        # self.hide()
        #
        # # create the buyin window instance and show it
        # self.buyin_window = BuyInAmount()
        # self.buyin_window.show()
        #
        # # connect the buyin window's closed signal to a method that will show the main window again
        # self.buyin_window.closed.connect(self.show_main_window)

    def add_entry(self):
        # Create a layout for the input fields
        layout = QVBoxLayout()

        # Create the input fields
        game_input = QLineEdit()
        bet_amount_input = QLineEdit()
        win_amount_input = QLineEdit()
        date_time_label = QLabel(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        date_time_layout = QHBoxLayout()
        date_time_layout.addWidget(QLabel('Date and Time:'))
        date_time_layout.addWidget(date_time_label)
        layout.addWidget(QLabel('Game:'))
        layout.addWidget(game_input)
        layout.addWidget(QLabel('Bet Amount:'))
        layout.addWidget(bet_amount_input)
        layout.addWidget(QLabel('Win/Loss Amount:'))
        layout.addWidget(win_amount_input)
        layout.addLayout(date_time_layout)

        # Create a widget to hold the input fields
        widget = QWidget()
        widget.setLayout(layout)

        # Create the "Add Entry" button and connect it to the add_entry_confirm function
        add_entry_button = QPushButton('Add Entry', self)
        add_entry_button.clicked.connect(
            lambda: self.add_entry_confirm(game_input.text(), bet_amount_input.text(), win_amount_input.text(),
                                           date_time_label.text()))

        # Create the "Add Another Entry" button and connect it to the add_entry function
        add_another_entry_button = QPushButton('Add Another Entry', self)
        add_another_entry_button.clicked.connect(self.add_entry)

        # Create the "Exit" button and connect it to the close function
        exit_button = QPushButton('Exit', self)
        exit_button.clicked.connect(self.close)

        # Create a layout for the buttons
        button_layout = QHBoxLayout()
        button_layout.addWidget(add_entry_button)
        button_layout.addWidget(add_another_entry_button)
        button_layout.addWidget(exit_button)

        # Create a widget to hold the buttons
        button_widget = QWidget()
        button_widget.setLayout(button_layout)

        # Create a layout for the window
        window_layout = QVBoxLayout()
        window_layout.addWidget(widget)
        window_layout.addWidget(button_widget)

        # Create a widget to hold the window layout
        window_widget = QWidget()
        window_widget.setLayout(window_layout)

        # Set the window title
        self.setWindowTitle('Add Entry')

        # Set the central widget of the window to be the input widget
        self.setCentralWidget(window_widget)

    def add_entry_confirm(self, game, bet_amount, win_amount, date_time):
        # Create a dataframe with the data to add to the CSV
        data = {'Game': game, 'Bet Amount': bet_amount, 'Win/loss Amount': win_amount, 'Date and Time': date_time}
        df = pd.DataFrame(data, index=[0])
        df = df.append(df, ignore_index=True)

        # Append the data to the CSV file
        # print(name_file)
        # with open(name_file["Filename"], 'a') as f:
        df.to_csv(name_file, header=False, index=False)
        print("here")
        # Show a confirmation message
        QMessageBox.information(self, 'Message', 'Entry added to CSV file.')

        # Ask the user if they want to add another entry
        reply = QMessageBox.question(self, 'Message', 'Do you want to add another entry?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.add_entry()
        else:
            self.close()

class BuyInAmount(QWidget):
    def __init__(self):
        super().__init__()

        # set window title
        self.setWindowTitle('Buy-in Amount')

        # create layout
        layout = QVBoxLayout()

        # create buttons
        self.create_csv_button = QPushButton('Create Buy-in CSV')
        self.add_buyin_button = QPushButton('Add Buy-in')
        self.exit_button = QPushButton('Exit')

        # add buttons to layout
        layout.addWidget(self.create_csv_button)
        layout.addWidget(self.add_buyin_button)
        layout.addWidget(self.exit_button)

        # set layout for window
        self.setLayout(layout)

        # set connections for buttons
        self.create_csv_button.clicked.connect(self.create_csv)
        self.add_buyin_button.clicked.connect(self.add_buyin)
        self.exit_button.clicked.connect(self.close)

    def create_csv(self):
        # create empty pandas dataframe
        df = pd.DataFrame(columns=['Buy-in Amount', 'Date and Time'])

        # save dataframe to CSV file
        df.to_csv('buyin.csv', index=False)

    def add_buyin(self):
        # prompt user for buy-in amount
        buyin_amount, ok = QInputDialog.getDouble(self, 'Add Buy-in', 'Enter Buy-in Amount:')

        # check if user clicked OK
        if ok:
            # get current date and time
            now = datetime.now()
            date_time = now.strftime('%Y-%m-%d %H:%M:%S')

            # read existing CSV file
            try:
                df = pd.read_csv('buyin.csv')
            except FileNotFoundError:
                # create empty pandas dataframe if file not found
                df = pd.DataFrame(columns=['Buy-in Amount', 'Date and Time'])

            # add new row to dataframe
            new_row = {'Buy-in Amount': buyin_amount, 'Date and Time': date_time}
            df = df.append(new_row, ignore_index=True)

            # save dataframe to CSV file
            df.to_csv('buyin.csv', index=False)


if __name__ == '__main__':
    # Create the application and the main window
    app = QApplication(sys.argv)
    window = MainWindow()

    # Show the window
    window.show()

    # Run the event loop
    sys.exit(app.exec_())


