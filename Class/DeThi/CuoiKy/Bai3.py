import pandas as pd
import numpy as np
from sklearn.cluster import KMeans

# Đọc dữ liệu từ tập tin input.csv
data = pd.read_csv('input.csv')

X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values

# Số lượng cụm mong muốn
k = 3

# Áp dụng thuật toán K-means
kmeans = KMeans(n_clusters=k, random_state=20)
kmeans.fit(X)

# Nhãn của các mẫu dữ liệu sau khi phân cụm
labels = kmeans.labels_
# Tọa độ của các trung tâm cụm
centroids = kmeans.cluster_centers_

# In kết quả
print("Nhãn của các mẫu dữ liệu:")
print(labels)
print("Tọa độ của các trung tâm cụm:")
print(centroids)