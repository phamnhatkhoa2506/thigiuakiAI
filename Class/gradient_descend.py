import numpy as np
import matplotlib.pyplot as plt

# Hàm số f(x)
def f(x):
    return x**2 - 4*x + 4

# Đạo hàm của f(x)
def grad_f(x):
    return 2*x - 4

# Thuật toán Gradient Descent
def gradient_descent(lr=0.1, max_iters=100, epsilon=1e-6):
    x = np.random.uniform(-5, 5)  # Khởi tạo x ngẫu nhiên
    history = [x]  # Lưu lịch sử x

    for i in range(max_iters):
        grad = grad_f(x)  # Tính đạo hàm
        x_new = x - lr * grad  # Cập nhật x
        
        history.append(x_new)  # Lưu lại giá trị mới

        # Kiểm tra điều kiện hội tụ
        if abs(x_new - x) < epsilon:
            break

        x = x_new  # Cập nhật giá trị x
    
    return x, f(x), history

# Chạy thuật toán
min_x, min_f, history = gradient_descent()

# Kết quả
print(f"Giá trị x tối ưu: {min_x}")
print(f"Giá trị nhỏ nhất f(x): {min_f}")

# Vẽ đồ thị
x_vals = np.linspace(-2, 6, 100)
y_vals = f(x_vals)

plt.plot(x_vals, y_vals, label="f(x) = x^2 - 4x + 4", color="blue")
plt.scatter(history, [f(x) for x in history], color="red", label="Gradient Descent Steps")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.title("Gradient Descent tìm cực tiểu")
plt.show()
