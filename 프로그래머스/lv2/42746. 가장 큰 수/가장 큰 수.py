def solution(numbers):
    ans = ''
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x : (x*4)[:4], reverse=True)        
    ans = ''.join(numbers)
    if ans[0]=='0':
        return '0'
    else:
        return ans