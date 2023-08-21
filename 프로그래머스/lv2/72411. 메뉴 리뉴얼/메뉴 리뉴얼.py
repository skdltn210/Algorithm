from itertools import combinations
from collections import Counter

def solution(orders, course):
    ans = []
    for c in course:
        all_combinations = Counter()
        for order in orders:
            for combi in combinations(sorted(order), c):
                all_combinations[combi] += 1
                
        if all_combinations:
            max_count = max(all_combinations.values())
            if max_count >= 2:
                for combo, count in all_combinations.items():
                    if count == max_count:
                        ans.append(''.join(combo))

    return sorted(ans)