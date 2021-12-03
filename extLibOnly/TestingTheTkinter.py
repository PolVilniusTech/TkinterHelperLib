#!/usr/bin/python
#GUI thanks to TkinerHelperLib Author

import sys

sys.path.insert(0,'/path_to_the/TkinterHelperLib/')

from TkinterHelperLib import makeRoot, addMenuWidget, addButtonWidget, addTextWidget, addLabelWidget, addImageWidget

def hello():
	print('Hello')

def bye():
	print('Bye')

root = makeRoot(title='Name', size='1000x500', bg=None)

addMenuWidget(root, (('Hello One','Hello Two'), (hello, hello)))

addButtonWidget(root, (1, 0, 'Bye Button', 13, 0, 0, None, None, None, bye, None))

addTextWidget(root, (2, 0, 4, 12, 0, 0, None, None, None, 'Hello Text', False))

addLabelWidget(root, (3, 0, 'Hello World', 0, 0, None, None, None))

addImageWidget(root, (4, 0, 'The Lock', 0, 0, None, None, None, 'lock.png'))

root.mainloop()
