from bst import BST

tree = BST()

tree.insert("Rey", 1, (10, 5))
tree.insert("Ganteng", 1, (3, 7))
tree.insert("Rey", 5, (20, 1))
tree.insert("Rey", 1, (11, 2))

print(tree.inorder())
