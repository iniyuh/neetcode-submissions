class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0
        
        L = len(endWord)
        adjList = defaultdict(list)


        def updateAdjList(word1, word2):
            if word1 == word2: return

            flag = False

            for i in range(L):
                if word1[i] != word2[i]:
                    if flag: return
                    else: flag = True
            
            adjList[word1].append(word2)
            adjList[word2].append(word1)

        for word1 in wordList + [beginWord, endWord]:
            for word2 in wordList + [beginWord, endWord]: updateAdjList(word1, word2)

        visited = set()
        queue = deque()

        queue.append(beginWord)
        depth = 0

        while queue:
            for i in range(len(queue)):
                word1 = queue.popleft()

                if word1 == endWord: return depth + 1
                else:
                    for word2 in adjList[word1]:
                        if word2 not in visited:
                            queue.append(word2)
                            visited.add(word2)
            
            depth += 1
        
        return 0
