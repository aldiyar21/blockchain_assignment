import hashlib

class m_node:         #class for every node in merkle tree
    def __init__(self, data):
        self.data = data       # storing the data of transaction
        self.left = None       #left child
        self.right = None      # right child

class MerkleTree:   
    def __init__(self, trans):
        self.trans = trans       #initializing list of trans-s in tree
        self.root = self.createTree(trans)   #save the root of the tree

    def createTree(self, trans):   #function to combine nodes and create tree
        if len(trans) == 0:
            return None
        if len(trans) == 1:
            return m_node(trans[0])

        nodes = [m_node(tx) for tx in trans]  #create node for every transaction

        while len(nodes) > 1:
            new_level = []
            for i in range(0, len(nodes), 2):
                left = nodes[i]
                right = nodes[i + 1] if i + 1 < len(nodes) else left
                comb_data = left.data + right.data   #combine data from both child-nodes
                combined_hash = hashlib.sha256(comb_data.encode()).hexdigest()  #calculate the hash of this data
                parent_node = m_node(combined_hash)  #create a parent node with combined hash
                parent_node.left = left       #set it to the left and right childs
                parent_node.right = right
                new_level.append(parent_node)
            nodes = new_level

        return nodes[0] #return the root node of the merkle tree

    def addTransaction(self, transaction_data):    #func to add new transaction to merkle
        self.trans.append(transaction_data)
        self.root = self.createTree(self.trans) #redoing the tree with updated list

    def getRootHash(self):   #func to retrieve hash of root node
        return self.root.data if self.root else None
        pass        
