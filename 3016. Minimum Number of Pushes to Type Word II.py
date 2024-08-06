from collections import defaultdict
class Solution:
    def minimumPushes(self, word: str) -> int:
        frequencies = defaultdict(int)
        keys = [''] 
        for i in range(len(word)):
            frequencies[word[i]] += 1
        sorted_keys = [k for k, v in sorted(frequencies.items(), key=lambda item: item[1], reverse=True)]
        keys = [''] * 8
        for i in range(len(sorted_keys)):
            keys[i % 8] = keys[i % 8] + sorted_keys[i]
        clicks = 0
        for i in range(len(word)):
            for j in range(len(keys)):
                index = keys[j].find(word[i])
                if index > -1:
                    clicks += (index + 1)
        return clicks