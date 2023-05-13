# Add main function to run the GUI
# Initialize Tkinter window and GUI object
# Set window title, size, and prevent resizing

from gui import GUI
from tkinter import Tk


def main() -> None:
    """
    Initializes the Tkinter window and runs the GUI for the Grades Calculator.
    :return:
    """
    window = Tk()
    window.title('Grades Calculator')
    window.geometry('500x400')
    window.resizable(False, False)

    GUI(window)
    window.mainloop()


if __name__ == '__main__':
    main()
