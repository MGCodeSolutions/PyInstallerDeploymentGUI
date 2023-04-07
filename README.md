# PyInstallerGUI
 <!-- If you have the project hosted somewhere, include the link here. -->

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Screenshots](#screenshots)
* [Setup](#setup)
* [Usage](#usage)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)
<!-- * [License](#license) -->


## General Information
- PyInstallerGui is a python based GUI application to convert your python programs the windows executable application (.exe), with dependencies baked in.
- This is an easy to use application for beginner coders to start their scale and deployment of their cade and applications.
- The purpose of this project was to learn to import modules into tkinter and make a usable user friendly gui app for other learners
<!-- You don't have to answer all the questions - just the ones relevant to your project. -->


## Technologies Used
- Python - version 3.11
- PyInstaller - version 5.9.0



## Features
- Input box for file name
- input box for file location
- One click convert to .exe file


## Screenshots
<!--[Example screenshot](./img/screenshot.png)-->
<!-- If you have screenshots you'd like to share, include them here. -->


## Setup
This requires that PyInstaller be installed. instructions can be found here 

https://pyinstaller.org/en/stable/index.html

<!--Proceed to describe how to install / setup one's local environment / get started with the project.-->


## Usage
- Input in the Python file name (.py) to convert to .exe
- Input the location of the file to convert
- Press convert button

# Author: MichaelGuerrero@MGCodeSolutions

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


## Project Status
Open


## Room for Improvement
Open to sugestions...ALWAYS!

Room for improvement:


To do:
- Make this app an .exe for windows with all dependencies


## Contact
Created by [@MGCodeSolutions] mgcodesolutions@gmail.com - feel free to contact me!


<!-- Optional -->
<!-- ## License -->
<!-- This project is open source and available under the [... License](). -->

<!-- You don't have to include all sections - just the one's relevant to your project -->
