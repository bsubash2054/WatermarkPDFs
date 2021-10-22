from reportlab.pdfgen import canvas
from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter


import os

directory = r'in-pdf' #input directory

picture_path = 'watermark.png' #watermark image location
#create watermark png to PDF
c = canvas.Canvas('temp/watermark.pdf')
c.drawImage(picture_path, 170 , 300,250,250,mask='auto')
c.save()
#eo creation of pdf from png watermark
watermark_pdf = PdfFileReader(open("temp/watermark.pdf", "rb")) #open watermark PDF

watermark_page = watermark_pdf.getPage(0) #get PDF Page of Watermark


for filename in os.listdir(directory):   #loop via all pdfs placed in the directory 'in-pdf'
    if filename.endswith(".pdf"): #Take only pdf files to watermark
        input_file = "in-pdf/" + filename #place your files to watermark in this directory
        output_file = "out-pdf/" + filename #Watermarked files appear here after being watermarked

        with open(input_file, 'rb') as f:
            pdf_reader = PdfFileReader(f)
            number_of_pages = pdf_reader.getNumPages()
            output = PdfFileWriter()
            for x in range(number_of_pages): #Loop through each page of the pdf file
                page_temp = pdf_reader.getPage(x) #Get the current page to watermark
                page_temp.mergePage(watermark_page) #Apply watermark to a particular page
                output.addPage(page_temp)
                print(str(x)+" Pages of " + str(number_of_pages) + " of File :"+filename)
            with open(output_file, "wb") as merged_file:
                output.write(merged_file) #Write watermarked file to the directory 'out-pdf'
        print("File WaterMarked:"+filename)
    else:
        continue
