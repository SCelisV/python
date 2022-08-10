import PyPDF2
from PyPDF2 import PdffileMerger, PdfFileReader

list = ["file1.pdf", "file2.pdf"]

merge = PyPDF2.PdfFileMerger()

for file in list:

    merge.append(PyPDF2.PdfFileReader(file, 'rb'))
    merge.write("mergedfile.pdf")
    merge.close

createdfile = PdfFileReader('mergedfile.pdf')

print(createdfile)