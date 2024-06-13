import io
import sys
from tkinter import filedialog

# Dateipfad auswählen
def selectFile() -> str:
    file = filedialog.askopenfilename()
    return file

def getConsoleOutput(methodToCall):
    output = io.StringIO()

    # Redirect standard output to the new stream
    sys.stdout = output

    methodToCall()

    # Reset standard output to the console
    sys.stdout = sys.__stdout__
    return output.getvalue()