import time
from merkle_tree import MerkleTree

def main():   #creating 2 instances for case
    blockchain = Blockchain()
    merkle_tree = MerkleTree([])

    while True:         # we provided a console interface for users, and to test the working of blockchain
        print("List of actions:")
        print("1. Add new transaction")     #we can add new transaction
        print("2. Mine block")         #we can mine the new block
        print("3. See the blockchain")     # we can view the blockchain and info about transactions
        print("4. Exit")         
        choice = input("What do you want to do? ")   #here user can write what he wants to choose

        if choice == "1":
            data = input("Write transaction data: ")               #here you can add some message or smth
            merkle_tree.addTransaction(data)  # adding your transaction to merkel tree
            print("Successfully\n")
        
        elif choice == "2":
            if len(merkle_tree.transactions) == 0:         #if there is no transactions we cant create (mine) new block
                print("There is no transactions yet!")
            else:
                new_block = Block(len(blockchain.chain), blockchain.chain[-1].curr_hash, int(time.time()), merkle_tree.root) #creating a new block
                blockchain.addBlock(new_block)
                merkle_tree = MerkleTree([])  # reset the tree after mining ended
                print("Block has been mined")
        
        elif choice == "3":           
            for block in blockchain.chain:         # displaying the data of transactions from blockchain
                print(f"Index: {block.index}")
                print(f"Previous hash: {block.PrevHash}")
                print(f"Timestamp: {block.TimeStamp}")
                print(f"Transactions: {block.trans}")
                print(f"Current hash: {block.curr_hash}")
        
        elif choice == "4":
            break
        else:
            print("You entered the wrong number, please try again\n")      

if __name__ == "__main__":
    main()           #starting the main function
