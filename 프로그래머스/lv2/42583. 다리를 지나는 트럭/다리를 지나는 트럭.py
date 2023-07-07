from collections import deque
def solution(bridge_length, weight, truck_weights):
    cnt = 0
    truck = deque(truck_weights)
    bridge = deque([0] * bridge_length)
    current_weight = 0
    while truck or current_weight > 0:
        cnt+=1
        current_weight -= bridge.popleft()
        if truck and current_weight + truck[0] <= weight:
            current_truck = truck.popleft()
            bridge.append(current_truck)
            current_weight += current_truck
        else:
            bridge.append(0)
        
    return cnt