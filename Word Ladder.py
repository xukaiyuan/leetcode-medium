class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        word_list = set(wordList)
        queue = [beginWord]
        record = {beginWord: 1}

        while(len(queue) != 0):
            current = queue.pop(0)

            for i in range(len(current)):
                for j in string.ascii_lowercase:
                    if(current[i] == j):
                        continue                
                    newWord = current[:i] + j + current[i + 1:]
                    if(newWord in word_list and newWord not in record):
                        record[newWord] = record[current] + 1
                        if(newWord == endWord):
                            return record[newWord]
                        queue.append(newWord)

        return 0