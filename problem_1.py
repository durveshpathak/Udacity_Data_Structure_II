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
            self.tail.next = None
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

            if node_obj.value is self.lru_list.head.value:
                return self.lru_list.head.value

            if node_obj.value is self.lru_list.tail.value:
                self.lru_list.prepend(node_obj.value)
                self.lru_list.poptail()
                return node_obj.value

            else:
                if node_obj.prev is not None:
                    node_obj.prev.next = node_obj.next

                if node_obj.next is not None:
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

            else:

                lru_key = self._lru_obj_find()
                #print(lru_key.value)
                del self.cache_map[lru_key.value]
                self.cache_map[key] = self.lru_list.prepend(value)

        return


# Test Case 1
our_cache = LRU_Cache(5) # Cache Size define to 5
our_cache.set(3, 3)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(4, 4)
our_cache.set(5, 5)
print(our_cache.get(1))
# 1
print(our_cache.get(2))
# 2
print(our_cache.get(4))
# 4
print(our_cache.get(77))
# -1
our_cache.set(6, 6)
our_cache.set(7, 7)
print(our_cache.get(5))
# -1

# Test Case 2

our_cache = LRU_Cache(3)
print(our_cache.get(1))
# -1
our_cache.set(1,1)
our_cache.set(2,2)
print(our_cache.get(1))
# 1
our_cache.set(7,7)
print(our_cache.get(2))
# 2
our_cache.set(8,8)
print(our_cache.get(1))
# -1


# Edge Case
our_cache = LRU_Cache(2)
our_cache.set(1,1)
our_cache.set(2,2)
print(our_cache.get(1))
# 1
print(our_cache.get(2))
# 2
print(our_cache.get(1))
# 1
print(our_cache.get(1))
# 1
print(our_cache.get(2))
# 2
our_cache.set(4,4)
print(our_cache.get(1))
# -1
