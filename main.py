from bst import BST

tree = BST()

tree.insert("Rey", "UwU")
tree.insert("Ganteng", "UwU")
tree.insert("Rey", "LOL")
tree.insert("Rey", "UwU")

print(tree.inorder())

print(tree.search("Rey"))
print(tree.search("Jelek"))