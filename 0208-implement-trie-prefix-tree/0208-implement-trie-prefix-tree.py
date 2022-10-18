class TrieNode:
    def __init__(self):
        self.child = dict()
        self.isEnd = False
        
class Trie:

    def __init__(self):
        self.dummy = TrieNode()        

    def insert(self, word: str) -> None:
        cur = self.dummy
        for i in range(len(word)):
            char = word[i]
            if char not in cur.child:
                cur.child[char] = TrieNode()
            cur = cur.child[char]
            
            if i == len(word) - 1:
                cur.isEnd = True
        

    def search(self, word: str) -> bool:
        cur = self.dummy
        for i in range(len(word)):
            char = word[i]
            if char not in cur.child: return False
            cur = cur.child[char]
        return cur.isEnd

    def startsWith(self, prefix: str) -> bool:
        cur = self.dummy
        for i in range(len(prefix)):
            char = prefix[i]
            if char not in cur.child: return False
            cur = cur.child[char]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)