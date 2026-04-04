class WordDictionary:

    def __init__(self):
        self.root = Node()
        
    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = Node()
            node = node.children[c]
        node.end = True
    
    def search(self, word: str) -> bool:
        print("word", word)
        node = self.root

        def dfs(start, node):
            print("recurse", start)
            curr = node
            for i in range(start, len(word)):
                if word[i] == '.':
                    for n in curr.children.values():
                        if dfs(i+1, n):
                            return True
                    return False
                else:
                    if word[i] in curr.children:
                        curr = curr.children[word[i]]
                    else:
                        return False
            return curr.end
        
        return dfs(0, self.root)




 # VERSION WITH BFS, LESS GOOD CUZ MEMORY EXPLOSION     
 #   def search(self, word: str) -> bool:
 #       print("searching", word)
 #       nodes = [self.root]
 #       for c in word:
 #           if len(nodes) == 0:
 #               print("no match")
 #               return False
 #           elif c == '.':
 #               nodes = [child for n in nodes for child in n.children.values()]
 #               print("wildcard add all", nodes)
 #           else: 
 #               newnodes = []
 #               for n in nodes:
 #                   if c in n.children:
 #                       newnodes.append(n.children[c])
 #               nodes = newnodes
 #               print("new nodes", nodes)
 #       return any(n.end for n in nodes)

class Node:
    def __init__(self):
        self.children = {}
        self.end = False

        
