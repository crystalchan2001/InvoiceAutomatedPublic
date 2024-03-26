from invoice import Invoice
from datetime import datetime

def sortLessons(lessonStrings):
    lessonDates = [datetime.strptime(lesson, "%d/%m/%y %H:%M") for lesson in lessonStrings]
    sortedDates = sorted(lessonDates)
    sortedStrings = [date.strftime("%d/%m/%y %H:%M") for date in sortedDates]
    return sortedStrings

def createInvoice(lessonsList):
    Invoice(sortLessons(lessonsList))
