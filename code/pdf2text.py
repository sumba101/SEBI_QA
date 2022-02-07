from io import StringIO

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

def convert_pdf_to_string(file_path):

    output_string = StringIO()
    with open(file_path, 'rb') as in_file:
        parser = PDFParser(in_file)
        doc = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)

    return(output_string.getvalue())

                
def convert_title_to_filename(title):
    filename = title.lower()
    filename = filename.replace(' ', '_')
    return filename


def split_to_title_and_pagenum(table_of_contents_entry): #Can be used to print regulations chapterwise
    title_and_pagenum = table_of_contents_entry.strip()
    
    title = None
    pagenum = None
    
    if len(title_and_pagenum) > 0:
        if title_and_pagenum[-1].isdigit():
            i = -2
            while title_and_pagenum[i].isdigit():
                i -= 1

            title = title_and_pagenum[:i].strip()
            pagenum = int(title_and_pagenum[i:].strip())
        
    return title, pagenum


# text = convert_pdf_to_string('../document_scraping/regulations/collected_docs/1602652369689.pdf')

from tqdm import tqdm as tqdm
from glob import glob
from os import path

print('started running')

for file in tqdm(glob('./collected_pdfs/*.pdf')):
    file_name = path.basename(file)
    file_str, _ = file_name.split('.')
    if not path.exists(f"./text_pdfs/{file_str}.txt"):
        with open(f"./text_pdfs/{file_str}.txt", "w") as f:
            f.write(convert_pdf_to_string(file))
    else:
        "Dates repeat ??"
    
