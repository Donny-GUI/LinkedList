
class LinkedList:
	def __init__(self):
		self.head = None

	def __iter__(self):
		""" Iterates through the loop and yields each node"""
		node = self.head
		while node is not None:
			yield node
			node = node.next

	def insertFirst(self, node):
		""" Insert new node at the first position """
		node.next = self.head
		self.head = node

	def insertLast(self, node):
		""" Insert new node at last position """
		if self.head is None:
			self.head = node
			return
		for current_node in self: 
			pass
		current_node.next = node

	def insertAfter(self, target_data, new_node):
		""" Finds the target node and inserts the new node after it"""
		if self.head is None:
			raise Exception("Empty List -- Can not insert a new node after a node that does not exist")
		for node in self:
			if node.data == target_data:
				new_node.next = node.next
				node.next = new_node
				return
		raise Exception("Target 404 -- Target node not in List")

	def insertBefore(self, target_data, new_node):
		""" Finds the target Node and inserts it before the node, without knowing the previous node """
		if self.head is None:
			raise Exception("Empty List -- Can not insert a new node before a node that does not exist")
		for node in self:
			if node.next == target_data:
				node.next = new_node
				new_node.next = target_data
				return
		raise Exception("Target 404 -- Node Not found in List")

	def remove(self, target_data):
		""" Remove a target Node """
		if self.head is None:
			raise Exception("Empty List -- No data to remove from list.")
		if self.head.data == target_data:
			self.head = self.head.next
			return
		node_before = self.head
		for node in self:
			if node.data == target_data:
				node_before.next = node.next
				return
			node_before = node
		raise Exception("Target 404 -- Target Node Not in List")


	def show(self):
		""" Print the List out with arrows to visualize """
		node = self.head
		nodes = []
		while node is not None:
			nodes.append(node.data)
			node = node.next
		nodes.append("None")
		print("->".join(nodes))


class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
