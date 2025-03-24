import numpy as np
import matplotlib.pyplot as plt

# Hàm số f(x)
def f(x):
    return -x**2 + 4*x

# Đạo hàm của f(x)
def grad_f(x):
    return -2*x + 4

# Gradient Descent with Momentum
def gradient_descent_with_momentum(lr=0.1, beta=0.9, max_iters=50, epsilon=1e-6):
    x = np.random.uniform(-5, 5)  # Khởi tạo x ngẫu nhiên
    v = 0  # Vận tốc ban đầu
    
    history = [x]  # Lưu lịch sử x
    
    for i in range(max_iters):
        grad = grad_f(x)
        v = beta * v + lr * grad  # Cập nhật vận tốc
        x += v  # Cập nhật x
        
        history.append(x)  # Lưu lại vị trí mới
        
        # Điều kiện dừng nếu cập nhật nhỏ
        if abs(lr * grad) < epsilon:
            break
            
    return x, f(x), history

# Chạy thuật toán
max_x, max_f, history = gradient_descent_with_momentum()

# Kết quả
print(f"Giá trị x tối ưu: {max_x}")
print(f"Giá trị lớn nhất f(x): {max_f}")

# Vẽ đồ thị
x_vals = np.linspace(-1, 5, 100)
y_vals = f(x_vals)

plt.plot(x_vals, y_vals, label="f(x) = -x^2 + 4x", color="blue")
plt.scatter(history, [f(x) for x in history], color="red", label="Gradient Descent Steps")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.title("Gradient Descent with Momentum tìm cực đại")
plt.show()
