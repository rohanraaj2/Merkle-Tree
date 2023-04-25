import hashlib

# Understanding: data is coming in the form of a list which will be used to create the merkle tree.

class Node:
    def __init__(self, left, right, hashval, value):
        self.left = left
        self.right = right
        self.hashval = hashval                          # repesents hash value of node
        self.value = value                              # represents content of node

class MerkleTree:
    def __init__(self, words: list):
        self.buildTree(words)

    def hash(self, val : str) -> str:
        return hashlib.sha256(val.encode('utf-8')).hexdigest()    # returns hash value of provided node    

    def buildTree(self, words: list) -> None:
        # builds a tree from the dataset 

        nodes = []                                          # creates the initial list of nodes that will be stored in the merkle tree
        for val in words:
            print(val)
            print("node hash", self.hash(val))
            node = Node(None,None,self.hash(val),val)
            nodes.append(node)  
        print("nodes: ", nodes) 

        if len(nodes) % 2 != 0:                             # if no of nodes are odd, duplicate the last node to make it even
            nodes.append(nodes[-1])
            print("dup", nodes)

        self.root = self._buildTree(nodes)                  # resulting tree is stored in the root of the MerkleTree object
        # print("root: ", self.root.value)
        print("root: ", self.root.hashval)
        self.print_tree(self.root)

    def insert(self, value, nodes: list[Node]):
        # inserts a new word to the list

        node = Node(None,None,self.hash(value),value)

        if nodes[-1] == nodes[-2]:                          # if there is a duplication
            nodes[-1] = node                                # overwrite the duplicate with the new node
        else:
            nodes.append(node)                              # else append to list

        # calls update tree function so that it can: add node to nodes list
        # update tree here
        print("root",self.root.value)
        self._update_tree(self.root,nodes)

        pass

    def verify(self, proof, value, root_hash):
        # verifies the merkle proof for the given value
        # returns True if correct, False if incorrect
        pass

    def get_proof(self, value, words : list):
        # proves that the value exists in the tree
        # returns the proof for the given value
        pass

    def print_tree(self, node: Node) -> None: 
        # prints the values of the tree
        if node != None:
            print(node.value)
            self.print_tree(node.left)
            self.print_tree(node.right)

    # helper functions
    def _buildTree(self, nodes: list[Node]) -> Node:
        # print("nodes list", nodes)
        if len(nodes) % 2 != 0:                             # if no. of nodes are odd, duplicate the last node to make it even
            nodes.append(nodes[-1])
            print("duplicating")

        half: int = len(nodes) // 2                         # to be used to split the tree for obtaining left right branches
 
        # if only 2 elements exist, the new node is the hash of the hashes of the two
        if len(nodes) == 2:                                 
            tree = Node(nodes[0], nodes[1], self.hash(nodes[0].hashval + nodes[1].hashval), nodes[0].value+"+"+nodes[1].value)
            return tree
 
        # Recursively build the left and right subtrees
        left = self._buildTree(nodes[:half])
        right = self._buildTree(nodes[half:])

        # Calculate the hash and value of the current node based on the hashes and values of its children
        hashval = self.hash(left.hashval + right.hashval)
        value = f'{left.value}+{right.value}'

        # Create and return a new node with the calculated hash and value
        tree = Node(left, right, hashval, value)
        # print("tree", tree.value, tree.left,tree.right)
        return tree

    def _update_tree(self, node : Node, nodes : list[Node]) -> Node:
        # updates the right most branch of the tree after insertion of a node
        print("reached") 
        if node.right == None:
            # if node in nodes:
                # If the current node is one of the nodes that needs to be updated, calculate the new hash and value
            print("here")
            left = node.left
            right = node.right
            hashval = self.hash(left.hashval + right.hashval)       # Calculate the new hash based on the hashes of the children
            value = f'{left.value}+{right.value}'                   # Calculate the new value based on the values of the children
            node.hashval = hashval                                  # Update the hash of the current node
            node.value = value                                      # Update the value of the current node
            return node
        else:
            # Traverse to the right child of the current node recursively
            node.right = self._update_tree(node.right, nodes)
            return node
        pass

# Testing
# words = ["hash1", "hash2"]
# merkle_tree = MerkleTree(words)

words = ["hash1", "hash2", "hash3"]
merkle_tree = MerkleTree(words)
merkle_tree.insert("hash4",["hash1", "hash2", "hash3"])

# hashes = ["My", "name", "is", "Ayila"]
# merkle_tree = MerkleTree(hashes)

# hashes = ["My", "name", "is", "Ayla"]
# merkle_tree = MerkleTree(hashes)