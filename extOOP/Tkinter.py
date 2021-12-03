#!/usr/bin/python
#GUI thanks to TkinerHelperLib Author

import TkinterHelperLib as tkhl

class myRequestData:

	reqData = {}

	def __init__(self):
		self.prepare()
		
	def prepare(self):
		self.reqData['row'] = 0
		self.reqData['column'] = 0
		self.reqData['text'] = None
		self.reqData['height'] = None
		self.reqData['width'] = None
		self.reqData['padx'] = 0
		self.reqData['font'] = None
		self.reqData['insert'] = None
		self.reqData['buttonCmd'] = None
		self.reqData['buttonCmdArgs'] = None
		self.reqData['bg'] = None
		self.reqData['fg'] = None
		self.reqData['pady'] = 0
		self.reqData['scrollable'] = False
		self.reqData['menuLabels'] = None
		self.reqData['menuCmds'] = None
			
	def getEnvironment(self):
		return self.reqData
		
	def insertWidget(self, type, root):
		tkhl.addWidget(type, root, self.reqData['row'], self.reqData['column'], self.reqData['text'], self.reqData['height'], self.reqData['width'], self.reqData['padx'], self.reqData['font'], self.reqData['insert'], self.reqData['buttonCmd'], self.reqData['buttonCmdArgs'], self.reqData['bg'], self.reqData['fg'], self.reqData['pady'], self.reqData['scrollable'], self.reqData['menuLabels'], self.reqData['menuCmds'])
		self.prepare()
	
	def setLabelEnvironment(self, root, row, column, padx, pady, text, font, bg, fg):
		self.reqData['row'] = row
		self.reqData['column'] = column
		self.reqData['padx'] = padx
		self.reqData['pady'] = pady
		self.reqData['text'] = text
		self.reqData['font'] = font
		self.reqData['bg'] = bg
		self.reqData['fg'] = fg
		self.insertWidget('label', root)
	
	def setTextEnvironment(self, root, row, column, padx, pady, height, width, font, bg, fg, insert, scrollable):
		self.reqData['row'] = row
		self.reqData['column'] = column
		self.reqData['padx'] = padx
		self.reqData['pady'] = pady
		self.reqData['height'] = height
		self.reqData['width'] = width
		self.reqData['font'] = font
		self.reqData['bg'] = bg
		self.reqData['fg'] = fg
		self.reqData['insert'] = insert
		self.reqData['scrollable'] = scrollable
		self.insertWidget('text', root)

	def setButtonEnvironment(self, root, row, column, padx, pady, text, width, font, bg, fg, buttonCmd, buttonCmdArgs):
		self.reqData['row'] = row
		self.reqData['column'] = column
		self.reqData['padx'] = padx
		self.reqData['pady'] = pady
		self.reqData['text'] = text
		self.reqData['width'] = width
		self.reqData['font'] = font
		self.reqData['bg'] = bg
		self.reqData['fg'] = fg
		self.reqData['buttonCmd'] = buttonCmd
		self.reqData['buttonCmdArgs'] = buttonCmdArgs
		self.insertWidget('button', root)
	
	def setMenuEnvironment(self, root, menuLabels, menuCmds):
		self.reqData['menuLabels'] = menuLabels
		self.reqData['menuCmds'] = menuCmds
		self.insertWidget('menu', root)


mrd = myRequestData()

def hello():
	print('Hello')

def bye():
	print('Bye')

root = tkhl.makeRoot(title='Name', size='1000x500', bg=None)

#   'menu'  |  (root, menuLabels, menuCmds)
mrd.setMenuEnvironment(root, ('Hello One','Hello Two'), (hello, hello))

#   'button' | (root, row, column, padx, pady, text, width, font, bg, fg, buttonCmd, buttonCmdArgs)
mrd.setButtonEnvironment(root, 1, 0, 0, 0, 'Bye Button', None, None, None, None, bye, None)

#   'text'  | (root, row, column, padx, pady, height, width, font, bg, fg, insert, scrollable)
mrd.setTextEnvironment(root, 2, 0, 0, 0, 5, 10, None, None, None, None, True)

#   'label' | (root, row, column, padx, pady, text, font, bg, fg)
mrd.setLabelEnvironment(root, 3, 0, 0, 0, 'Hello World', None, None, None)

root.mainloop()
