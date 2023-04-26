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

    def _get_hashlist(self, words:list):
        # returns a list of all the leaf nodes before building of the tree

        hashes = []                                          # creates the initial list of nodes that will be stored in the merkle tree
        for val in words:
            hash = self.hash(val)
            hashes.append(hash) 
        return hashes        

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

    def ensureEven(self,lst):
        # duplicates if nodes are odd
        if len(lst) % 2 != 0:
            lst.append(lst[-1])

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

    def get_proof(self,hash,hashes):
        # checks for inclusion of leaf in tree

        tree = self.generateMerkleTree(hashes)   
        if hash not in tree[0] or len(hashes) == 0:
            return None
        

        pass

    # def generateMerkleProof(self, hash, hashes):
    #     if not hash or not hashes or len(hashes) == 0:
    #         return None
        
    #     tree = self.generateMerkleTree(hashes)
    #     merkleProof = [{'hash': hash,'direction': self.getLeafNodeDirectionInMerkleTree(hash, tree) }]
    #     hashIndex = tree[0].index(hash)

    #     for level in range(len(tree) - 1):
    #         isLeftChild = hashIndex % 2 == 0
    #         siblingDirection = 'right' if isLeftChild else 'left'
    #         siblingIndex = hashIndex + 1 if isLeftChild else hashIndex - 1
    #         siblingNode = {'hash': tree[level][siblingIndex],'direction': siblingDirection}
    #         merkleProof.append(siblingNode)
    #         hashIndex = hashIndex // 2

    #     return merkleProof
    
    # def getMerkleRootFromMerkleProof(self, merkleProof):
    #     if not merkleProof or len(merkleProof) == 0:
    #         return ''
        
    #     merkleRootFromProof = merkleProof[0]

    #     for hashProof in merkleProof[1:]:
    #         if hashProof['direction'] == 'right':
    #             hash = hashlib.sha256((merkleRootFromProof['hash'] + hashProof['hash']).encode()).hexdigest()
    #             merkleRootFromProof = {'hash': hash}
    #         else:
    #             hash = hashlib.sha256((hashProof['hash'] + merkleRootFromProof['hash']).encode()).hexdigest()
    #             merkleRootFromProof = {'hash': hash}

    #     return merkleRootFromProof['hash']
    
    def getLeafNodeDirectionInMerkleTree(self, hash, merkleTree):
        hashIndex = merkleTree[0].index(hash)
        if hashIndex % 2 == 0:
            return 'left'
        else:
            return 'right'
        

words = ["My", "name","is"]   
tree = Merkletree(words)     