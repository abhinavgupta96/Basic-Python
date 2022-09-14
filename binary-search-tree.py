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

    def inorder_successor(self): #this function is used to create a list with all the nodes in their order of traversal i.e inorder traversal
        inorder_st = []
        inorder_list = []
        temp = self.root
        while True:
            if temp is not None:
                inorder_st.append(temp)
                temp = temp.left
            elif inorder_st:
                temp = inorder_st.pop()
                inorder_list.append(temp.value)
                temp = temp.right
            else:
                break
        return inorder_list

    def find_parent(self,value): #this function helps in finding parent node of a given value
        temp = self.root
        parent = None
        while True:
            parent = temp
            if value > temp.value:
                temp = temp.right
                if temp.value == value:
                    return parent
            elif value < temp.value:
                temp = temp.left
                if temp.value == value:
                    return parent
            elif value == temp.value:
                return parent
        return ("No Parent")

            
    def remove_node(self,value): #add logic to handle nodes with single child or no child
        inorder_list = self.inorder_successor()
        value_index = inorder_list.index(value)
        successor = inorder_list[value_index+1] #get the value of successor
        temp = self.root
        parent_node = self.find_parent(successor) #get the parent node of successor node, helps in deleting successor node
        while True:
            if temp.value > value:
                temp = temp.left
            elif temp.value < value:
                temp = temp.right
            elif temp.value == value:
                temp.value = successor
                if value > parent_node.value: #This allows parent node to delete the successor node from original position as it will now have replaced the deleted node
                    parent_node.right = None
                else:
                    parent_node.left = None
                return ("Node removed")
    
bst = BST()
bst.insert(37)
bst.insert(23)
bst.insert(50)
bst.insert(16)
bst.insert(30)
bst.insert(40)
bst.insert(70)
bst.insert(10)
bst.insert(20)
bst.insert(38)
bst.insert(47)
bst.insert(69)
bst.insert(100)
print(bst.remove_node(23))