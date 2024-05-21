import camelot as cm
import PySimpleGUI as sg
from tkinter import filedialog
import pandas as pd

def createPdfGui():
    layout=[[sg.Button("open",key="-OPEN-")],[ sg.FileBrowse()],
            [sg.Text("",key="-TABLE-")],
            [sg.Button("toCsv",key="-CSV-",disabled=True)],[sg.Button("toXLSX",key="-XLSX-",disabled=True)],[sg.Button("toPDF",key="-PDF-",disabled=True)]]
    return sg.Window("pdf",layout,size=(400,400))

window=createPdfGui()
def openfiledialog(): 
 folder=filedialog.askdirectory()
 return folder

while True:
    event,values=window.read()
    if event==sg.WIN_CLOSED:
        break
    if event=="-OPEN-":
      try:
       wanted_file=cm.read_pdf(f"{values['Browse']}",flavor="lattice",pages="1,2")
       fc=sg.popup_get_text("from what column: ")
       tc=sg.popup_get_text("to what column: ")
       fr=sg.popup_get_text("from what row: ")
       tr=sg.popup_get_text("to what row: ")
       if not wanted_file or not fc or not tc or not fr or not tr:
         window["-TABLE-"].update("you didnt provide something")  
       else:  
        df=wanted_file[0].df.loc[fc:tc,fr:tr]
        window['-TABLE-'].update(df)
        window['-CSV-'].update(disabled=False)
        window['-XLSX-'].update(disabled=False)
        window['-PDF-'].update(disabled=False)
      except Exception as e:
       print("sorry wrong")   
       window["-TABLE-"].update("you didnt provide something")  
    if event=="-CSV-":
            df.to_csv("nova.csv")
    if event=="-XLSX-":
            df.to_csv("nova.xlsx")
       
window.close()

       

