class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.list = []

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

    def to_list(self):

        node = self.head
        while node is not None:
            self.list.append(node.value)
            node = node.next

        return self.list


def union(llist_1, llist_2):
    # Your Solution Here

    list1 = llist_1.to_list()
    list2 = llist_2.to_list()

    list = list1 + list2
    set_union = set(list)
    return set_union

def intersection(llist_1, llist_2):

    # Your Solution Here
    list1 = set(llist_1.to_list())
    list2 = set(llist_2.to_list())
    intersection_list = []
    list_co = list(list1) + list(list2)
    #print(list)
    freq_lookup = {}
    i = 1
    for item in list_co:
        if item not in freq_lookup:
            freq_lookup[item] = i

        else:
            freq_lookup[item] = freq_lookup[item] + 1
            intersection_list.append(item)

    return  intersection_list


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))
#print(linked_list_1.to_list())

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))


# Test case 3

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = [3,3,3,3,3,3,3,3,3]
element_2 = [1,3,4,1,1,1]

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print (union(linked_list_5,linked_list_6))
print (intersection(linked_list_5,linked_list_6))

# Edge Cases

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print (union(linked_list_5,linked_list_6))
print (intersection(linked_list_5,linked_list_6))

# Edge Cases

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = [1,2,3,4]
element_2 = [5,6,7,8]

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print (union(linked_list_5,linked_list_6))
print (intersection(linked_list_5,linked_list_6))