# importing required modules
import PyPDF2

pdfFiles=['example2.pdf','example.pdf']
merger=PyPDF2.PdfMerger()
for file in pdfFiles:
    pdfFile=open(file,'rb')
    pdfReader=PyPDF2.PdfReader(pdfFile)
    merger.append(pdfReader)
pdfFile.close()  
merger.write("merged.pdf")  




