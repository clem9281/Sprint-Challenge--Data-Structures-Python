class BinarySearchTree:
    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None
    def __str__(self):
        return f"{self.value}"
    
    # Insert the given value into the tree
    def insert(self, value):
        if not self.value:
            self.value = value
        elif value < self.value:
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        elif value > self.value:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
        
                
            

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == None:
            return False
        if self.value == target:
            return True
        if target < self.value:
            if not self.left:
                return False
            return self.left.contains(target)
        elif target > self.value:
            if not self.right:
                return False
            return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
       if not self.right:
           return self.value
       else:
           return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)
            
    def in_order_print(self, node):
        if node == None:
            return
        self.in_order_print(node.left)
        print(node.value)
        self.in_order_print(node.right)

