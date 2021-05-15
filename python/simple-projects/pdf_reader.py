import fitz
import re
import os

#Install following modules
#   pip install fitz
#   pip install pymupdf

PDF_FOLDER = "/Users/srmk/Desktop/nsdl/"


class MyPdfReader:

    def search_pdf(self, filename, pattern, password=""):
        pdf_file = fitz.Document(filename)
        all_lines = []

        if pdf_file.isEncrypted:
            if not pdf_file.authenticate(password):
                print("cannot decrypt with password")
                return

        for i in range(0, pdf_file.pageCount):
            page = pdf_file.loadPage(i)
            text = str(page.getText(output="text")).splitlines()
            prev_prev_line = ""
            prev_line = ""
            for line in text:
                line.strip()
                if re.search(pattern, line, re.IGNORECASE):
                    #print(line)
                    all_lines.append(line)

        return all_lines

                    #for word in line.split(" "):
                        #if re.search("\.00$", word, re.IGNORECASE):
                            #print(word)
