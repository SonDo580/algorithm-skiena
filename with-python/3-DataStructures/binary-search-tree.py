class TreeNode:
    def __init__(self, val, parent = None):
        self.val = val
        self.parent = parent
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def search(self, x):
        return self.__search(self.root, x)
        
    def __search(self, tree, x):
        if tree is None:
            return None
        
        if x == tree.val:
            return tree
        elif x < tree.val:
            return self.__search(tree.left, x) 
        else:
            return self.__search(tree.right, x) 
    
    def find_min(self):
        return self.__find_min(self.root)
    
    def __find_min(self, tree):
        if tree is None:
            return None
        
        current = tree
        while current.left is not None:
            current = current.left
        return current 
    
    def find_max(self):
        return self.__find_max(self.root)
    
    def __find_max(self, tree):
        if tree is None:
            return None
        
        current = tree
        while current.right is not None:
            current = current.right
        return current 
    
    def insert(self, x):
        self.root = self.__insert(self.root, x)
        
    def __insert(self, tree, x, parent=None):
        if tree is None:
            return TreeNode(x, parent)

        if x < tree.val:
            tree.left = self.__insert(tree.left, x, tree)
        elif x > tree.val:
            tree.right = self.__insert(tree.right, x, tree)
        
        return tree

    def in_order_traverse(self, func):
        self.__in_order_traverse(self.root, func)
    
    def __in_order_traverse(self, tree, func):
        if tree is not None:
            self.__in_order_traverse(tree.left)
            func(tree.val)
            self.__in_order_traverse(tree.right)

    def delete(self, x):
        self.root = self.__delete(self.root, x)

    def __delete(self, tree, x):
        if tree is None:
            return None
        
        if x < tree.val:
            tree.left = self.__delete(tree.left, x)
        elif x > tree.val:
            tree.right = self.__delete(tree.right, x)
        else:
            # node is leaf
            if tree.left is None and tree.right is None:
                return None
            
            # node has only right child
            if tree.left is None:
                return tree.right
            
            # node has only left child
            if tree.right is None:
                return tree.left
            
            # node has 2 children
            # replace current node with min node of the right subtree
            min_node = self.__find_min(tree.right)
            tree.val = min_node.val
            tree.right = self.__delete(tree.right, min_node.val)

# Usage
def main():
    bst = BinarySearchTree()
    
    # Insert elements
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(2)
    bst.insert(4)
    bst.insert(6)
    bst.insert(8)

    # In-order traverse - print each node's value
    print("In-order traverse:")
    bst.in_order_traverse(lambda node: print(node.val, end=" "))
    print()

    # Search
    for search_val in [4, 9]:
        found_node = bst.search(search_val)
        if found_node:
            print(f"{search_val} found")
        else:
            print(f"{search_val} not found.")

    # Find minimum value
    min_node = bst.find_min()
    if min_node:
        print(f"Minimum value: {min_node.val}")
    else:
        print("Tree is empty.")

    # Find maximum value
    max_node = bst.find_max()
    if max_node:
        print(f"Maximum value: {max_node.val}")
    else:
        print("Tree is empty.")

if __name__ == "__main__":
    main()