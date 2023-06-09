# import hashlib

# # Understanding: data is coming in the form of a list which will be used to create the merkle tree.

# class Node:
#     def __init__(self, left, right, hashval, value):
#         self.left = left
#         self.right = right
#         self.hashval = hashval                          # repesents hash value of node
#         self.value = value                              # represents content of node

# class MerkleTree:
#     def __init__(self, words: list):
#         self.buildTree(words)

#     def hash(self, val : str) -> str:
#         return hashlib.sha256(val.encode('utf-8')).hexdigest()    # returns hash value of provided node    

#     def buildTree(self, words: list) -> None:
#         # builds a tree from the dataset 

#         nodes = self._get_leaf_nodes(words)  
#         print("nodes: ", nodes) 

#         if len(nodes) % 2 != 0:                             # if no of nodes are odd, duplicate the last node to make it even
#             nodes.append(nodes[-1])
#             print("dup", nodes)

#         self.root = self._buildTree(nodes)                  # resulting tree is stored in the root of the MerkleTree object
#         print("root: ", self.root.value)
#         # print("root: ", self.root.hashval)
#         self.print_tree(self.root)

#     def insert(self, value, nodes: list[Node]):
#         # inserts a new word to the list

#         node = Node(None,None,self.hash(value),value)       # create a new node using value

#         if nodes[-1] == nodes[-2]:                          # if there is a duplication
#             nodes[-1] = node                                # overwrite the duplicate with the new node
#         else:
#             nodes.append(node)                              # else append to list

#         if len(nodes) % 2 != 0:                             # if no of nodes are odd, duplicate the last node to make it even
#             nodes.append(nodes[-1])

#         self.root = self._buildTree(nodes)                  # rebuilding the tree here
#         self.print_tree(self.root)

#         pass

#     def verify(self, root_hash, leaf_index, leaf_hash):
#         proof = self.get_proof(leaf_index, include_leaf=True)
#         calculated_root_hash = leaf_hash
#         for i, sibling_hash in proof:
#             if leaf_index % 2 == 0:
#                 calculated_root_hash = self.hash(calculated_root_hash + sibling_hash)
#             else:
#                 calculated_root_hash = self.hash(sibling_hash + calculated_root_hash)
#             leaf_index //= 2
#         return calculated_root_hash == root_hash

#     def generate_proof(self, hash, nodes: list[Node]):
#         if len(nodes) == 0:
#             return None
        

#         pass

#     def get_proof(self, leaf_index, include_leaf=True):
#         proof = []
#         nodes = [self.root]

#         while len(nodes) > 0 and nodes[0].left is not None:
#             node = nodes[0]
#             if leaf_index % 2 == 0:
#                 sibling = node.right
#                 proof.append((leaf_index+1, sibling.hashval))
#             else:
#                 sibling = node.left
#                 proof.append((leaf_index-1, sibling.hashval))
#             nodes = [sibling] + nodes[1:]
#             leaf_index //= 2

#         if include_leaf:
#             proof.append((leaf_index, self.get_leaf(leaf_index).hashval))

#         return proof[::-1]

#     def get_leaf(self, index):
#         # returns the leaf node at the specified index in the tree
#         nodes = [self.root]
#         while nodes:
#             node = nodes.pop()
#             if node.left is None and node.right is None:
#                 if index == 0:
#                     return node
#                 else:
#                     index -= 1
#             else:
#                 if index % 2 == 0:
#                     nodes.append(node.right)
#                 else:
#                     nodes.append(node.left)
#                 index //= 2
#         raise IndexError('Index out of range')

#     def print_tree(self, node: Node) -> None: 
#         # prints the values of the tree
#         if node != None:
#             print(node.value)
#             self.print_tree(node.left)
#             self.print_tree(node.right)


#     # helper functions
#     def _buildTree(self, nodes: list[Node]) -> Node:
#         # print("nodes list", nodes)
#         if len(nodes) % 2 != 0:                             # if no. of nodes are odd, duplicate the last node to make it even
#             nodes.append(nodes[-1])
#             print("duplicating")

#         half: int = len(nodes) // 2                         # to be used to split the tree for obtaining left right branches
 
#         # if only 2 elements exist, the new node is the hash of the hashes of the two
#         if len(nodes) == 2:        
#             # print("node0",nodes[0], "node1 ",nodes[1])                         
#             node = Node(nodes[0], nodes[1], self.hash(nodes[0].hashval + nodes[1].hashval), nodes[0].value+"+"+nodes[1].value)
#             return node
 
#         # Recursively build the left and right subtrees
#         left = self._buildTree(nodes[:half])
#         right = self._buildTree(nodes[half:])

#         # Calculate the hash and value of the current node based on the hashes and values of its children
#         hashval = self.hash(left.hashval + right.hashval)
#         value = f'{left.value}+{right.value}'

#         # Create and return a new node with the calculated hash and value
#         node = Node(left, right, hashval, value)
#         # print("tree", tree.value, tree.left,tree.right)
#         return node

#     def _get_leaf_nodes(self, words:list) -> list[Node]:
#         # returns a list of all the leaf nodes before building of the tree

#         nodes = []                                          # creates the initial list of nodes that will be stored in the merkle tree
#         for val in words:
#             # print(val)
#             # print("node hash", self.hash(val))
#             node = Node(None,None,self.hash(val),val)
#             nodes.append(node) 
#         return nodes    
    
#     def _get_merkle_root(self):
#         # returns the merkle root
#         return self.root.hashval

# # Testing
# # words = ["hash1", "hash2"]
# # merkle_tree = MerkleTree(words)

# # words = ["hash1", "hash2", "hash3"]
# # merkle_tree = MerkleTree(words)
# # merkle_tree.insert("hash4",merkle_tree._get_leaf_nodes(words))

# # hashes = ["My", "name", "is", "Ayila"]
# # merkle_tree = MerkleTree(hashes)
# # print(merkle_tree._get_merkle_root())
# # print(merkle_tree.get_proof(2,True))

# # hashes = ["My", "name", "is", "Ayla"]
# # merkle_tree = MerkleTree(hashes)
