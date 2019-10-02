import heapq
import sys



class HeapNode:
    def __init__(self,char,value):
        self.frequency = value
        self.char = char
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.frequency <= other.frequency

def count_occurence(data):
    dict_char_freq = {}
    i = 1

    for char in data:
        if char not in dict_char_freq:
            dict_char_freq[char] = i
        else:
            dict_char_freq[char] = dict_char_freq[char] + 1
    return dict_char_freq


def create_min_heap(key, value):
    node = HeapNode(key, value)
    heapq.heappush(heap, node)
    return node


def merge_low_freq_nodes():

    node1 = heapq.heappop(heap)
    node2 = heapq.heappop(heap)
    new_freq = node1.frequency+node2.frequency
    new_char = 'Arbitary'
    new_node = create_min_heap(new_char,new_freq)
    new_node.left = node1
    new_node.right = node2
    return

def code_key(node, code):
    if node is None:
        return
    if node is not None:
        if node.char != 'Arbitary':
            code_lookup[node.char] = code
    code_key(node.left, code + '1')
    code_key(node.right, code + '0')
    return

def huffman_encoding(data):
    if data == '':
        return -1
    else:
        rev_lookup = {}
        encoded_data = ''
        lookup_char_freq = count_occurence(data)

        for key in lookup_char_freq:
            node = create_min_heap(key, lookup_char_freq[key])
        while len(heap) != 1:
            merge_low_freq_nodes()
        encoded_node = heapq.heappop(heap)
        code_key(encoded_node,'')
        for key in code_lookup:
            rev_lookup[code_lookup[key]] = key

        for char in data:
            encoded_data += code_lookup[char]
        return encoded_data, rev_lookup

def huffman_decoding(data,code_lookup):
    string = ''
    char = ''
    for i in range(len(data)):
        char += data[i]
        if char in code_lookup:
            string+=code_lookup[char]
            char = ''
    return string



# Test Case 1

heap = []
code_lookup = {}

a_great_sentence = "The bird is the word"
print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
#The size of the data is: 69
print ("The content of the data is: {}\n".format(a_great_sentence))
#The content of the data is: The bird is the word

encoded_data, lookup = huffman_encoding(a_great_sentence)
print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
#The size of the encoded data is: 36
print ("The content of the encoded data is: {}\n".format(encoded_data))
#The content of the encoded data is: 0101110001000010101111000110001110100000001101100010000001111011100011

decoded_data = huffman_decoding(encoded_data,lookup)
print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
#The size of the decoded data is: 69
print ("The content of the encoded data is: {}\n".format(decoded_data))
#The content of the encoded data is: The bird is the word


# Test Case 2
heap = []
code_lookup = {}
a_new_sentence = "I like Programming"
print ("The size of the data is: {}\n".format(sys.getsizeof(a_new_sentence)))
#The size of the data is: 67
print ("The content of the data is: {}\n".format(a_new_sentence))
#The content of the data is:  I like Programming

encoded_data, lookup = huffman_encoding(a_new_sentence)
print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
#The size of the encoded data is: 36
print ("The content of the encoded data is: {}\n".format(encoded_data))
#The content of the encoded data is: 101101110000010000100000011111011011110101101010000100010011001010

decoded_data = huffman_decoding(encoded_data,lookup)
print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
#The size of the decoded data is: 67
print ("The content of the encoded data is: {}\n".format(decoded_data))
#The content of the encoded data is: I like Programming


# Test Case 3
heap = []
code_lookup = {}
a_new_sentence = "I am dumb"
print ("The size of the data is: {}\n".format(sys.getsizeof(a_new_sentence)))
#The size of the data is: 67
print ("The content of the data is: {}\n".format(a_new_sentence))
#The content of the data is:  I like Programming

encoded_data, lookup = huffman_encoding(a_new_sentence)
print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
#The size of the encoded data is: 36
print ("The content of the encoded data is: {}\n".format(encoded_data))
#The content of the encoded data is: 101101110000010000100000011111011011110101101010000100010011001010

decoded_data = huffman_decoding(encoded_data,lookup)
print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
#The size of the decoded data is: 67
print ("The content of the encoded data is: {}\n".format(decoded_data))
#The content of the encoded data is: I like Programming