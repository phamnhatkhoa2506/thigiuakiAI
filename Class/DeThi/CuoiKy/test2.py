# 102190017_VoTuanManhHung bài 2

import numpy as np

def euclidean_distance(a, b):
    return np.sqrt(np.sum((a - b) ** 2))

def kmeans(data, k, num_iterations):
    # Khởi tạo ngẫu nhiên các điểm trung tâm ban đầu
    centroids = data[np.random.choice(range(len(data)), size=k, replace=False)]

    for _ in range(num_iterations):
        # Gán mỗi điểm dữ liệu cho cụm gần nhất
        clusters = [[] for _ in range(k)]
        for point in data:
            distances = [euclidean_distance(point, centroid) for centroid in centroids]
            cluster_index = np.argmin(distances)
            clusters[cluster_index].append(point)

        # Cập nhật vị trí của các điểm trung tâm
        for i in range(k):
            if len(clusters[i]) > 0:
                centroids[i] = np.mean(clusters[i], axis=0)

    return centroids, clusters

# Dữ liệu đầu vào
data = np.array([[3, 12], [6, 9], [4.5, 12], [12, 3], [15, 6], [12, 15], [9, 18], [9, 12]])

# Số cụm (clusters) và số lần lặp
k = 3
num_iterations = 100

# Thực hiện thuật toán K-means
centroids, clusters = kmeans(data, k, num_iterations)

# In ra kết quả
print("Các trung tâm cụm:")
print(centroids)
print("\nCác điểm dữ liệu trong từng cụm:")
for i, cluster in enumerate(clusters):
    print(f"Cụm {i+1}: {cluster}")
