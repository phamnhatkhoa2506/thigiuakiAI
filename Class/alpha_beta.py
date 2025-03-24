'''
    *** Chiến lược Cắt Tỉa Alpha-Beta (Alpha-Beta Pruning) ***
    Cắt tỉa Alpha-Beta là một kỹ thuật tối ưu hóa được sử dụng trong thuật toán Minimax để giảm số lượng nút cần duyệt trong 
    cây tìm kiếm. Kỹ thuật này giúp tăng tốc độ tìm kiếm mà không ảnh hưởng đến kết quả cuối cùng.

    *** Mô tả thuật toán ***
        - Khi tìm kiếm trên cây Minimax, ta có hai giá trị quan trọng tại mỗi nút:
            + Alpha (α): Giá trị tốt nhất mà người chơi "Max" (người cần tối đa hóa điểm) có thể đạt được.
            + Beta (β): Giá trị tốt nhất mà người chơi "Min" (người cần tối thiểu hóa điểm) có thể đạt được.

        - Ý tưởng chính:
            + Nếu một nút con có giá trị tồi hơn so với mức tốt nhất mà cha nó có thể đảm bảo, ta có thể bỏ qua tất cả 
              các nút con của nó mà không cần xét tiếp.
            + Điều này giúp giảm số nút cần xét, cải thiện hiệu suất đáng kể.

    *** Cách hoạt động ***
        1️⃣ Khi duyệt nút Max
            - Cập nhật Alpha (α): Nếu tìm thấy một giá trị lớn hơn α, ta cập nhật α.
            - Cắt tỉa: Nếu 𝛼 ≥ 𝛽, ta dừng xét các con còn lại của nút đó.
        2️⃣ Khi duyệt nút Min
            - Cập nhật Beta (β): Nếu tìm thấy một giá trị nhỏ hơn β, ta cập nhật β.
            - Cắt tỉa: Nếu 𝛼 ≥ 𝛽, ta dừng xét các con còn lại của nút đó.
'''

import math

# Hàm đánh giá giá trị của một trạng thái (đối với các nút lá)
def evaluate(state):
    return state  # Trong ví dụ này, trạng thái là giá trị của chính nút lá

# Thuật toán Minimax với cắt tỉa Alpha-Beta
def alpha_beta_pruning(depth, node_index, is_maximizing, values, alpha, beta):
    # Nếu đạt độ sâu tối đa, trả về giá trị của nút lá
    if depth == 3:  
        return values[node_index]

    if is_maximizing:
        max_eval = -math.inf
        # Mỗi nút có 2 con, xét lần lượt
        for i in range(2):
            eval_value = alpha_beta_pruning(depth + 1, node_index * 2 + i, False, values, alpha, beta)
            max_eval = max(max_eval, eval_value)
            alpha = max(alpha, eval_value)
            if beta <= alpha:
                break  # Cắt tỉa Beta (vì MIN sẽ không chọn nhánh này)
        return max_eval
    else:
        min_eval = math.inf
        for i in range(2):
            eval_value = alpha_beta_pruning(depth + 1, node_index * 2 + i, True, values, alpha, beta)
            min_eval = min(min_eval, eval_value)
            beta = min(beta, eval_value)
            if beta <= alpha:
                break  # Cắt tỉa Alpha (vì MAX sẽ không chọn nhánh này)
        return min_eval

# Danh sách giá trị tại các nút lá
values = [3, 5, 6, 9, 1, 2, 0, -1]

# Gọi thuật toán từ gốc (độ sâu = 0, node_index = 0, MAX là người chơi đầu tiên)
optimal_value = alpha_beta_pruning(0, 0, True, values, -math.inf, math.inf)

print(f"Giá trị tối ưu mà MAX có thể đạt được là: {optimal_value}")
