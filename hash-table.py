class HashTable:
    def __init__(self,size=7):
        self.data_map = [None]*size ##opening a list of the given size, these are the addresses

    def __hash(self, key): 
        ##'__' as prefix to name means its internal function and cannot be called outside of the class
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
            ## for every letter the address is calculated by adding my_hash to the letter's ASCII value (ord), 
            ## then that number's remainder when divided by size of addresses
        return my_hash
    
    def print_table(self):
        for key, value in enumerate(self.data_map):
            print(f"{key} : {value}")

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None : 
            self.data_map[index] = [] ## initializing an empty list if not present at the address already to store multiple key-value pairs
        self.data_map[index].append([key,value])

    def get(self, key):
        index = self.__hash(key)
        if self.data_map[index] == None:
            print("Key doesnt exist")
            return False
        for i,j in self.data_map[index]:
            if key == i :
                print(f"{key} : {j}")
                return True
        return False

    def keys(self): ##return list of keys in hash table
        key_list = []
        for i in range (len(self.data_map)):
            if self.data_map[i] is not None :   
                for key in self.data_map[i]:
                    key_list.append(key[0])
        return key_list


myhash = HashTable()
myhash.print_table()
myhash.set_item("bolts", 50)
myhash.set_item("washers", 510)
myhash.set_item("nails", 3500)
print("---------")
myhash.print_table()
myhash.get("washers")
print(myhash.keys())
