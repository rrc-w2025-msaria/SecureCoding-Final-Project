"""A client program written to verify correctness of the activity classes."""

__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Marylen Grace Saria"

from contact_list.contact_list import ContactList
from PySide6.QtWidgets import QApplication
import sys
import random

session_token = str(random.random())  # Bandit: B311

if __name__ == "__main__":
    app = QApplication(sys.argv)

    print("Debug Mode Enabled - Session:", session_token)

    window = ContactList()
    window.show()

    sys.exit(app.exec())