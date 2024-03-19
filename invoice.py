from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH as WAP
from docx.shared import Pt
from datetime import datetime


myAddress = "Address\nSeparated\nBy\nWhitespaces"
lineTo = "Who is this for?"
myBankDetails = "Bank Details: \n\nBank Account: \n\nSort Code: \n\nAccount Number: \n\nIBAN: "

now = datetime.now()
day = now.strftime('%d')
monthNum = now.strftime('%m')
month = now.strftime('%B')
yearShort = now.strftime('%y')
year = now.strftime('%Y')

class Invoice():                                                                                                                                                                                                                                                                                    

    def __init__(self, lessonsList):
        self.invoiceDoc = Document()
        self.setStyle()
        
        self.lessonsList = lessonsList

        self.writeAddress()
        self.writeHeader()
        self.writeHours()
        self.writeTotal()
        self.writeBankDetails()

        self.saveInvoice()

    def getPath(self):
        name = f"Monthly Invoice {month} {year}.docx"
        path = f"path_to_file_name/{name}"
        return path

    def setStyle(self):
        style = self.invoiceDoc.styles['Normal']
        font = style.font
        font.name = 'Calibri'
        font.size = Pt(12)

    def write(self, text):
        para = self.invoiceDoc.add_paragraph(text)
        para.style = self.invoiceDoc.styles['Normal']
        return para

    def getDate(self):
        date = f"{now.strftime('%d')}/{monthNum}/{yearShort}"
        return "Date: " + date

    def getCode(self):
        code = f"NAME_{monthNum}_{yearShort}"
        return "Invoice: " + code

    def getSubjects(self):
        return "For: English, Maths, Reasoning, Science"
    
    def getHours(self):
        # lessons will be in format "DD/MM/YY HH:MM"
        lessons = "\n"
        for lesson in self.lessonsList:
            lesson = lesson.strip()
            lessons += f"\t-{lesson}\n"
        return lessons

    def getTotal(self):
        hours = len(self.lessonsList)
        total = str(hours * 40)
        return "Total: £" + total

    def writeAddress(self):
        addressPar = self.write(myAddress)
        addressPar.alignment = WAP.CENTER

    def writeHeader(self):
        self.write(lineTo)
        self.write(self.getDate())
        self.write(self.getCode())
        self.write(self.getSubjects())
    
    def writeHours(self):
        hoursPar = self.write("Hours:")
        hoursPar.add_run(self.getHours())
    
    def writeTotal(self):
        self.write(self.getTotal())

    def writeBankDetails(self):
        self.write(myBankDetails)
    
    def saveInvoice(self):
        path = self.getPath()
        try:
            self.invoiceDoc.save(path)
        except PermissionError:
            print("Check if you have the file open luv")
            doc = Document(path)
            doc.save(path)

    

# to run the file: python InvoiceAutomatedPublic/createInvoice.py
# input into CLI
# 1/11/23 16:15-17:15, 8/11/23 16:15-17:15, 29/11/23 16:15-17:15
