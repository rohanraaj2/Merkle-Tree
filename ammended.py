import hashlib

class Merkletree:

    def __init__(self, words:list) -> None:
        self.tree = self.build_tree(words)

    def hash(self, val : str) -> str:
        return hashlib.sha256(val.encode('utf-8')).hexdigest()    # returns hash value of provided node    

    def build_tree(self, words:list[str]):
        hashes = self._get_hashlist(words)
        tree = self.generateMerkleTree(hashes)
        return tree
   
    def generateMerkleTree(self, hashes:list):
        
        if not hashes or len(hashes) == 0:          # returns an empty list if there are no hashes provided
            return []
        
        tree = [hashes]                             # creates a tree and adds the list of hashes as the first index
        
        self._generate(hashes, tree)                 # calls this function so that it can create the remainign levels of hashes
        # print("tree", tree)
        return tree

    def generateMerkleRoot(self,hashes):
        # returns the merkle root 
        # works in a similar way to generate
        if not hashes or len(hashes) == 0:
            return ''
        
        self._ensureEven(hashes)
        combinedHashes = []

        for i in range(0, len(hashes), 2):
            hashPairConcatenated = hashes[i] + hashes[i + 1]
            hash = self.hash(hashPairConcatenated)
            combinedHashes.append(hash)

        if len(combinedHashes) == 1:
            return combinedHashes[0]
        
        return self.generateMerkleRoot(combinedHashes)

    def insert(self,value):
        # inserts a new hash to the merkle tree
        hash = self.hash(value)
        if len(self.tree) == 0:
            self.tree = [[hash]]
        else:
            self.tree[0].append(hash)
            self.generateMerkleTree(self.tree[0])

    def generate_proof(self, hash, hashes):
        # returns the proof for the inclusivity of a hash
        if hash not in hashes:                                                  # inclusivity failed 
            return []
     
        merkleProof = [{'hash': hash,'direction': self._get_direction(hash, self.tree) }]
        hashIndex = self.tree[0].index(hash)

        for level in range(len(self.tree) - 1):                                  # traversing through the levels
            isLeftChild = hashIndex % 2 == 0
            siblingDirection = 'right' if isLeftChild else 'left'
            siblingIndex = hashIndex + 1 if isLeftChild else hashIndex - 1
            siblingNode = {'hash': self.tree[level][siblingIndex],'direction': siblingDirection}
            merkleProof.append(siblingNode)
            hashIndex = hashIndex // 2

        return merkleProof
    
    def generate_proof_using_value(self, value, hashes):
        # returns the proof for the inclusivity of a value
        hash = self.hash(value)
        if hash not in hashes:                                                  # inclusivity failed 
            return []
     
        merkleProof = [{'hash': hash,'direction': self._get_direction(hash, self.tree) }]
        hashIndex = self.tree[0].index(hash)

        for level in range(len(self.tree) - 1):                                  # traversing through the levels
            isLeftChild = hashIndex % 2 == 0
            siblingDirection = 'right' if isLeftChild else 'left'
            siblingIndex = hashIndex + 1 if isLeftChild else hashIndex - 1
            siblingNode = {'hash': self.tree[level][siblingIndex],'direction': siblingDirection}
            merkleProof.append(siblingNode)
            hashIndex = hashIndex // 2

        return merkleProof
    
    def verify(self, hash, hashes):
        if self.generate_proof(hash, hashes) == []:
            return False
        else:
            return True

    # helper functions

    def _generate(self,hashes, tree):
        if len(hashes) == 1:                            # if only one hash then return that only
            return hashes
            
        self._ensureEven(hashes)                         # check if need for duplication
        combinedHashes = []

        for i in range(0, len(hashes), 2):                          # use every alternate node and concatenate it to create the parent hash
            hashesConcatenated = hashes[i] + hashes[i + 1]
            hash = self.hash(hashesConcatenated)
            combinedHashes.append(hash)                             

        tree.append(combinedHashes)                                 # append the levels of hashes to the tree
        # print(tree)
        return self._generate(combinedHashes, tree)

    def _get_hashlist(self, words:list):
        # returns a list of all the leaf nodes before building of the tree

        hashes = []                                          # creates the initial list of nodes that will be stored in the merkle tree
        for val in words:
            hash = self.hash(val)
            hashes.append(hash) 
        return hashes 
    
    def _get_direction(self, hash, merkleTree):
        hashIndex = merkleTree[0].index(hash)
        if hashIndex % 2 == 0:
            return 'left'
        else:
            return 'right'

    def _ensureEven(self,lst):
        # duplicates if nodes are odd
        if len(lst) % 2 != 0:
            lst.append(lst[-1])

# testing
words = ["My", "name","is"]   
tree = Merkletree(words)
hashlist = ['8ed6791bdf3d61a1e6edcbb253979b0a6bef7f3d99dda0fb49cffe96923514b6', '82a3537ff0dbce7eec35d69edc3a189ee6f17d82f353a553f9aa96cb0be3ce89', 'fa51fd49abf67705d6a35d18218c115ff5633aec1f9ebfdc9d5d4956416f57f6']

# does not exist in tree 
print(tree.generate_proof('8ed6791bdf3d61a1e6edcbb253979b0a6bef7f3d99dda0fb49cffe96923514b6',hashlist))
print(tree.verify('8ed6791bdf3d61a1e6edcbb253979b0a6bef7f3d99dda0fb49cffe96923514b6',hashlist))

# exists in tree
print(tree.generate_proof_using_value("My",hashlist))
print(tree.generate_proof('8ed6791bdf3d61a1e6edcab253979b0a6bef7f3d99dda0fb49cffe96923514b6',hashlist))
print(tree.verify('8ed6791bdf3d61a1e6edcab253979b0a6bef7f3d99dda0fb49cffe96923514b6',hashlist))