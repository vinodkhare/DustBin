import os

folder = '/media/Store/.Trash-1000/files/Kim.Kardashian.Superstar.XXX.DVDRiP.XviD-DivXfacTory'

def isDirEmpty(folder):
    if os.listdir(folder) == []:
        return True
    else:
        return False
        
print isDirEmpty(folder)
