from itertools import combinations
def solution(relation):
    columns = len(relation[0])
    candidates = []
    for num in range(1, columns + 1):
        for combination in combinations(range(columns), num):
            subset = [tuple(row[column] for column in combination) for row in relation]
            if is_unique(subset) and is_minimal(candidates, combination):
                candidates.append(combination)
    return len(candidates)

def is_unique(subset):
    return len(subset) == len(set(subset))

def is_minimal(candidates, combination):
    for candidate in candidates:
        if set(candidate).issubset(set(combination)):
            return False
    return True