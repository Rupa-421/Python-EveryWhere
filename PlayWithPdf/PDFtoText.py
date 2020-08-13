from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter, HTMLConverter, XMLConverter
from pdfminer.layout import LAParams
import io


pdf_path='D:\\Users\\hp\\Desktop\\pdf1.pdf'#path to your pdf file
pdf=open(pdf_path,'rb')
mem=io.StringIO()

lp=LAParams()
rm=PDFResourceManager()
cnv=TextConverter(rm,mem,laparams=lp)
ip=PDFPageInterpreter(rm,cnv)

for i in PDFPage.get_pages(pdf):
    ip.process_page(i)
    text=mem.getvalue()

file=open("D:\\Mani\\pdf1.txt",'wb')#path to your destination file
file.write(text.encode('utf-8'))
