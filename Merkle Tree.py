import hashlib

class Node:
    def __init__(self, value):
        self.value = value
        self.hash = hashlib.sha256(value.encode('utf-8')).hexdigest()
        self.left = None
        self.right = None
        self.parent = None

class MerkleTree:
    def __init__(self):
        self.root = None

    def insert(self,value):
        # adds a new node to the tree
        node = Node(value)
        print(node.value)
        if not self.root:
            self.root = node
        else:
            current_node = self.root
            while True:
                if value < current_node.value:
                    if current_node.left is None:
                        current_node.left = node
                        node.parent = current_node
                        break
                    else:
                        current_node = current_node.left
                else:
                    if current_node.right is None:
                        current_node.right = node
                        node.parent = current_node
                        break
                    else:
                        current_node = current_node.right
            self.rehash(node)
            print("rehashed")
        pass

    def delete(self,value):
        # deletes a node from the tree
        # returns the updated tree
        pass

    def verify(self, proof, value, root_hash):
        # verifies the merkle proof for the given value
        # returns True if correct, False if incorrect
        pass

    def rehash(self,node):
        # updates the hash values of each node 
        while node:
            if node.left:
                left_hash = node.left.hash
            else: 
                left_hash = ""

            if node.right:
                right_hash = node.right.hash
            else: 
                right_hash = ""
                
            node.hash = hashlib.sha256((left_hash + right_hash).encode('utf-8')).hexdigest()
            print("node hash: ",node.hash)
            node = node.parent
        pass

    def get_proof(self,value):
        # proves that the value exists in the tree
        # returns the proof for the given value
        pass

    def print_tree(self):
        # prints the contents of the tree 
        pass

tree = MerkleTree()

# Insert some values into the tree
tree.insert("apple")
tree.insert("banana")
tree.insert("cherry")
tree.insert("date")
tree.insert("elderberry")    