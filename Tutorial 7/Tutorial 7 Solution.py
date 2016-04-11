# Data Structures & Algorithms
# Tutorial 7: Stack
# Name: TODO Write your name here
# NPM: TODO Write your NPM here

from html.parser import HTMLParser

class ListNode:
	'''This class represents a node in a singly linked list 
	implementation.'''

	def __init__(self, d=None, n=None):
		self._data = d
		self._next = n

	def getData(self):
		return self._data

	def getNext(self):
		return self._next

	def insert(self, d):
		# Insert a new node immediately after this node
		self._next = ListNode(d, self._next)

	def delete(self):
		# Remove the node immediately after this node
		try:
			self._next = self._next._next
		except AttributeError:
			return
		
	def printList(self):
		# Step through list, outputting each item
		n = self
		while n is not None:
			print(n._data)
			n = n._next

	def __str__(self):
		if self._data is None:
			return ''
		else:
			return self._data

class ListItr:

	def __init__(self, list):
		self._list = list
		self._current = list._header

	def __iter__(self):
		return self

	def __next__(self):
		self._current = self._current._next
		if self._current is not None:
			return self._current
		else:
			raise StopIteration

class MyStack:

	def __init__(self, top=ListNode()):
		self._top = top

	def isEmpty(self):
		return self._top.getNext() is None

	def push(self, d):
		'''Inserts d as new node on top of the stack.'''
		# TODO Implement me
		self._top = ListNode(d, self._top)
##		print("Pushed {}".format(d))

	def pop(self):
		'''Returns and removes the first data in the topmost node in the 
		stack.'''
		# TODO Implement me
		node = self._top
		self._top = self._top.getNext()
##		print("Popped {}".format(node._data))
		return node

	def __len__(self):
		'''Returns the number of elements in the stack.'''
		current = self._top
		count = 0

		while current.getNext() is not None:
			current = current.getNext()
			count = count + 1

		return count

class MyHTMLParser(HTMLParser):

	def __init__(self):
		super().__init__()
		self._stack = MyStack()
		self._valid = True

	def isValidDocument(self):
		return self._valid

	def handle_starttag(self, tag, attrs):
		# TODO Implement me
		print("Encountered start tag: {}".format(tag))
		self._stack.push(tag)

	def handle_endtag(self, tag):
		if self._valid is True:
			# TODO Implement me
			print("Encountered end tag: {}".format(tag))
			if self._stack.isEmpty():
				self._valid = False
			else:
				node = self._stack.pop()
				if node._data != tag:
					print("{} != {}".format(node._data, tag))
					self._valid = False
	
	def feed(self, data):
		super().feed(data)
		# TODO Implement me
		if len(self._stack):
			self._valid = False
		else:
			self._valid = True

def main():
	dummyHTML1 = '<html><head><title>Hello World</title></head>' + \
			'<body><h1>Hello Hello</h1></body></html>'

	dummyHTML2 = '<html><head><title>Hello World</title></head>' + \
			'<body><h1>Hello Hello<h1></body></html>'
	
	parser = MyHTMLParser()
	# Put any string containing HTML documents into the parser
	parser.feed(dummyHTML2)
	parser.close()

	if parser.isValidDocument() is True:
		print("HTML document is valid.")
	else:
		print("HTML document is invalid.")

if __name__ == "__main__":
	main()
