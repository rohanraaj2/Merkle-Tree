import hashlib

class Node:
    def __init__(self, value):
        self.value = value
        self.hash = hashlib.sha256(value.encode()).hexdigest()
        self.left = None
        self.right = None

class MerkleTree:
    def __init__(self):
        self.root = None

    def insert(self,value):
        # adds a new node to the tree
        pass

    def delete(self,value):
        # deletes a node from the tree
        # returns the updated tree
        pass

    def verify(self, proof, value, root_hash):
        # verifies the merkle proof for the given value
        # returns True if correct, False if incorrect
        pass

    def rehash(self):
        # updates the hash values of each node 
        pass

    def get_proof(self,value):
        # proves that the value exists in the tree
        # returns the proof for the given value
        pass

    def print_tree(self):
        # prints the contents of the tree 
        pass