import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

# Khởi tạo tập đỉnh V
V = ["S", "A", "B", "C", "D", "E", "F", "G", "H"]

# Khởi tạo tập cạnh E dưới dạng danh sách các cặp đỉnh
E = [("S", "A"), ("S", "B"), ("S", "C"), ("A", "D"), ("B", "D"), 
     ("B", "F"), ("C", "F"), ("D", "E"), ("E", "G"), ("F", "H"), 
     ("G", "H"), ("B", "G"), ("F", "E")]

# Chuyển danh sách cạnh thành danh sách kề
graph = {v: [] for v in V}
for u, v in E:
    graph[u].append(v)
    graph[v].append(u)  # Vì đây là đồ thị vô hướng

# Tạo đồ thị vô hướng
graph = {v: [] for v in V}
for u, v in E:
    graph[u].append(v)
    graph[v].append(u)

def bfs_find_path(start, goal):
    queue = deque([(start, [start])])
    visited = set()
    order = []  # Ghi nhận thứ tự duyệt

    while queue:
        node, path = queue.popleft()
        if node in visited:
            continue
        visited.add(node)
        order.append(node)

        if node == goal:
            return order, path  # Trả về thứ tự duyệt và đường đi

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
    
    print("Khong tim thay duong di")
    return order, None  # Không tìm thấy đường đi
    

# Thực hiện BFS từ S đến G
order, path = bfs_find_path("S", "G")

# Tạo đồ thị bằng NetworkX
G = nx.Graph()
G.add_edges_from(E)

# Vẽ đồ thị
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G)  # Sắp xếp vị trí các đỉnh

# Vẽ tất cả các cạnh và đỉnh ban đầu
nx.draw(G, pos, with_labels=True, node_color="lightgray", edge_color="gray", node_size=2000, font_size=10)

# Đánh dấu thứ tự khám phá
if order:
    for i, node in enumerate(order):
        plt.text(pos[node][0], pos[node][1] + 0.05, str(i+1), fontsize=12, color="red", fontweight="bold")

# Vẽ đường đi tìm được nếu có
if path:
    path_edges = list(zip(path, path[1:]))
    nx.draw_networkx_nodes(G, pos, nodelist=path, node_color="lightblue", node_size=2000)
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color="blue", width=2)
    print("Duong di BFS:", " -> ".join(path))
else:
    print("Khong tim thay duong di")

plt.show()