class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity
    
  def iterate_current(self):
    if self.current == self.capacity - 1:
      self.current = 0
    else:
      self.current += 1
      
  def append(self, item):
    # if there are Nones in our storage we have not yet reached capacity
    if None in self.storage:
      for i in range(len(self.storage)):
        if not self.storage[i]:
          # when we find a None item overwrite it to the item we are appending, but then stop! Don't overwrite all the Nones
          self.storage[i] = item
          break
    else:
       self.storage[self.current] = item
       self.iterate_current() 

  def get(self):
    if None in self.storage:
      print_storage = []
      for element in self.storage:
        if element:
          print_storage.append(element)
      return print_storage
    return self.storage

buffer = RingBuffer(5)

buffer.append('a')
buffer.append('b')
buffer.append('c')
buffer.append('d')
print(len(buffer.storage), 5)
print(buffer.get(), ['a','b', 'c', 'd'])

buffer.append('e')
print(len(buffer.storage), 5)
print(buffer.get(), ['a', 'b', 'c', 'd', 'e'])

buffer.append('f')
print(len(buffer.storage), 5)
print(buffer.get(), ['f', 'b', 'c', 'd', 'e'])

buffer.append('g')
buffer.append('h')
buffer.append('i')
print(len(buffer.storage), 5)
print(buffer.get(), ['f', 'g', 'h', 'i', 'e'])

# *******************************************************************************
# Ignore this probably, I was trying to do this with a Queue but I think it's probably
# just better off with an array, an array preserves the order better
# *******************************************************************************
# from dll_queue import Queue
# class RingBuffer:
#   def __init__(self, capacity):
#     self.capacity = capacity
#     self.current = 0
#     self.storage = Queue()
#   def __str__(self):
#     current_node = self.storage.storage.head
#     arr = []
#     while current_node:
#       arr.append(current_node.value)
#       current_node = current_node.next
#     return f"{arr}"
      
#   def append(self, item):
#     # print((self.storage.len()))
#     if len(self.storage) >= self.capacity:
#       self.storage.dequeue()
#     self.storage.enqueue(item)

#   def get(self):
#     return self.storage
# 