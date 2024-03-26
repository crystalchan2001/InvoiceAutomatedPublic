from tkinter import Tk, Button, messagebox
from tkcalendar import Calendar
from datetime import datetime
from createInvoice import createInvoice

class LessonSelector:
    def __init__(self, root):
        self.root = root
        self.root.title("Select Lessons")
        self.root.geometry("600x700")
        self.root.config(background="pink")
        self.font = ("Courier", 14)

        self.lessonsList = []

        self.setupGUI()
        self.setupButtons()
    
    def setupGUI(self):
        # Creating the calendar
        self.cal = Calendar(self.root, font=("Courier", 14))
        self.cal.pack(padx=5, pady=5, fill="both", expand=True)

    def addLesson(self, lessonTime):
        lesson = f"{self.formatDate(self.cal.get_date())} {lessonTime}"
        self.lessonsList.append(lesson)
        print(f"Lessons: {self.lessonsList}")
    
    def addBoth(self):
        self.addLesson("16:15")
        self.addLesson("17:45")
    
    def showPopup(self, title, message):
        messagebox.showinfo(title, message)

    def clear(self):
        self.lessonsList = []
        self.showPopup("Message", "You cleared all selected lessons.")

    def done(self):
        if self.lessonsList:
            createInvoice(self.lessonsList)
            self.root.destroy()
        else:
            self.showPopup("Error Message", "Please select lessons to create an invoice.")

    def setupButtons(self):
        buttonA = Button(self.root, text="Student1", font=self.font, bg="lightyellow", command=lambda: self.addLesson("16:15"))
        buttonA.pack(pady=5)

        buttonD = Button(self.root, text="Student2", font=self.font, bg="lightgreen", command=lambda: self.addLesson("17:45"))
        buttonD.pack(pady=5)

        buttonBoth = Button(self.root, text="Both", font=self.font, bg="lightblue", command=self.addBoth)
        buttonBoth.pack(pady=5)

        buttonClear = Button(self.root, text="Clear", font=self.font, bg="white", command=self.clear)
        buttonClear.pack(pady=20)

        buttonExit = Button(self.root, text="Done", font=self.font, command=self.done)
        buttonExit.pack(pady=20)

    @staticmethod
    def formatDate(date):
        try:
            ogDate = datetime.strptime(date, "%m/%d/%y")
            formattedDate = ogDate.strftime("%d/%m/%y")
            return formattedDate
        except ValueError:
            print("Please select a date")

if __name__ == "__main__":
    root = Tk()
    LessonSelector(root)
    root.mainloop()