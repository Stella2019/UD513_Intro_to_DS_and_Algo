class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        
        new_node = Node( new_val )
        
        
        if None == self.root :
            # empty tree
            
            self.root = new_node
            
        else:
            # non-empty tree
            current = self.root
            
            while current != None:
                
                if new_val > self.root.value:
                    # move to right subtree to find vacancy
                    current = current.right
                else:
                    # move to left subtree to find vacancy
                    current = current.left
            
            current = new_node
            
        pass



    def search(self, find_val):
        
            
        current = self.root
        while current != None:
            
            if find_val == current.value:
                return True
                
            elif find_val > current.value:
                current = current.right
                
            else:
                current = current.left
        
        return False
    
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print( tree.search(4) )
# Should be False
print( tree.search(6) )