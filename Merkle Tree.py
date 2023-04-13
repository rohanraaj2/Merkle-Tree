import hashlib

class Node:
    def __init__(self, left, right, hashval, value):
        self.left = left
        self.right = right
        self.hashval = hashval                          # repesents hash value of node
        self.value = value                              # represents content of node

class MerkleTree:
    def __init__(self, hashes: list):
        self.buildTree(hashes)

    def hash(self, val : str) -> str:
        return hashlib.sha256(val.encode('utf-8')).hexdigest()    # returns hash value of provided node    

    def buildTree(self, hashes: list) -> None:
        # builds a tree from the dataset 

        nodes = []                                          # creates the initial list of nodes that will be stored in the merkle tree
        for val in hashes:
            print(val)
            print("node hash", self.hash(val))
            node = Node(None,None,self.hash(val),val)
            nodes.append(node)  
        print("nodes: ", nodes) 

        if len(nodes) % 2 != 0:                             # if no of nodes are odd, duplicate the last node to make it even
            nodes.append(nodes[-1])
            print("dup")

        self.root = self._buildTree(nodes)                  # resulting tree is stored in the root of the MerkleTree object
        print("root: ", self.root.value)
        self.print_tree(self.root)

    def insert(self, value, hashes : list):
        # adds values to the list

        node = Node(value)                                  # create a new node 
        hashes.append(node.value)                           # add the new node to the hash list
        self.buildTree(hashes)                              # re-build the tree after insertion

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

    def get_proof(self,value):
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
        
        if len(nodes) % 2 != 0:                             # if no. of nodes are odd, duplicate the last node to make it even
            nodes.append(nodes[-1])
            print("duplicating")

        half: int = len(nodes) // 2                         # to be used to split the tree for obtaining left right branches
 
        # if only 2 elements exist, the new node is the hash of the hashes of the two
        if len(nodes) == 2:                                 
            node = Node(nodes[0], nodes[1], self.hash(nodes[0].hashval + nodes[1].hashval), nodes[0].value+" "+nodes[1].value)
            return node
 
        # Recursively build the left and right subtrees
        left = self._buildTree(nodes[:half])
        right = self._buildTree(nodes[half:])

        # Calculate the hash and value of the current node based on the hashes and values of its children
        hashval = self.hash(left.hashval + right.hashval)
        value = f'{left.value}+{right.value}'

        # Create and return a new node with the calculated hash and value
        node = Node(left, right, hashval, value)
        return node

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

hashes = ["hash1", "hash2", "hash3", "hash4"]
merkle_tree = MerkleTree(hashes)