class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity
    self.oldest_index = 0
    
  def iterate_oldest_index(self):
    if self.oldest_index == self.capacity - 1:
      self.oldest_index = 0
    else:
      self.oldest_index += 1
      
  def append(self, item):
    # if there are Nones in our storage we have not yet reached capacity
    if None in self.storage:
      for i in range(len(self.storage)):
        if not self.storage[i]:
          # when we find a None item overwrite it to the item we are appending, but then stop! Don't overwrite all the Nones
          self.storage[i] = item
          break
    else:
       self.storage[self.oldest_index] = item
       self.iterate_oldest_index() 

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