#This file will initiate the workflow process for analyzing and converting PDF information to ICS

from functions.rawDataFunctions import getText
from modules.RawData import RawData
from modules.ICS import ICS
from pdf2image.exceptions import PDFPageCountError


def runExtraction():
    
    run = True
    
    while (run):
        print("Welcome! Please input a filepath to a PDF file, enter 0 to quit!")
        path = input()
        if path == "0":
            run = False
        elif path[-4:] != ".pdf":
            print("filepath does not point to a pdf file, make sure the filepath ends with '.pdf'!")
        else:
            try:
                text = getText(path)
            except FileNotFoundError:
                print("Invalid file path!")
            except PDFPageCountError:
                print("Invalid file path!")
            else:
                rawData = RawData(None,text,path)
                rawData.getTitlefromData()
                rawData.mineDueDates()
                ics = ICS(rawData.title,rawData.Events)
                ics.writeICS()
                print("Your ICS file has been generated!")
                
