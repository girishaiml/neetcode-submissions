class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()

            cur = cur.children[char]

        cur.endOfWord = True

    def search(self, word: str) -> bool:

        def dfs(index, node):
            for i in range(index, len(word)):
                char = word[i]

                if char == ".":
                    for child in node.children.values():
                        if dfs(i + 1, child):
                            return True

                    return False

                if char not in node.children:
                    return False

                node = node.children[char]

            return node.endOfWord

        return dfs(0, self.root)
