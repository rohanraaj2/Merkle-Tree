import hashlib

class Merkletree:

    def __init__(self, words:list) -> None:
        self.build_tree(words)

    def hash(self, val : str) -> str:
        return hashlib.sha256(val.encode('utf-8')).hexdigest()    # returns hash value of provided node    

    def build_tree(self, words:list[str]):
        hashes = self._get_hashlist(words)
        tree = self.generateMerkleTree(hashes)
        return tree
   
    def generateMerkleTree(self, hashes:list):
        # hashes: list of hash values

        if not hashes or len(hashes) == 0:
            return []
        
        tree = [hashes]
        
        self.generate(hashes, tree)
        print("tree", tree)
        return tree

    def generate(self,hashes, tree):
        if len(hashes) == 1:
            return hashes
            
        self.ensureEven(hashes)
        combinedHashes = []

        for i in range(0, len(hashes), 2):
            hashesConcatenated = hashes[i] + hashes[i + 1]
            hash = self.hash(hashesConcatenated)
            combinedHashes.append(hash)

        tree.append(combinedHashes)
        print(tree)
        return self.generate(combinedHashes, tree)

    def generateMerkleRoot(self,hashes):
        # returns the merkle root 
        if not hashes or len(hashes) == 0:
            return ''
        
        self.ensureEven(hashes)
        combinedHashes = []

        for i in range(0, len(hashes), 2):
            hashPairConcatenated = hashes[i] + hashes[i + 1]
            hash = hashlib.sha256(hashPairConcatenated.encode()).hexdigest()
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

    def generateMerkleProof(self, hash, hashes):
        if not hash or not hashes or len(hashes) == 0:
            return None
        
        tree = self.generateMerkleTree(hashes)
        merkleProof = [{'hash': hash,'direction': self.getLeafNodeDirectionInMerkleTree(hash, tree) }]
        hashIndex = tree[0].index(hash)

        for level in range(len(tree) - 1):
            isLeftChild = hashIndex % 2 == 0
            siblingDirection = 'right' if isLeftChild else 'left'
            siblingIndex = hashIndex + 1 if isLeftChild else hashIndex - 1
            siblingNode = {'hash': tree[level][siblingIndex],'direction': siblingDirection}
            merkleProof.append(siblingNode)
            hashIndex = hashIndex // 2

        return merkleProof
    
    def verify(self, hash, hashes):
        if self.generateMerkleProof(self, hash, hashes) == None:
            return False
        else:
            return True

        
    # helper functions

    def _get_hashlist(self, words:list):
        # returns a list of all the leaf nodes before building of the tree

        hashes = []                                          # creates the initial list of nodes that will be stored in the merkle tree
        for val in words:
            hash = self.hash(val)
            hashes.append(hash) 
        return hashes 
    
    def getLeafNodeDirectionInMerkleTree(self, hash, merkleTree):
        hashIndex = merkleTree[0].index(hash)
        if hashIndex % 2 == 0:
            return 'left'
        else:
            return 'right'

    def ensureEven(self,lst):
        # duplicates if nodes are odd
        if len(lst) % 2 != 0:
            lst.append(lst[-1])

words = ["My", "name","is"]   
tree = Merkletree(words)   
print(tree.generateMerkleProof('8ed6791bdf3d61a1e6edcbb253979b0a6bef7f3d99dda0fb49cffe96923514b6',['8ed6791bdf3d61a1e6edcbb253979b0a6bef7f3d99dda0fb49cffe96923514b6', '82a3537ff0dbce7eec35d69edc3a189ee6f17d82f353a553f9aa96cb0be3ce89', 'fa51fd49abf67705d6a35d18218c115ff5633aec1f9ebfdc9d5d4956416f57f6']))