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
        pass

    def delete(self,value):
        pass

    def search(self,value):
        pass

    def verify(self, proof, value, root_hash):
        pass

    def hash(self):
        pass

    def get_proof(self,value):
        pass