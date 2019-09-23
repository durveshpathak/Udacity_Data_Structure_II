class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def prepend(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

        return self.head

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            new_node = Node(data)
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def search(self, data):
        if self.head is None:
            return None
        else:
            current_node = self.head
            while current_node:
                if current_node.value == data:
                    return current_node
                else:
                    current_node = current_node.next
            return None

    def remove(self, data):
        if self.head is None:
            return
        elif self.head.value == data:
            self.head = self.head.next
            return
        else:
            current_node = self.head
            #print(current_node.next.value)
            while current_node:
                if current_node.next.value == data:
                    current_node.next = current_node.next.next
                    return
                current_node = current_node.next

    def pop(self):
        if self.head is None:
            return
        else:
            node = self.head.value
            self.head = self.head.next
            return node

    def poptail(self):
        if self.head is None:
            return
        else:
            node = self.tail
            self.tail = self.tail.prev
        return node

    def insert(self, data, position):
        if position == 0:
            self.prepend(data)
            return

        if position > self.size():
            position = self.size()

        else:
            position == position

        new_node = Node(data)
        current_node = self.head
        for i in range(position-1):
            current_node = current_node.next
        new_node.next = current_node.next
        current_node.next = new_node

    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.value)
            current_node = current_node.next

    def to_list(self):
        createList = []
        current_node = self.head
        while current_node is not None:
            createList.append(current_node.value)
            current_node = current_node.next
        return createList

    def size(self):
        if self.head is None:
            return None
        else:
            size = 0
            current_node =self.head
            while current_node:
                size += 1
                current_node = current_node.next
        return size

class LRU_Cache(object):
    def __init__(self, capacity):
        self.cache_size = capacity
        self.cache_map = {}
        self.lru_list = LinkedList()
        # Initialize class variables
        pass

    def _lru_obj_find(self):

        node = self.lru_list.poptail()

        return node

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.

        if key in self.cache_map:
            node_obj = self.cache_map[key]
            #print(str(node_obj) + 'chk')
            #print(node_obj.prev.value)
            #self.lru_list.prepend(node_obj)

            if node_obj is self.lru_list.head:
                return
            if node_obj is self.lru_list.tail:
                self.lru_list.prepend(node_obj.value)
                self.lru_list.poptail()

            else:
                node_obj.prev.next = node_obj.next
                node_obj.next.prev  = node_obj.prev
                self.lru_list.prepend(node_obj.value)

            return node_obj.value
        else:
            return -1
        pass

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.

        if key in self.cache_map:
            return
        else:
            if self.cache_size != 0:
                self.cache_map[key] = self.lru_list.prepend(value)
                self.cache_size -= 1
                #print(self.cache_map[key].value)

            else:

                lru_key = self._lru_obj_find()
                #print(lru_key.value)
                del self.cache_map[lru_key.value]
                self.cache_map[key] = self.lru_list.prepend(value)

        pass




our_cache = LRU_Cache(5)
#print(our_cache.size)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
#print (our_cache.lru_list.head.value)
our_cache.set(4, 4)
print(our_cache.get(3))
print(our_cache.get(2))
our_cache.set(5, 5)
#print(our_cache.lru_list.tail.value.value)
our_cache.set(6, 6)
our_cache.set(7, 7)
our_cache.set(8,8)
our_cache.set(9,9)
print(our_cache.get(2))
print(our_cache.get(5))
our_cache.set(10,10)

#our_cache.lru_list.print_list()#
#print(our_cache.cache_size)

 # returns 1
#print(our_cache.get(2) )     # returns 2
#print(our_cache.get(9)   )   # returns -1 because 9 is not present in the cache

#our_cache.set(5, 5)
#our_cache.set(6, 6)

#print(our_cache.get(3))     # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
#print(our_cache.size)
print(our_cache.cache_map)
#our_cache.lru_list.print_list()