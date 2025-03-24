import numpy as np
from cvxopt import matrix, solvers  # Thư viện giải tối ưu hóa
from sklearn.datasets import make_moons  # Dữ liệu thử nghiệm
import matplotlib.pyplot as plt

class SVM_RBF:
    def __init__(self, C=1.0, gamma=0.5):
        self.C = C  # Hệ số điều chỉnh lỗi lề mềm
        self.gamma = gamma  # Hệ số gamma cho kernel RBF

    def rbf_kernel(self, X1, X2):
        """Hàm kernel RBF: K(x, x') = exp(-gamma ||x - x'||^2)"""
        return np.exp(-self.gamma * np.linalg.norm(X1[:, np.newaxis] - X2, axis=2) ** 2)

    def fit(self, X, y):
        """Huấn luyện SVM bằng cách giải bài toán tối ưu"""
        n_samples, n_features = X.shape
        y = y.astype(np.double)

        # Tính toán Kernel Gram matrix (K_ij = K(x_i, x_j))
        K = self.rbf_kernel(X, X)

        # Cấu trúc bài toán tối ưu hóa dạng Quadratic Programming
        P = matrix(np.outer(y, y) * K)
        q = matrix(-np.ones(n_samples))
        G = matrix(np.vstack((-np.eye(n_samples), np.eye(n_samples))))
        h = matrix(np.hstack((np.zeros(n_samples), np.ones(n_samples) * self.C)))
        A = matrix(y.reshape(1, -1), tc='d')
        b = matrix(0.0)

        # Giải bài toán tối ưu
        solvers.options['show_progress'] = False
        solution = solvers.qp(P, q, G, h, A, b)
        alphas = np.ravel(solution['x'])

        # Chọn các support vectors (alpha > 0)
        support_vector_indices = alphas > 1e-5
        self.alphas = alphas[support_vector_indices]
        self.support_vectors = X[support_vector_indices]
        self.support_labels = y[support_vector_indices]

        # Tính bias (b)
        self.b = np.mean(self.support_labels - np.sum(self.alphas * self.support_labels * K[support_vector_indices][:, support_vector_indices], axis=1))

    def predict(self, X):
        """Dự đoán nhãn của mẫu X"""
        K = self.rbf_kernel(X, self.support_vectors)
        return np.sign(np.sum(self.alphas * self.support_labels * K, axis=1) + self.b)

# ========================== #
# 📌 THỬ NGHIỆM MÔ HÌNH #
# ========================== #

# Tạo dữ liệu không tuyến tính
X, y = make_moons(n_samples=100, noise=0.1, random_state=42)
y = np.where(y == 0, -1, 1)  # Chuyển nhãn từ {0,1} thành {-1,1}

# Huấn luyện mô hình SVM với kernel RBF
svm = SVM_RBF(C=1.0, gamma=1.0)
svm.fit(X, y)

# Vẽ kết quả
xx, yy = np.meshgrid(np.linspace(-2, 3, 100), np.linspace(-2, 3, 100))
Z = svm.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

plt.contourf(xx, yy, Z, alpha=0.3, cmap=plt.cm.coolwarm)
plt.scatter(X[:, 0], X[:, 1], c=y, s=30, cmap=plt.cm.coolwarm, edgecolors='k')
plt.title("SVM với Kernel RBF")
plt.show()
