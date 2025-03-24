from heapq import heappop, heappush

class State:
    def __init__(self, g1, g2, b, prev_state=None, action=None):
        self.g1 = g1  # Lượng nước trong gáo 1
        self.g2 = g2  # Lượng nước trong gáo 2
        self.b = b  # Lượng nước trong bể
        self.prev_state = prev_state  # Trạng thái trước đó
        self.action = action  # Hành động thực hiện để đạt được trạng thái này

    def __lt__(self, other):
        return False  # Không sử dụng tính năng so sánh trong heap

    def is_goal(self, target):
        return self.b == target

    def generate_successors(self, capacities):
        successors = []
        # Chuyển/Múc từ bờ sông qua gáo 1
        if self.g1 < capacities[0]:
            successors.append(State(capacities[0], self.g2, self.b, self, "Chuyển/Múc {} lít nước từ bờ sông qua gáo 1".format(capacities[0] - self.g1)))
        # Chuyển/Múc từ bờ sông qua gáo 2
        if self.g2 < capacities[1]:
            successors.append(State(self.g1, capacities[1], self.b, self, "Chuyển/Múc {} lít nước từ bờ sông qua gáo 2".format(capacities[1] - self.g2)))
        # Chuyển/Múc từ gáo 1 qua bể
        if self.g1 > 0 and self.b < capacities[2]:
            amount = min(self.g1, capacities[2] - self.b)
            successors.append(State(self.g1 - amount, self.g2, self.b + amount, self, "Chuyển/Múc {} lít nước từ gáo 1 qua bể".format(amount)))
        # Chuyển/Múc từ gáo 2 qua bể
        if self.g2 > 0 and self.b < capacities[2]:
            amount = min(self.g2, capacities[2] - self.b)
            successors.append(State(self.g1, self.g2 - amount, self.b + amount, self, "Chuyển/Múc {} lít nước từ gáo 2 qua bể".format(amount)))
        # Chuyển/Múc từ gáo 1 qua gáo 2
        if self.g1 > 0 and self.g2 < capacities[1]:
            amount = min(self.g1, capacities[1] - self.g2)
            successors.append(State(self.g1 - amount, self.g2 + amount, self.b, self, "Chuyển/Múc {} lít nước từ gáo 1 qua gáo 2".format(amount)))
        # Chuyển/Múc từ gáo 2 qua gáo 1
        if self.g2 > 0 and self.g1 < capacities[0]:
            amount = min(self.g2, capacities[0] - self.g1)
            successors.append(State(self.g1 + amount, self.g2 - amount, self.b, self, "Chuyển/Múc {} lít nước từ gáo 2 qua gáo 1".format(amount)))

        return successors

def astar_search(initial_state, target, capacities):
    visited = set()
    heap = [(0, initial_state)]
    
    while heap:
        _, current_state = heappop(heap)
        
        if current_state.is_goal(target):
            return get_solution(current_state)
        
        visited.add(current_state)
        
        successors = current_state.generate_successors(capacities)
        for successor in successors:
            if successor not in visited:
                priority = heuristic(successor, target)
                heappush(heap, (priority, successor))
    
    return None

def heuristic(state, target):
    return abs(state.b - target)

def get_solution(state):
    solution = []
    while state.prev_state is not None:
        solution.append(state.action)
        state = state.prev_state
    solution.reverse()
    return solution

# Hàm main
def main():
    n, M, *a = map(int, input().split())
    
    initial_state = State(0, 0, 0)
    target = M
    capacities = a
    
    solution = astar_search(initial_state, target, capacities)
    if solution is None:
        print("Không có đáp án")
    else:
        for step in solution:
            print(step)

if __name__ == "__main__":
    main()