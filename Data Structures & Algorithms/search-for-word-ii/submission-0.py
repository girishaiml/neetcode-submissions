class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        # 1. Build Trie
        for word in words:
            cur = root

            for char in word:
                if char not in cur.children:
                    cur.children[char] = TrieNode()

                cur = cur.children[char]

            cur.word = word

        rows = len(board)
        cols = len(board[0])
        result = []

        # 2. DFS through the board
        def dfs(r, c, node):
            char = board[r][c]

            # Current path is not a prefix of any word
            if char not in node.children:
                return

            next_node = node.children[char]

            # Found a complete word
            if next_node.word is not None:
                result.append(next_node.word)

                # Prevent adding the same word multiple times
                next_node.word = None

            # Mark cell as visited
            board[r][c] = "#"

            # Explore neighbors
            if r > 0:
                dfs(r - 1, c, next_node)

            if r < rows - 1:
                dfs(r + 1, c, next_node)

            if c > 0:
                dfs(r, c - 1, next_node)

            if c < cols - 1:
                dfs(r, c + 1, next_node)

            # Backtrack
            board[r][c] = char

            # Optional pruning:
            # If this Trie branch has nothing left, delete it.
            if not next_node.children and next_node.word is None:
                del node.children[char]

        # 3. Try every board cell as a starting point
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return result