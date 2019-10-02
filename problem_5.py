import hashlib


class Block:

    def __init__(self, timestamp, data, previous_hash = None):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash(data + timestamp)

    def calc_hash(self,data):
        sha = hashlib.sha256()
        hash_str = data.encode('utf-8')
        sha.update(hash_str)

        return sha.hexdigest()

    def __repr__(self):

        return 'Block is: \n Data: {} \n Timestamp: {} \n Hash: {}'.format(self.data, self.timestamp, self.hash)

class LinkedList:
      def __init__(self):
          self.head = None
          self.tail = None

      def prepend(self,node):
          if self.head is None:
              self.head = node
              self.tail = self.head
          else:
              self.head.previous_hash = node
              self.head = node

      def search(self,data):

          if self.tail is None:
              return None
          else:
              node = self.tail
              #print(node.previous_hash)
              while node is not None:
                  if data == node.data:
                      return node
                  node = node.previous_hash
          return None

      def size(self):
          size = 0
          node = self.tail
          while node is not None:
              size += 1
              node = node.previous_hash


          return size


#Test Case 1
Block1 = Block('12:00','durvesh')
Block2 = Block('13:00', 'Prachi')
Block3 = Block('1:00', 'Nikhil' )
Block4 = Block('2:00', 'Anurag' )
blockchain = LinkedList()
blockchain.prepend(Block1)
blockchain.prepend(Block2)
blockchain.prepend(Block3)
blockchain.prepend(Block4)
print(blockchain.search('Anurag'))
#Block is:
# Data: Anurag
# Timestamp: 2:00
# Hash: ed884fd26229ce7a5b11310468eb5363a8449ef552020dbb50e4461c2d1d9c43
print (blockchain.size())
# 4

#Test Case 2
Block1 = Block('12:00','durvesh')
Block4 = Block('2:00', 'Anurag' )
Block3 = Block('1:00', 'Nikhil' )
Block5 = Block('2:00', 'ramesh' )
Block6 = Block('2:00', 'bharati' )
Block7 = Block('2:00', 'shyam' )
Block8 = Block('2:00', 'saurabh' )
Block9 = Block('1:00', 'friedman' )
Block10 = Block('1:00', 'dave' )
blockchain = LinkedList()
blockchain.prepend(Block1)
blockchain.prepend(Block2)
blockchain.prepend(Block3)
blockchain.prepend(Block4)
blockchain.prepend(Block5)
blockchain.prepend(Block6)
blockchain.prepend(Block7)
blockchain.prepend(Block8)
blockchain.prepend(Block9)
blockchain.prepend(Block10)
print(blockchain.search('dave'))

#Block is:
# Data: dave
# Timestamp: 1:00
# Hash: 650e7e195a7c49acbacdca380bfc9e96a274d6b1141b1f0d6694b0c08ba4c0c3

print(blockchain.search('shubham'))
#None

print (blockchain.size())
#10