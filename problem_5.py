import hashlib
from datetime import datetime

class Block:

    def __init__(self, timestamp, data, previous_hash = None):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.more_secure_hash()

    def calc_hash(self,data):
        sha = hashlib.sha256()
        hash_str = data.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

    """ Added as per reviewer suggestion"""
    def more_secure_hash(self):
        encoded_data = hashlib.sha256(self.data.encode('utf-8'))
        encoded_timestamp = hashlib.sha256(self.timestamp.encode('utf-8'))
        encoded_data.hexdigest()
        encoded_timestamp.update(encoded_data.digest())
        if (self.previous_hash is not None):
            encoded_timestamp.update(self.previous_hash.hash.encode("utf-8"))
        return encoded_timestamp.hexdigest()



    def __repr__(self):

        return 'Block is: \n Data: {} \n Timestamp: {} \n Hash: {}'.format(self.data, self.timestamp, self.hash)

class LinkedList:
      def __init__(self):
          self.head = None
          self.tail = None
""" Prepend function accepts BlockXXX_data which is a tuple having timestamp  
and name this tuple will not have the previous_hash attribute"""
      def prepend(self, data):
          if len(data) == 0:
              print('Cant add block with no data')
              return
          node = Block(data[0], data[1])
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

      def print_blockchain(self):
          if self.size() == 0:
              print('Block empty')
              return
          else:
              current_node = self.tail
              while current_node is not None:
                  print(current_node)
                  current_node = current_node.previous_hash
              return


#Test Case 1
Block1_data = (str(datetime.now().timestamp()),'durvesh')
Block2_data = (str(datetime.now().timestamp()), 'Prachi')
Block3_data = (str(datetime.now().timestamp()), 'Nikhil' )
Block4_data = (str(datetime.now().timestamp()), 'Anurag' )
blockchain = LinkedList()
blockchain.prepend(Block1_data)
blockchain.prepend(Block2_data)
blockchain.prepend(Block3_data)
blockchain.prepend(Block4_data)
print(blockchain.search('Anurag'))
#Block is:
# Data: Anurag
# Timestamp: 2:00
# Hash: ed884fd26229ce7a5b11310468eb5363a8449ef552020dbb50e4461c2d1d9c43
print (blockchain.size())
# 4

blockchain.print_blockchain()
"""Block is: 
 Data: durvesh 
 Timestamp: 1570054743.665027 
 Hash: 6b63fa1dda3879ec5867d50ed60b39cd9daa022f8a4160f7a23d38cc34cc8d88
Block is: 
 Data: Prachi 
 Timestamp: 1570054743.665069 
 Hash: cc505e943f41e56d2a2eca5047d4696ebe48717f05d2caaa3b6c2085e4bccefd
Block is: 
 Data: Nikhil 
 Timestamp: 1570054743.665079 
 Hash: f7c2c2af41070457ba2ae3b564f65cf9086047d0febb9451a03a45330910db69
Block is: 
 Data: Anurag 
 Timestamp: 1570054743.665086 
 Hash: af6120b194b0fd59eed566e0ed9943f0f93752020df72fc9205809d73c3bd449"""

#Test Case 2
Block1_data = (str(datetime.now().timestamp()),'durvesh')
Block4_data = (str(datetime.now().timestamp()), 'Anurag' )
Block3_data = (str(datetime.now().timestamp()), 'Nikhil' )
Block5_data = (str(datetime.now().timestamp()), 'ramesh' )
Block6_data = (str(datetime.now().timestamp()), 'bharati' )
Block7_data = (str(datetime.now().timestamp()), 'shyam' )
Block8_data = (str(datetime.now().timestamp()), 'saurabh' )
Block9_data = (str(datetime.now().timestamp()), 'friedman' )
Block10_data =(str(datetime.now().timestamp()), 'dave' )
blockchain = LinkedList()
blockchain.prepend(Block1_data)
blockchain.prepend(Block2_data)
blockchain.prepend(Block3_data)
blockchain.prepend(Block4_data)
blockchain.prepend(Block5_data)
blockchain.prepend(Block6_data)
blockchain.prepend(Block7_data)
blockchain.prepend(Block8_data)
blockchain.prepend(Block9_data)
blockchain.prepend(Block10_data)
print(blockchain.search('dave'))
#Block is:
# Data: dave
# Timestamp: 1:00
# Hash: 650e7e195a7c49acbacdca380bfc9e96a274d6b1141b1f0d6694b0c08ba4c0c3

print(blockchain.search('shubham'))
#None

print(blockchain.tail.previous_hash)

print (blockchain.size())
#10




# Edge cases
Block1_data = ('')
blockchain = LinkedList()

blockchain.prepend(Block1_data)
#Cant add block with no data
blockchain.print_blockchain()
#Block empty