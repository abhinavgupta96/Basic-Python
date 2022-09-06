class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList : 

    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None :
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.length == 0 :
            self.head = new_node
            self.tail = new_node
        else :
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0 :
            return("LL is empty, nothing to pop")
            
        elif self.length == 1 :
            temp = self.head
            self.head = None
            self.tail = None
            self.length -=1
            return(f"LL popped : {temp.value}")
        else : 
            temp = self.head
            pre = self.head
            while temp.next is not None :
                pre = temp
                temp = temp.next
            self.tail = pre
            pre.next = None
            self.length -=1
            return(f"LL popped : {temp.value}")

    def prepend(self, value):
        new_node = Node(value)
        if self.length==0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length+=1
        return True

    def pop_first(self) :
        if self.length == 0 :
            print("Nothing to pop")
            return None
        elif self.length == 1 :
            temp = self.head
            self.head = None
            self.tail = None
            self.length-=1
            print(f"Popped : {temp.value}")
        else :
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.length-=1
            print(f"Popped : {temp.value}")
        return temp

    def get(self, index):
        if self.length ==0 or index > self.length :
            return None
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp

    def set_value(self, index, value) :
        temp = self.get(index) #get the node at the given index
        if temp is not None :
            temp.value = value
            return True
        return False

    def insert(self, index,value):
        if index < 0 or index > self.length:
            return False
        elif index == 0:
            return self.prepend(value)
        elif index == self.length :
            return self.append(value)
        else:
            new_node = Node(value)
            temp = self.get(index-1)
            new_node.next = temp.next
            temp.next = new_node
            self.length+=1
            return True

    def insert_new(self, index, value): ##without using get function adding new value
        temp = self.head
        new_node = Node(value)
        for _ in range(index):
            prev = temp
            temp = temp.next
        prev.next = new_node
        new_node.next = temp
        
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        elif index == 0:
            return self.pop_first()
        elif index == self.length-1 :
            return self.pop()
        else:
            # prev = self.get(index-1) ##Using get func 2 times is inefficient as its twice O(n)
            # after = self.get(index+1)
            # prev.next = after
            prev = self.get(index-1)
            temp = prev.next ##removing extra get func call in previous way
            prev.next = temp.next
            temp.next = None
            self.length-=1
            return temp
        
    def remove_by_value(self,value):
        ##this method will search the entire LL and remove the value given to it as a parameter
        temp = self.head
        prev = None
        after = None
        while temp is not None:
            if temp.value == value:
                after = temp.next
                if prev is None: ##edge case where head is the value given as parameter
                    self.head = after
                    temp.next = None
                else:
                    prev.next = after
                    temp.next = None
                self.length-=1
                return True
            prev = temp
            temp = temp.next
    
    def reverse_ll(self):
        ##reversing self.head and self.tail
        temp = self.head
        self.head = self.tail
        self.tail = temp
        ##using 2 variables to keep track of before and after nodes of temp
        before = None
        after = temp.next
        for _ in range(self.length): ##running the steps till ll's length
            after = temp.next ##defining after node
            temp.next = before ##reversing pointer from temp to before instead of after
            before = temp #moving before to where temp is currently
            temp = after #moving temp to where after was so that it repeats from line 147



new_ll = LinkedList(14)
new_ll.append(8)
new_ll.append(18)
new_ll.append(81)
new_ll.append(27)
new_ll.prepend(28)
print("-------")
new_ll.print_list()
new_ll.insert(4,3)
print("-------")
new_ll.print_list()
new_ll.remove(3)
print("-------")
new_ll.print_list()
new_ll.reverse_ll()
print("-------")
new_ll.print_list()

