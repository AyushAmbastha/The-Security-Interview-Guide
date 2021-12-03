#!usr/bin/env python
# This program displays metadata from pdf file

import pyPdf

def main():
    # Enter the location of 'ANONOPS_The_Press_Release.pdf'
    # Download the PDF if you haven't already
	filename = <LOCATION_OF_THE_PDF>
	
	pdfFile = pyPdf.PdfFileReader(file(filename,'rb'))
	data = pdfFile.getDocumentInfo()

	print "----Metadata of the file----"
	
	for metadata in data:
		print metadata+ ":" +data[metadata]

if __name__ == '__main__':
	main()