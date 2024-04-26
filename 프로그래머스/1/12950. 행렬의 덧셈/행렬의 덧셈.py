def solution(arr1, arr2):
    ans = []
    for i in range(len(arr1)):
        ans1 = []
        for j in range(len(arr1[0])):
            ans1.append(arr1[i][j]+arr2[i][j])
        ans.append(ans1)
    return ans