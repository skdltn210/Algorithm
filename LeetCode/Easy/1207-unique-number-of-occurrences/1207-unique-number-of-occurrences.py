class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        map={}
        for num in arr:
            if not num in map:
                map[num]=1
            else:
                map[num]+=1
        arr=list(map.values())
        arr.sort()
        for i in range(len(arr)-1):
            if arr[i]==arr[i+1]: return False
        return True