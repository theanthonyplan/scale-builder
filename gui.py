#tkinter ui module
from Tkinter import *
from scaler import *

#CALLBACK FUNCTIONS
def drawScale():
	n = letter_to_number[note.get()]
	s = scale_selection.get()
	output = str(buildScale(n,s))
	t.set(output)
def reset():
	t.set('Select a root note and scale type, then press build')
def printAbout():
	print "Scaler(early-alpha)"
	print "This build is scaler1.0"
	print "Anthony Gagliardo 2012"

#ROOT AND CONTENT WINDOWs
root = Tk()
root.title("scaler gui(alpha)")

content = Frame(root).grid()
#CONTROL MENU
menubar = Menu(content)
menubar.add_command(label="About", command=printAbout)
menubar.add_command(label="Quit",command=root.quit)
root.config(menu=menubar)

#REPORT LABEL
t = StringVar()
reset()

Label(content, textvariable=t, height=3, width=40).grid(row=1,column=0,columnspan=3,sticky=E+W)

#MENUS
#note menu
note = StringVar()
note.set('-')
note_options = fullScale
OptionMenu(content, note, *note_options).grid(row=2,column=0,sticky=EW)
#scaletype menu
scale_selection = StringVar()
scale_selection.set('-')
scale_options = scaleMapper.values()
OptionMenu(content, scale_selection, *scale_options).grid(row=2,column=1,sticky=EW)

#BUTTONS
Button(content, text="Build it!", command=drawScale ).grid(row=2,column=3,sticky=EW)
Button(content, text="reset", command=reset ).grid(row=2,column=4,sticky=W)


#MAINLOOP
root.mainloop()

