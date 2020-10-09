from bst import BST
import re

def preprocessText(s):
    return re.sub(r'[^\w\s]', '', s).lower()

def fileToTree(tree, file_name):
    file1 = open(file_name, 'r') 
    while True:
        # Get next line from file 
        line = file1.readline() 
    
        # if line is empty 
        # end of file is reached 
        if not line: 
            break
        
        line = line.split(' ')

        for word in line:
            tree.insert(preprocessText(word), file_name)
    
    file1.close()

def generateTree(files):
    tree = BST()

    for file in files:
        fileToTree(tree, file)

    return tree

n = int(input("Number of files: "))
files = []

print("File names:")
for _ in range(n):
    files.append(str(input()))

tree = generateTree(files)

again = 'y'

while again != 'n' and again != 'N':
    key = input("Search key: ")

    print(tree.search(preprocessText(key)))

    again = input("Search again? (Y/N) ")