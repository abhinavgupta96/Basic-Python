class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class BST :

    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True): ##we need to return to break out the loop
            if new_node.value == temp.value:
                return False
            if new_node.value > temp.value:
                if temp.right is not None:
                    temp = temp.right
                else:
                    temp.right = new_node
                    return True
            else :
                if temp.left is not None:
                    temp = temp.left
                else:
                    temp.left = new_node
                    return True

    def contains(self, value):
        if self.root is None:
            return False
        temp = self.root
        while temp is not None:
            if temp.value > value :
                temp = temp.left
            elif temp.value < value:
                temp = temp.right
            else :
                return True
        return False

    def min_value_node(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value

    def remove_node(self, value):
        ##Function working, but better and complete at below link
        ##See > https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/
        temp = self.root
        while (True):
            if temp.value < value:
                temp = temp.right
            elif temp.value > value:
                temp = temp.left
            elif temp.value == value:
                print("Found the value, processing")
                if temp.left == None and temp.right == None:
                    temp.value = None
                    print("Removing the node")
                    return True
                else:
                    print("Cannot remove node as child node exists")
                    return False
            else:
                print("Value not found")
                return False


mybst = BST()
mybst.insert(45)
mybst.insert(21)
mybst.insert(17)
mybst.insert(89)
mybst.insert(65)
mybst.insert(39)
mybst.insert(97)
mybst.insert(1)
# print(mybst.min_value_node(mybst.root.right.right))
#mybst.remove_node(97)
print(mybst.contains(97))