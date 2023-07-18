def is_possible(stones, k, max_val):
    count = 0
    for stone in stones:
        if stone - max_val <= 0:
            count += 1
        else:
            count = 0
        if count >= k:
            return False
    return True

def solution(stones, k):
    left, right = 1, max(stones)

    while left <= right:
        mid = (left + right) // 2
        if is_possible(stones, k, mid):
            left = mid + 1
        else:
            right = mid - 1

    return left