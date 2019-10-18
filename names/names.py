import time
from bst import BinarySearchTree

# O(n) 
# 0.021986961364746094 seconds 
start_time = time.time()
directory = {}
f = open('names_1.txt', 'r')
for line in f:
    line = line.strip()
    directory[line] = line
f.close()

duplicates = []
f = open('names_2.txt', 'r')
for line in f:
    line = line.strip()
    if line in directory:
        duplicates.append(line)
f.close()


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")



# ***************************************
# This approach with the binary search tree still took 0.25 seconds, much longer than just using a dictionary - Complexity of this approach: O(nlogn)
# ***************************************
# start_time = time.time()
# 
# names_1_tree = BinarySearchTree()
# f = open('names_1.txt', 'r')
# for line in f:
#     line = line.strip()
#     names_1_tree.insert(line)
# f.close()
# 
# duplicates = []
# f = open('names_2.txt', 'r')
# for line in f:
#     line = line.strip()
#     if names_1_tree.contains(line):
#         duplicates.append(line)
# f.close()
# 
# end_time = time.time()
# print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
# print (f"runtime: {end_time - start_time} seconds")
# ********************************************************

# ***************************************
# Original Code Took 16 seconds on my machine!! O(n^2) :(
# ***************************************
# start_time = time.time()
# f = open('names_1.txt', 'r')
# names_1 = f.read().split("\n")  # List containing 10000 names
# f.close()
# 
# f = open('names_2.txt', 'r')
# names_2 = f.read().split("\n")  # List containing 10000 names
# f.close()
# 
# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)
# 
# end_time = time.time()
# print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
# print (f"runtime: {end_time - start_time} seconds")
# 
# ********************************************************