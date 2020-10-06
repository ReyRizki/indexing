from bst import BST

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
            tree.insert(word, file_name)
    
    file1.close()

tree = BST()

fileToTree(tree, 'test_file.txt')

print(tree.search('BTS'))