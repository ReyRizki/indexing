from wordInfo import wordInformation

class Node(object):
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
        
	def insert(self, word, file_number, index):
		if self.data.word == word:
			self.data.insertIndex(file_number, index)
		elif word < self.data.word:
			if self.left:
				return self.left.insert(word, file_number, index)
			else:
				self.left = Node(wordInformation(word))
				self.left.data.insertIndex(file_number, index)
		else:
			if self.right:
				return self.right.insert(word, file_number, index)
			else:
				self.right = Node(wordInformation(word))
				self.right.data.insertIndex(file_number, index)

	def find(self, d):
		if self.data == d:
			return True
		elif d < self.data and self.left:
			return self.left.find(d)
		elif d > self.data and self.right:
			return self.right.find(d)
		return False

	def preorder(self, l):
		l.append(self.data)
		if self.left:
			self.left.preorder(l)
		if self.right:
			self.right.preorder(l)
		return l

	def postorder(self, l):
		if self.left:
			self.left.postorder(l)
		if self.right:
			self.right.postorder(l)
		l.append(self.data)
		return l

	def inorder(self, l):
		if self.left:
			self.left.inorder(l)
		l.append((self.data.word, self.data.indexes))
		if self.right:
			self.right.inorder(l)
		return l
		
class BST(object):
	def __init__(self):
		self.root = None

	# return True if successfully inserted, false if exists
	def insert(self, word, file_number, index):
		if self.root:
			return self.root.insert(word, file_number, index)
		else:
			self.root = Node(wordInformation(word))
			self.root.data.insertIndex(file_number, index)

	# return True if d is found in tree, false otherwise
	def find(self, d):
		if self.root:
			return self.root.find(d)
		else:
			return False

	# return list of data elements resulting from preorder tree traversal
	def preorder(self):
		if self.root:
			return self.root.preorder([])
		else:
			return []

	# return list of postorder elements
	def postorder(self):
		if self.root:
			return self.root.postorder([])
		else:
			return []

	# return list of inorder elements
	def inorder(self):
		if self.root:
			return self.root.inorder([])
		else:
			return []