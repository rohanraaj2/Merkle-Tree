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
        # print(node.value)
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
            self.print_tree()
        pass

    def delete(self,value):
        # deletes a node from the tree
        print("Tree before deletion:")
        self.print_tree()
        
        if not self.root:
            return None

        # find the node to delete
        node = self._find_node(self.root, value)

        if not node:
            return self.root

        # delete the node
        self._delete_node(node)

        print(f"Node with value {value} was successfully deleted")
        print("Tree after deletion:")
        self.print_tree()

        return self.root
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
            # print("node hash: ",node.hash)
            node = node.parent
        pass

    def get_proof(self,value):
        # proves that the value exists in the tree
        # returns the proof for the given value
        pass

    def print_tree(self, node= None, indent=0):
        # prints the contents of the tree 
        if node is None:
            node = self.root

        print(" " * indent, end="")
        #print(f"{node.value} ({node.hash})")
        print(f"{node.value}")

        if node.left:
            self.print_tree(node.left, indent+2)
        if node.right:
            self.print_tree(node.right, indent+2)
        pass

    # helper functions

    def _find_node(self, node, value):
        if not node:
            return None

        if node.value == value:
            return node

        left_node = self._find_node(node.left, value)
        if left_node:
            return left_node

        return self._find_node(node.right, value)
    
    def find(self, value):
        # start at the root node
        current_node = self.root
        
        # traverse the tree until the value is found or the end is reached
        while current_node is not None:
            if current_node.value == value:
                return current_node
            elif value < current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right
        
        # value was not found in the tree
        return None

    def _delete_node(self, node):
        if not node.left and not node.right:
            # node has no children
            if node == self.root:
                self.root = None
            else:
                parent = self._find_parent(self.root, node)
                if parent.left == node:
                    parent.left = None
                else:
                    parent.right = None

        elif node.left and node.right:
            # node has two children
            successor = self._find_min_node(node.right)
            node.value = successor.value
            node.hash = successor.hash
            self._delete_node(successor)

        else:
            # node has one child
            if node.left:
                child = node.left
            else:
                child = node.right

            if node == self.root:
                self.root = child
            else:
                parent = self._find_parent(self.root, node)
                if parent.left == node:
                    parent.left = child
                else:
                    parent.right = child

        return

    def _find_min_node(self, node):
        while node.left:
            node = node.left

        return node

    def _find_parent(self, node, child):
        if not node:
            return None

        if node.left == child or node.right == child:
            return node

        left_parent = self._find_parent(node.left, child)
        if left_parent:
            return left_parent

        return self._find_parent(node.right, child)

tree = MerkleTree()

# Insert some values into the tree
tree.insert("apple")
tree.insert("banana")
tree.insert("cherry")
tree.insert("date")
tree.insert("elderberry")    

# delete some values from tree
tree.delete("banana")
tree.delete("date")
tree.insert("date")