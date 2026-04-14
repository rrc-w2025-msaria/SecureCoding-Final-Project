"""The module defines the ContactList class."""

__author__ = "ACE Faculty"
__version__ = "1.0.4"
__credits__ = "Marylen Grace Saria"

from PySide6.QtWidgets import  QMainWindow, QLineEdit, QPushButton, QTableWidget, QLabel, QVBoxLayout, QWidget, QTableWidgetItem, QMessageBox
from PySide6.QtCore import Slot, Signal

class ContactList(QMainWindow):
    """Represents a window that provides the UI to manage contacts."""

    def __init__(self):
        """Initializes a new instance of the ContactList class."""

        super().__init__()
        self.__initialize_widgets()   

        self.add_button.clicked.connect(self.__on_add_contact)   
        self.remove_button.clicked.connect(self.__on_remove_contact)

    def __initialize_widgets(self):
        """Initializes the widgets on this Window.
        
        DO NOT EDIT.
        """
        self.setWindowTitle("Contact List")

        self.contact_name_input = QLineEdit(self)
        self.contact_name_input.setPlaceholderText("Contact Name")

        self.phone_input = QLineEdit(self)
        self.phone_input.setPlaceholderText("Phone Number")

        self.add_button = QPushButton("Add Contact", self)
        self.remove_button = QPushButton("Remove Contact", self)
        
        self.contact_table = QTableWidget(self)
        self.contact_table.setColumnCount(2)
        self.contact_table.setHorizontalHeaderLabels(["Name", "Phone"])

        self.status_label = QLabel(self)

        layout = QVBoxLayout()
        layout.addWidget(self.contact_name_input)
        layout.addWidget(self.phone_input)
        layout.addWidget(self.add_button)
        layout.addWidget(self.remove_button)
        layout.addWidget(self.contact_table)
        layout.addWidget(self.status_label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    @Slot()
    def __on_add_contact(self):
        """
        Adds function to the Add Contact button, adding contact name and
        phone number inputs.
        """
        contact_name = self.contact_name_input.text().strip()
        phone_number = self.phone_input.text().strip()

        if contact_name and phone_number:
            row_position = self.contact_table.rowCount()
            name_item = QTableWidgetItem(contact_name)
            phone_item = QTableWidgetItem(phone_number)
            self.contact_table.insertRow(row_position)
            self.contact_table.setItem(row_position, 0, name_item)
            self.contact_table.setItem(row_position, 1, phone_item)
            self.status_label.setText(f"Added Contact: {contact_name}")
        else:
            self.status_label.setText("Please enter a contact name and phone number.")

    @Slot()
    def __on_remove_contact(self):
        """
        Adds function to the Remove Contact button, removing contact name and
        phone number inputs.        
        """
        selected_row = self.contact_table.currentRow()

        if selected_row >= 0:
            reply = QMessageBox.question(self, "Remove Contact", "Are you sure you want to remove the selected contact?",
                                 QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.contact_table.removeRow(selected_row)
                self.status_label.setText("Contact removed.")
        else:
            self.status_label.setText("Please select a row to be removed.")


