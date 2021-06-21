from PyPDF2 import PdfFileWriter, PdfFileReader
pdfl = ["F:\\Documents\\1ST YAER MASTER PDF.pdf"]
obj=PdfFileWriter()


for i in pdfl:
    x=PdfFileReader(i)
    pages=x.getNumPages()


    for j in range(pages):
        p=x.getPage(j)
        obj.addPage(p)


a=open("F:\\Documents\\sdsencrypt.pdf","wb")
obj.encrypt('sds','2003',True)
obj.write(a)
a.close()




