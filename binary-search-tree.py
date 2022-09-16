class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self,value):
        node = Node(value)
        if self.root is None:
            self.root = node
            return True
        temp = self.root
        while True:
            if temp.value > node.value:
                if temp.left:
                    temp = temp.left
                else:
                    temp.left = node
                    return True
            elif temp.value < node.value:
                if temp.right :
                    temp = temp.right
                else:
                    temp.right = node
                    return True
            else:
                return None
    
    def inorder_successor(self): ##Function that returns list of nodes in their in-order traversal (iteratively)
        temp = self.root
        inorder_st = []
        inoder_list = []
        while True:
            if temp is not None:
                inorder_st.append(temp)
                temp = temp.left
            elif inorder_st:
                temp = inorder_st.pop()
                inoder_list.append(temp.value)
                temp = temp.right
            else:
                break
        return inoder_list


    def find_node(self,value): ##function returns a node if it exists in the tree when value is passed to it
        temp = self.root
        while temp is not None:
            if temp.value > value:
                temp = temp.left ##move left regardless of value, if temp is none while condition will take care of it
            elif temp.value < value:
                temp = temp.right
            elif temp.value == value:
                return temp
        return None

            
    
    def get_parent_node(self,node): ##this function gets the parent node of any given node
        node = node
        parent_node = None
        temp = self.root
        if node is self.root:
            return parent_node
        while node is not None:
            if temp.value < node.value:
                if temp.right:
                    parent_node = temp
                    temp = temp.right
            elif temp.value > node.value:
                if temp.left:
                    parent_node = temp
                    temp = temp.left
            elif temp.value == node.value:
                return parent_node
        return None

    def delete_node(self, value): #Function handles deletion of node, can be optimised
        node = self.find_node(value)
        parent_node = self.get_parent_node(node)
        successor_list = self.inorder_successor()
        deleted_node_index = successor_list.index(value)
        successor_node = successor_list[deleted_node_index+1]
        successor_node = self.find_node(successor_node)
        if node.left or node.right: ##If node has one child
            if node.left:
                parent_node.left = successor_node
                node.left = None
            else:
                parent_node.right = successor_node
                node.right = None
        elif node.left and node.right: ##If node has 2 children
            if successor_node.value < parent_node.value:
                parent_node.left = successor_node
            else:
                parent_node.right = successor_node
            node.right = None
        else: ##If node is a leaf node
            if parent_node.left is node:
                parent_node.left = None
            else:
                parent_node.right = None
        return node


bst = BST()
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(25)
bst.insert(45)
bst.insert(60)
bst.insert(80)
bst.insert(5)
bst.insert(27)
bst.insert(35)
bst.insert(100)
print(bst.delete_node(30).value)
print(bst.root.left.value)
print(bst.root.left.right.left.value)
