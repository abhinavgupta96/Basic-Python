class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class DLL:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length=1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length+=1
        return True
    
    def pop(self):
        temp = self.tail.prev
        if self.length == 0 :
            return None
        elif self.length ==1:
            self.head = None
            self.tail = None
            self.length-=1
        else :
            temp.next = None
            self.tail.prev = None
            self.tail = temp
            self.length-=1
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else : 
            new_node.next=self.head
            self.head.prev = new_node
            self.head = new_node
        self.length+=1
        return True

    def pop_first(self):
        if self.length == 0 :
            return None
        temp = self.head.next
        if self.length == 1:
            self.head = None
            self.head = None
            self.length-=1
        else:
            temp.prev = None
            self.head.next = None
            self.head = temp
            self.length-=1
        return temp   

    def get (self, index):
        ##code for getting a node in doubly linked list can be the same as the one for linked-list,
        ##however we can optimise it in case of doubly linked list as in it we can traverse the list backwards,
        ##so we divide the operation in 2 halfs, if target is closer from head we approach from there, otherwise we seek from tail
        if index < 0 or index >= self.length :
            return None
        else:
            temp = self.head
            if index < self.length /2 :
                for _ in range(index):
                    temp = temp.next
            else:
                temp = self.tail
                for _ in range(self.length-1, index, -1):
                    temp = temp.prev
            return temp

    def set_value(self, index, value):
        node = self.get(index)
        if node is not None:
            node.value = value
            return True
        return False

    def insert(self, index, value):
        new_node = Node(value)
        if index<0 or index>=self.length:
            return False
        elif index==0:
            return (self.prepend(value))
        elif index ==self.length:
            return (self.append(value))
        prev = self.get(index-1)
        temp = prev.next
        prev.next = new_node
        new_node.prev = prev
        new_node.next = temp
        temp.prev = new_node
        self.length+=1
        return True

    def remove(self, index):
        if index<0 or index>=self.length:
            return False
        elif index==0:
            return (self.pop_first())
        elif index ==self.length:
            return (self.pop())
        prev = self.get(index-1)
        temp = self.get(index+1)
        prev.next = temp
        temp.prev = prev
        self.length-=1
        return True

my_dll = DLL(1)
my_dll.append(23)
my_dll.append(81)
my_dll.append(42)
my_dll.append(67)
my_dll.append(9)
my_dll.print_list()
print("----------")
my_dll.pop()
my_dll.print_list()
my_dll.set_value(3,21)
print("----------")
my_dll.print_list()
my_dll.insert(2,100)
my_dll.insert(4,66)
print("----------")
my_dll.print_list()
my_dll.remove(4)
print("----------")
my_dll.print_list()