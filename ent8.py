# CTCI 16.20

class Node:
    def __init__(self):
        self.children = {}              
        self.EOF = False        

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        node = self.root

        for char in word:
            if char in node.children:          
                node = node.children[char]
            else:
                new_node = Node()
                node.children[char] = new_node     
                node = new_node                       

        node.EOF = True

    def search(self, word):
        node = self.root

        for i in range(len(word)):
            if word[i] in node.children:
                node = node.children[word[i]]
            else:
                return False

        if node.EOF:
            return True

        return False

    def starts_with(self, word):
        node = self.root

        for i in range(len(word)):
            if word[i] not in node.children:
                return False

            node = node.children[word[i]]

        return True

# def get_valid_t9_words(number: str, words: List[str]) -> List[str]:
def get_valid_t9_words(number, words):

    T9_CHARS = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    }

    T = Trie()

    ans = []

    for word in words:
      T.insert(word)

    number_list = list(number)

    def backtrack(lvl=0, word=""):
        if lvl == len(number):
            if T.search(word):
                ans.append(word)

            return

        if not T.starts_with(word):
            return

        for char in T9_CHARS[number_list[lvl]]:
            backtrack(lvl+1, word+char)

    backtrack()

    return ans

print(get_valid_t9_words("233",["add","brg"]))