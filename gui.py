# Add GUI class to create and manage window and widgets
# Implement method to create text boxes based on number of students entered
# Implement method to calculate grades and display results
# Implement method to reset GUI to initial state
# Add input validation for student name and scores

from tkinter import *
from tkinter import messagebox  # Didn't import with * for some reason
from grades import calculate_grades


class GUI:
    def __init__(self, master: Tk) -> None:
        """
        Initializes the GUI class.
        :param master: The tkinter master object.
        """
        self.master = master
        self.students = 0
        self.textboxes = []
        self.labels = []
        self.grades = []

        # Create widgets
        Label(master, text="How many students?").grid(row=0, column=0, padx=10, pady=10, sticky=W)
        self.students_entry = Entry(master)
        self.students_entry.grid(row=0, column=1, padx=10, pady=10, sticky=W)

        self.create_button = Button(master, text="Create Textboxes", command=self.create_textboxes)
        self.create_button.grid(row=0, column=2, padx=10, pady=10)

    def create_textboxes(self) -> None:
        """
        Creates the required number of text boxes needed for entering
        the grades of each student.
        """
        try:
            self.students = int(self.students_entry.get())
            if self.students <= 0:
                messagebox.showerror("Error", "The number of students must be greater than 0")
                return
            elif self.students > 5:
                messagebox.showerror("Error", "The number of students cannot be greater than 5")
                return
        except ValueError:
            messagebox.showerror("Error", "Only a number can be entered")
            return

        self.labels = []
        self.textboxes = []
        self.grades = []

        # Create text boxes for each student
        for i in range(self.students):
            label = Label(self.master, text=f"Student {i+1} Grade:")
            label.grid(row=i+2, column=0, padx=10, pady=10, sticky=W)
            self.labels.append(label)

            textbox = Entry(self.master)
            textbox.grid(row=i+2, column=1, padx=10, pady=10, sticky=W)
            self.textboxes.append(textbox)

        #  The buttons are here, so they appear after "Create Textboxes" button is pushed
        self.calculate_button = Button(self.master, text="Calculate Grades", command=self.calculate_grades)
        self.calculate_button.grid(column=1, row=3+int(self.students), padx=5, pady=5, sticky='W')

        self.reset_button = Button(self.master, text="Reset", command=self.reset)
        self.reset_button.grid(column=0, row=3+int(self.students), padx=5, pady=5, sticky='W')

    def calculate_grades(self) -> None:
        """
        Calculates the grade letter for each student and displays the results
        """
        self.grades = []
        for i in range(self.students):
            try:
                grade = int(self.textboxes[i].get())
                if grade < 0 or grade > 100:
                    messagebox.showerror("Error", "Please enter a valid grade (between 0 and 100) for each student")
                self.grades.append(grade)
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid grade for each student")
                return

        try:
            results = calculate_grades(self.grades)
        except ZeroDivisionError:
            messagebox.showerror("Error", "The list of grades cannot be empty")
            return
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while calculating grades: {str(e)}")
            return

        for i, result in enumerate(results):
            label = self.labels[i]
            label.config(text=f"Student {i + 1} score is {self.grades[i]} and grade is {result}")

        messagebox.showinfo("Grades", "Grades calculated successfully!")

    def reset(self) -> None:
        """
        Resets the GUI by deleting all text boxes, labels, and resetting the number
        of students to zero
        """
        self.students_entry.delete(0, END)
        self.students = 0
        for label in self.labels:
            label.destroy()
        for textbox in self.textboxes:
            textbox.destroy()
        self.labels = []
        self.textboxes = []
        self.grades = []
        self.calculate_button.destroy()
        self.reset_button.destroy()
