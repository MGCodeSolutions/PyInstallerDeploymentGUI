# Author: TheRealInfidel@MGCodeSolutions

from tkinter import *
import PyInstaller.__main__

root = Tk()
root.geometry('800x300')
root.title("PyInstaller for .exe")

pyfile = StringVar()
pylocal = StringVar()

def convert():
    py4exe = ent1.get()
    pylocation = ent2.get()
   
    PyInstaller.__main__.run([pylocation + "/" + py4exe, "--onefile"])
    #print(pylocation + "/" + py4exe + " --onefile") #uncomment for testing

lbl1 = Label(root, text="Insert filename '.py' to convert to '.exe'", font=('ariel', 18))
lbl1.pack(pady=25)

ent1 = Entry(root, textvariable=pyfile, font=("ariel", 12))
ent1.pack()

lbl2 = Label(root, text="Input location of file to convert", font=('ariel', 18))
lbl2.pack(pady=25)

ent2 = Entry(root, textvariable=pylocal, font=('ariel', 12))
ent2.pack()


lbl3 = Label(root, text="Hint: convert backslash (\) to front slash *(/) to avoid errors", font=('ariel',10))
lbl3.pack()

btn = Button(root, text="Convert", font=('ariel', 18), command=convert)
btn.pack(pady=10)

root.mainloop()