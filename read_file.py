# -*- coding: utf-8 -*-
"""
#Process different filetypes and return the content as a string
#Supported filetypes: pdf, scanned pdf, word, html.

@author: Viktoria
June, 2021

"""

import pdfplumber
import ocrmypdf
import textract
import os
import magic
import docx2txt
import pdfkit
from docx2pdf import convert
import re


def read_file(title, directory):
    
    if 'DS_Store' not in title:
  
        try:
            os.chdir(directory)
            
            #Find out the file type
            filetype = magic.from_file(title)
            
            if 'PDF' in filetype:
            
                with pdfplumber.open(title) as pdf:
                    
                    page = pdf.pages[0]
                    text = page.extract_text()
                
                    #scanned pdf
                    if text==None: #scanned pdf
                        ocrmypdf.ocr(title, 'myfile_converted.pdf', deskew=True, progress_bar=False)
                        content = textract.process('myfile_converted.pdf', method='pdfminer') #pdf
                        os.remove('myfile_converted.pdf')
                            
                    #normal pdf
                    else:
                        content = textract.process(title, method='pdfminer') #pdf
                        
            #word
            elif 'Microsoft Word' in filetype:
                
                content = docx2txt.process(title)
        
                #convert to pdf
                newtitle = re.sub(r'.pdf', '', title)
                convert(title, newtitle + '.pdf')
                os.remove(title)
                
            elif 'HTML Document' in filetype:
        
                newtitle = re.sub(r'htm', '', title)
                pdfkit.from_file(title, newtitle + '.pdf')
                content = textract.process(newtitle+'.pdf', method='pdfminer')
                os.remove(title)
                
            else:
                #some unknown file type
                content=None
            
        except: 
            print(title)
            content=None
            
    else:
        #DS Store
        content=None
        
    
    return content