class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def areNeighbors(word1, word2):
            diff = False
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    if diff: return False
                    else: diff = True
            
            return True
        
        adjList = defaultdict(list)
        wordList.append(beginWord)
        for word1 in wordList:
            for word2 in wordList:
                if word1 != word2 and areNeighbors(word1, word2):
                    adjList[word1].append(word2)
        wordList.pop()

        q = deque([beginWord])
        count = 0
        visited = set()

        while q:
            count += 1

            for _ in range(len(q)):
                word = q.popleft()
                print(word, count)
                print(adjList[word])

                if word == endWord: return count
                elif word in visited: continue
                else:
                    visited.add(word)

                    for neighbor in adjList[word]:
                        q.append(neighbor)
                    

        
        return 0



