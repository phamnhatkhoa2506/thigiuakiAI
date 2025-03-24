import numpy as np
import matplotlib.pyplot as plt

class LinearRegression:
    def __init__(self, lr=0.01, epochs=1000, batch_size=1):
        self.lr = lr
        self.epochs = epochs
        self.batch_size = batch_size
        self.W = None
        self.b = None

    def fit(self, X, y):
        """Huấn luyện mô hình Linear Regression với batch size cụ thể."""
        n_samples, n_features = X.shape
        self.W = np.zeros(n_features)
        self.b = 0

        for epoch in range(self.epochs):
            indices = np.random.permutation(n_samples)  # Xáo trộn dữ liệu
            X_shuffled, y_shuffled = X[indices], y[indices]

            for i in range(0, n_samples, self.batch_size):
                X_batch = X_shuffled[i:i + self.batch_size]
                y_batch = y_shuffled[i:i + self.batch_size]

                y_pred = np.dot(X_batch, self.W) + self.b
                error = y_pred - y_batch

                # Gradient tính trung bình trên batch
                dW = (2 / self.batch_size) * np.dot(X_batch.T, error)
                db = (2 / self.batch_size) * np.sum(error)

                # Cập nhật tham số
                self.W -= self.lr * dW
                self.b -= self.lr * db

    def predict(self, X):
        """Dự đoán giá trị y cho đầu vào X."""
        return np.dot(X, self.W) + self.b

# ============================ #
# 🚀 THỬ NGHIỆM VỚI DỮ LIỆU #
# ============================ #

# Tạo dữ liệu giả lập
np.random.seed(42)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X[:, 0] + np.random.randn(100)

# Huấn luyện mô hình với 3 cách tiếp cận
models = {
    "SGD (n=1)": LinearRegression(lr=0.01, epochs=200, batch_size=1),
    "Mini-batch (n=10)": LinearRegression(lr=0.01, epochs=200, batch_size=10),
    "Batch (n=N)": LinearRegression(lr=0.01, epochs=200, batch_size=100)
}

plt.figure(figsize=(10, 5))
plt.scatter(X, y, color='gray', label="Data")

colors = ['r', 'g', 'b']
for i, (name, model) in enumerate(models.items()):
    model.fit(X, y)
    y_pred = model.predict(X)
    plt.plot(X, y_pred, color=colors[i], label=name)

plt.xlabel("X")
plt.ylabel("y")
plt.legend()
plt.title("So sánh các phương pháp huấn luyện Linear Regression")
plt.show()
