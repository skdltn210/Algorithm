class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        set1=set(word1)
        set2=set(word2)
        map1={}
        map2={}
        for i in range(len(word1)):
            if word1[i] in map1: map1[word1[i]]+=1
            else: map1[word1[i]]=1
        for i in range(len(word2)):
            if word2[i] in map2: map2[word2[i]]+=1
            else: map2[word2[i]]=1
        if set1 != set2: return False
        if sorted(list(map1.values())) != sorted(list(map2.values())): return False
        return True