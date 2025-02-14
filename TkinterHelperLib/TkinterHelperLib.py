##AUTHOR - CARLY FREEDMAN
#This is a library for those who are not familiar with tkinter or who have not made a GUI before or just want their code to be more than just a boring black screen but are not really interested in UX Design.
#
#When I first got into programming I remember being very frustrated because I never wanted to learn any complicated GUI or UX skills but showing off my programs in a DOS '98 fashion was just ...unimpressive. Also, adding a UI really helped me advance my programming skills because you can have several 'pages' open at once and it expanded the options for what my programs could do. Hopefully this can help someone who was in my same position.

#At the moment, the library is made up of four functions which are listed and described below. I plan to update and expand the library soon. My next update should include the addWidget function allowing a type 'entry'. Let me know if you have any ideas for updates!(:

from os import path
from tkinter.scrolledtext import ScrolledText
from tkinter import Tk, Label, Text, Button, Menu, END, INSERT
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



#    ADDWIDGET FUNCTION:
#        purpose: combines methods of label, text, button, and menu widgets from tkinter. This function should make it easier for those not as familiar with tkinter to benefit from the package. Increases program runtime efficiency by 30% for those who do not wish to make an extremely complicated GUI. 
#        input arguments:
#
#            REQUIRED:
#           |
#           |    type : string representing type of widget to be added. Options are:
#           |   |
#           |   |     'label' : text label widget. Modifiable values are text, font, bg, fg, padx, pady
#           |   |     'text' : textbox widget where both developer and user may input text. Modifiable values are height, width, font, bg, fg, padx, pady
#           |   |     'button' : button widget. Can hold text and also run a function upon user's click. Modifiable Values are text, width, font, bg, fg, buttonCmd, buttonCmdArgs, padx, pady
#           |   |      'menu' : menu located at top of root containing series of buttons. Modifiable values are: menuLabels, menuCmds
#           |   |      'image' : image or simple text 
#           |    root : tkinter (tk) window object in which the widget is to be placed. NOTE: for some widgets, root can be replaced with frame. see tkinter docs for more info on which widgets this applies to
#           |
#            RECOMMENDED (hint-- you can ignore these when calling the function, but if you plan on using it more than once on the same root or frame it will result in things getting very messy as it will always place the new widget on the grid at coordinates (0, 0)):
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
#     output:
#           res : tkinter widget

def addWidget(type, root, row = 0, column=0, text = None, height = None, width = None, padx = 0, font = None, insert = None, buttonCmd = None, buttonCmdArgs = None, bg = None, fg = None, pady = 0, scrollable = False, menuLabels = None, menuCmds = None, imageName = None):
    if type == 'label':
        res = Label(root, text=text, font=font, bg = bg, fg = fg)
    elif type == 'text':
        if scrollable:
            res = ScrolledText(root, height = height, width = width, font = font, bg = bg, fg = fg)
        else:
            res = Text(root, height=height, width=width, font = font, bg = bg, fg = fg)
    elif type == 'button':
        if buttonCmdArgs is not None:
            res = Button(root, text=text, width=width, font=font, bg=bg, fg=fg, command=lambda : buttonCmd(buttonCmdArgs))
        else: 
            res = Button(root, text=text, width=width, font=font, bg=bg, fg=fg, command=lambda : buttonCmd())
    elif type == 'menu':
        res = Menu(root)
        if menuLabels is not None and menuCmds is not None:
            i = 0
            for label in menuLabels:
                if i < len(menuCmds):
                    res.add_command(label=label, command = menuCmds[i])
                i += 1
            root.config(menu = res)
            return res
    elif type == 'image':
        if imageName is not None and path.exists(imageName):
            logo = Image.open(imageName)
            logo = ImageTk.PhotoImage(logo)
            res = Label(root, text = text, font = font, bg = bg, fg = fg, image = logo)
       else:
            res = Label(root, text = text, font = font, bg = bg, fg = fg)
    else:
        return
        
    if insert is not None:
        insertLine(res, insert)

    res.grid(row = row, column = column, padx=padx, pady = pady)
    
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
