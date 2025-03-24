import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Đọc dữ liệu từ file CSV
data = pd.read_csv('input.csv')

# Chia dữ liệu thành đặc trưng và nhãn
X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values

# Xây dựng mô hình Logistic Regression với Softmax
model = LogisticRegression(multi_class='multinomial', solver='lbfgs')
model.fit(X, y)

# Dự đoán nhãn cho tập kiểm tra
# Đánh giá độ chính xác của mô hình
dataTest = pd.read_csv('output.csv')

y_pred = model.predict(dataTest)
print(y_pred)