#!/usr/bin/python
#GUI thanks to TkinerHelperLib Author

import sys

sys.path.insert(0,'/path_to_the/TkinterHelperLib/')

from TkinterHelperLib import makeRoot, addWidget

class myRequestData:
	
#   tupleDictReq = {
#   'label' : labelType = (row, column, padx, pady, text, font, bg, fg)
#   'text'  : textType = (row, column, padx, pady, height, width, font, bg, fg, insert, scrollable)
#   'button': buttonType = (row, column, padx, pady, text, width, font, bg, fg, buttonCmd, buttonCmdArgs)
#   'menu'  : menuType = (menuLabels, menuCmds)
#   'image' : imageType = (row, column, padx, pady, text, font, bg, fg, imageName)	
	
	reqData = {}

	def __init__(self):
		self.reqData['label'] = self.prepLabel()
		self.reqData['text'] = self.prepText()
		self.reqData['button'] = self.prepButton()
		self.reqData['menu'] = self.prepMenu()
		self.reqData['image'] = self.prepImage()
			
	def prepLabel(self):
		labelType = (0, 0, 0, 0, None, None, None, None)
		return labelType
			
	def prepText(self):
		textType = (0, 0, 0, 0, None, None, None, None, None, False, False)
		return textType
					
	def prepButton(self):
		buttonType = (0, 0, 0, 0, None, None, None, None, None, None, None)
		return buttonType
					
	def prepMenu(self):
		menuType = (None, None)
		return menuType
					
	def prepImage(self):
		imageType = (0, 0, 0, 0, None, None, None, None, None)
		return imageType
			
	def getEnvironment(self):
		return self.reqData
	
	def setEnvironment(self, type, newValues):
		if type == 'label':
			self.reqData['label'] = newValues
			self.reqData['text'] = self.prepText()
			self.reqData['button'] = self.prepButton()
			self.reqData['menu'] = self.prepMenu()
			self.reqData['image'] = self.prepImage()
		elif type == 'text':
			self.reqData['label'] = self.prepLabel()
			self.reqData['text'] = newValues
			self.reqData['button'] = self.prepButton()
			self.reqData['menu'] = self.prepMenu()
			self.reqData['image'] = self.prepImage()
		elif type == 'button':
			self.reqData['label'] = self.prepLabel()
			self.reqData['text'] = self.prepText()
			self.reqData['button'] = newValues
			self.reqData['menu'] = self.prepMenu()
			self.reqData['image'] = self.prepImage()
		elif type == 'menu':
			self.reqData['label'] = self.prepLabel()
			self.reqData['text'] = self.prepText()
			self.reqData['button'] = self.prepButton()
			self.reqData['menu'] = newValues
			self.reqData['image'] = self.prepImage()
		elif type == 'image':
			self.reqData['label'] = self.prepLabel()
			self.reqData['text'] = self.prepText()
			self.reqData['button'] = self.prepButton()
			self.reqData['menu'] = self.prepMenu()
			self.reqData['image'] = newValues


data = myRequestData()
env = data.getEnvironment()

#print(env)
#print(env['image'])
#print(env['image'][0])

def hello():
	print('Hello')

def bye(args):
	for person in args:
		print('Bye ' + person)

root = makeRoot(title='Name', size='1000x500', bg=None)

data.setEnvironment('menu', (('Hello One','Hello Two'), (hello, hello)))
addWidget('menu', root, data.getEnvironment())

data.setEnvironment('button', (1, 0, 0, 0, 'Bye Button', 12, None, None, None, bye, ('Alice', 'Bob')))
print(env)
addWidget('button', root, data.getEnvironment())

data.setEnvironment('text', (2, 0, 0, 0, 5, 10, None, None, None, 'Hello Text', True))
addWidget('text', root, data.getEnvironment())

data.setEnvironment('label', (3, 0, 0, 0, 'Hello World', None, None, None))
addWidget('label', root, data.getEnvironment())

data.setEnvironment('image', (4, 0, 0, 0, 'The Lock', None, None, None, 'lock.png'))
addWidget('image', root, data.getEnvironment())

root.mainloop()
