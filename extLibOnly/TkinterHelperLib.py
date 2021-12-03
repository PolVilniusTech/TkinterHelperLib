##AUTHOR - CARLY FREEDMAN
#This is a library for those who are not familiar with tkinter or who have not made a GUI before or just want their code to be more than just a boring black screen but are not really interested in UX Design.
#
#When I first got into programming I remember being very frustrated because I never wanted to learn any complicated GUI or UX skills but showing off my programs in a DOS '98 fashion was just ...unimpressive. Also, adding a UI really helped me advance my programming skills because you can have several 'pages' open at once and it expanded the options for what my programs could do. Hopefully this can help someone who was in my same position.

#At the moment, the library is made up of four functions which are listed and described below. I plan to update and expand the library soon. My next update should include the addWidget function allowing a type 'entry'. Let me know if you have any ideas for updates!(:

import logging
from os import path
from tkinter.scrolledtext import ScrolledText
from tkinter import Tk, Label, StringVar, Text, Button, Menu, END, INSERT
from PIL import Image, ImageTk


#   MAKEROOT FUNCTION:
#       purpose: makes "root" AKA a tkinter window object. This is like the blank page where you will place your widget(s)
#       input arguments:
#           REQUIRED:
#               title : string containing name for your window/gui/root
#           OPTIONAL:
#               size: string containing size for your window/gui/root in the format: ('pixelSize1xpixelSize2') where pixelSizes are ints. e.g., default is ('1000x500')
#               bg : color of background of window/gui/root. See tkinter docs for acceptable types. 

def makeRoot(title, size = '1000x500', bg = None):
    root = Tk()
    root.geometry(size)
    root.title(title)
    if bg is not None:
        root.config(bg = bg)
    return root



#    ADDWIDGET FUNCTION(s):
#        purpose: simplify methods of label, text, button, and menu widgets from tkinter. This function should make it easier for those not as familiar with tkinter to benefit from the package. Increases program runtime efficiency by 30% for those who do not wish to make an extremely complicated GUI. 
#        input arguments:
#
#            REQUIRED:
#           |
#           |    widget type Options :
#           |   |
#           |   |     'labelType' : text label widget. Modifiable values are text, font, bg, fg, padx, pady
#           |   |     'textType' : textbox widget where both developer and user may input text. Modifiable values are height, width, font, bg, fg, padx, pady
#           |   |     'buttonType' : button widget. Can hold text and also run a function upon user's click. Modifiable Values are text, width, font, bg, fg, buttonCmd, buttonCmdArgs, padx, pady
#           |   |      'menuType' : menu located at top of root containing series of buttons. Modifiable values are: menuLabels, menuCmds
#           |   |
#           |   |      'imageType' : image with the label, if image exists. Otherwise only label.
#           |    root : tkinter (tk) window object in which the widget is to be placed. NOTE: for some widgets, root can be replaced with frame. see tkinter docs for more info on which widgets this applies to
#           |
#            RECOMMENDED (without provided parameters new widgets placed on the grid at coordinates (0, 0)):
#           |    row : addWidget positions objects in the root/frame using a grid. In order to prevent overlap of widgets, keep track of where you want each to be placed. Applicable to all widgets except menu which is always placed at top of window.
#           |    column : addWidget positions objects in the root/frame using a grid. In order to prevent overlap of widgets, keep track of where you want each to be placed.
#            OPTIONAL (hint-- you can call this function with or without some or all of the following variables):
#           |    text : string holding the text to be displayed within the widget. Applicable to widget types label and button. 
#           |    height : int representing height of widget in pixels. Applicable only to widget type text.
#           |    width : int representing height of widget in pixels. Applicable to widget type text and button.
#           |    padx : int representing how many pixels on the x-axis (horizontally) you want to add of whitespace around the widget. Applicable to all widgets except menu which is always placed at top of window.
#           |    font : int representing font size. Applicable to all widgets except menu which is always placed at top of window.
#           |    insert : text string containing text you wish to insert into the text box you are creating. Applicable only to widget type text.
#           |    buttonCmd : function to be called upon user pressing button. Applicable only to widget type button.
#           |    buttonCmdArgs : parameter(s) of function being called upon user pressing button. Can be array or single variable. Applicable only to widget type button.
#           |    bg : color of background of widget. See tkinter docs for acceptable types. Applicable to all widgets except menu which is always placed at top of window.
#           |    fg : color of text (foreground) of widget. See tkinter docs for acceptable types. Applicable to all widgets except menu which is always placed at top of window.
#           |    pady : int representing how many pixels on the y-axis (vertically) you want to add of whitespace around the widget. Applicable to all widgets except menu which is always placed at top of window.
#           |    scrollable : boolean representing whether or not you want a scrollbar to display along with text box widget. Applicable only to widget type text.
#           |    menuLabels : String(s) that you wish to display as the possible menu buttons. Accepts array of strings or single string. Applicable only to widget type menu.
#           |    menuCmds : function(s) that you wish to be called upon user clicking menu buttons. Order and length must be compatible to menuLabels. Applicable only to widget type menu.
#           |    imageName : filaname of the Picture File.
#     output:
#           res : tkinter widget

row=0
column=0
text=None
padx=0
pady=0
font=None
bg=None
fg=None

def addLabelWidget(root, labelType=(row, column, text, padx, pady, font, bg, fg)):
	
	res = Label(root, text=labelType[2], font=labelType[5], bg=labelType[6], fg=labelType[7])
	
	res.grid(row=labelType[0], column=labelType[1], padx=labelType[3], pady=labelType[4])
	
	return res


row = 0
column = 0
height = None
width = None
padx = 0
pady = 0
font = None
bg = None
fg = None
insert = False
scrollable = False

def addTextWidget(root, textType=(row, column, height, width, padx, pady, font, bg, fg, insert, scrollable)):
	
	if textType[10]:
		res = ScrolledText(root, height=textType[2], width=textType[3], font=textType[6], bg=textType[7], fg=textType[8])
	else:
		res = Text(root, height=textType[2], width=textType[3], font=textType[6], bg=textType[7], fg=textType[8])
	
	if textType[9]:
		insertLine(res, textType[9])
	
	res.grid(row=textType[0], column=textType[1], padx=textType[4], pady=textType[5])
	
	return res


row = 0
column = 0
text = None
width = None
padx = 0
pady = 0
font = None
bg = None
fg = None
buttonCmd = None
buttonCmdArgs = None

def addButtonWidget(root, buttonType=(row, column, text, width, padx, pady, font, bg, fg, buttonCmd, buttonCmdArgs)):
	
	newText = StringVar()
	newText.set(buttonType[2])
	
	if buttonType[9] is None:
		logging.error('Error', 'submitButton')
	
	if buttonType[10] is not None:
		res = Button(root, textvariable=newText, width=buttonType[3], font=buttonType[6], bg=buttonType[7], fg=buttonType[8], command=lambda:buttonType[9](buttonType[10]))
	else:
		res = Button(root, textvariable=newText, width=buttonType[3], font=buttonType[6], bg=buttonType[7], fg=buttonType[8], command=lambda:buttonType[9]())
	
	res.grid(row=buttonType[0], column=buttonType[1], padx=buttonType[4], pady=buttonType[5])
	
	return res


menuLabels = None
menuCmds = None

def addMenuWidget(root, menuType=(menuLabels, menuCmds)):
	
	res = Menu(root)
	
	if menuType[0] is not None and menuType[1] is not None:
		i = 0
		
		for label in menuType[0]:
			if i < len(menuType[1]):
				res.add_command(label=label, command=menuType[1][i])
			
			i += 1
		
		root.config(menu = res)
		return res
	else:
		return


row = 0
column = 0
text = None
padx = 0
pady = 0
font = None
bg = None
fg = None
imageName = None

def addImageWidget(root, imageType=(row, column, text, padx, pady, font, bg, fg, imageName)):
	
	if imageType[8] is not None and path.exists(imageType[8]):
		logo = Image.open(imageType[8])
		logo = ImageTk.PhotoImage(logo)
		res = Label(root, text=imageType[2], font=imageType[5], bg=imageType[6], fg=imageType[7], image=logo)
		res.image = logo
	else:
		res = Label(root, text=imageType[2], font=imageType[5], bg=imageType[6], fg=imageType[7])
	
	res.grid(row=imageType[0], column=imageType[1], padx=imageType[3], pady=imageType[4])
	
	return res


#   GETLINE FUNCTION:
#       Purpose:
#           retrieves line(s) from text widget
#       input arguments (all required): 
#           txtBox : tkinter text widget containing the text you wish to retrieve
#           lineNum : int or array of int containing the line number(s) you wish to retrieve
#       output: 
#           res : string or array of strings containing text from text box
def getLine(txtBox, lineNum):
    res = []
    if type(lineNum) is int:
        return txtBox.get((str(lineNum) + '.0'), END)
    else:
        for line in lineNum:
            s = str(line) + '.0'
            res.append(txtBox.get(s, END))
    return res
     

#   INSERTLINE FUNCTION:
#       Purpose:
#           inputs line to text widget
#       input arguments: 
#           txtBox : tkinter text widget containing the text you wish to retrieve
#           insert : string you wish to insert
def insertLine(txtBox, insert):
    txtBox.insert(INSERT, insert)
