from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if set(word1) != set(word2):
            return False

        freq1 = Counter(word1)
        freq2 = Counter(word2)
        return Counter(freq1.values()) == Counter(freq2.values())