#!/usr/bin/python
#GUI thanks to TkinerHelperLib Author

import sys

sys.path.insert(0,'/path_to_the/TkinterHelperLib/')

from TkinterHelperLib import makeRoot, addWidget

def hello():
	print('Hello')

def bye():
	print('Bye')

root = makeRoot(title='Name', size='1000x500', bg=None)

addWidget('menu', root, row = 0, column = 0, text = None, height = None, width = None, padx = 0, font = None, insert = None, buttonCmd = None, buttonCmdArgs = None, bg = None, fg = None, pady = 0, scrollable = False, menuLabels = ('Hello One','Hello Two'), menuCmds = (hello, hello), imageName = None)

addWidget('button', root, row = 1, column = 0, text = 'Bye Button', height = None, width = None, padx = 0, font = None, insert = None, buttonCmd = bye, buttonCmdArgs = None, bg = None, fg = None, pady = 0, scrollable = False, menuLabels = None, menuCmds = None, imageName = None)

addWidget('text', root, row = 2, column = 0, text = 'Hello Text', height = 5, width = 10, padx = 0, font = None, insert = None, buttonCmd = None, buttonCmdArgs = None, bg = None, fg = None, pady = 0, scrollable = True, menuLabels = None, menuCmds = None, imageName = None)

addWidget('label', root, row = 3, column = 0, text = 'Hello World', height = None, width = None, padx = 0, font = None, insert = None, buttonCmd = None, buttonCmdArgs = None, bg = None, fg = None, pady = 0, scrollable = False, menuLabels = None, menuCmds = None, imageName = None)

addWidget('image', root, row = 4, column = 0, text = 'The Lock', height = None, width = None, padx = 0, font = None, insert = None, buttonCmd = None, buttonCmdArgs = None, bg = None, fg = None, pady = 0, scrollable = False, menuLabels = None, menuCmds = None, imageName = 'filename.png')

root.mainloop()
