'''
    --- Mô tả thuật toán Minimax ---
    
    Minimax hoạt động theo nguyên tắc:
        - Người chơi MAX (chúng ta) cố gắng tối đa hóa điểm số.
        - Người chơi MIN (đối thủ) cố gắng tối thiểu hóa điểm số.
    Cây trò chơi được xây dựng với các nút biểu diễn trạng thái của trò chơi, trong đó:
        - Nút MAX: Chọn giá trị lớn nhất từ các nút con.
        - Nút MIN: Chọn giá trị nhỏ nhất từ các nút con.

    Hàm Minimax(nút, độ sâu, isMax):
    Nếu nút là trạng thái kết thúc hoặc độ sâu = 0:
        Trả về giá trị đánh giá của nút
    
    Nếu isMax:
        Giá trị tốt nhất = -∞
        Duyệt qua tất cả nước đi có thể từ nút hiện tại:
            Giá trị tốt nhất = max(Giá trị tốt nhất, Minimax(nước đi, độ sâu - 1, False))
        Trả về Giá trị tốt nhất
    Ngược lại:  # Đến lượt MIN
        Giá trị tốt nhất = +∞
        Duyệt qua tất cả nước đi có thể từ nút hiện tại:
            Giá trị tốt nhất = min(Giá trị tốt nhất, Minimax(nước đi, độ sâu - 1, True))
        Trả về Giá trị tốt nhất

    --- Ứng dụng của thuật toán Minimax ---
    1. Trò chơi trên bảng (Board Games)

        Thuật toán Minimax được sử dụng rộng rãi trong các trò chơi có hai người chơi với tổng điểm bằng 0 (zero-sum games), 
        chẳng hạn như:
            - Cờ vua (Chess)
            - Cờ caro (Tic-tac-toe)
            - Cờ vây (Go)
            - Cờ tướng, cờ vua, cờ Othello...

        Trong các trò chơi này:
            - Min đại diện cho đối thủ (người muốn giảm lợi thế của bạn).
            - Max đại diện cho người chơi chính (người muốn tối đa hóa điểm số).
            - Thuật toán duyệt qua cây trạng thái để dự đoán nước đi tiếp theo và chọn nước đi có lợi nhất.

        🔹 Ví dụ: Cờ caro (Tic-Tac-Toe)
        AI sẽ xem xét mọi nước đi có thể và chọn nước đi giúp nó thắng hoặc tránh thua.

    2. AI trong trò chơi điện tử (Game AI)
        Minimax được ứng dụng để thiết kế AI trong nhiều trò chơi điện tử, đặc biệt là các trò chơi chiến 
        thuật.
        - Game chiến thuật theo lượt (Turn-based strategy games) như Civilization, Fire Emblem.
        - Game đánh cờ như Chess AI trong Stockfish, AlphaZero.

        Khi kết hợp với thuật toán Alpha-Beta Pruning, hiệu suất của Minimax được cải thiện đáng kể.

    3. Ra quyết định trong kinh tế và tài chính
        Trong các tình huống đàm phán, kinh doanh, và thị trường tài chính, Minimax có thể giúp dự đoán 
        hành vi của đối thủ (công ty cạnh tranh).
        - Chiến lược giá cả giữa các công ty cạnh tranh
        - Phân tích rủi ro trong giao dịch tài chính
        - Lập kế hoạch đấu thầu trong các cuộc đấu giá

        Ví dụ: Một công ty có thể sử dụng Minimax để mô phỏng chiến lược của đối thủ khi đặt giá sản phẩm.

    4. Lập kế hoạch và ra quyết định trong robot
        Minimax có thể giúp robot ra quyết định tối ưu khi thực hiện nhiệm vụ trong môi trường không chắc 
        chắn.
        - Robot có thể dùng Minimax để tìm chiến lược tránh chướng ngại vật.
        - Ứng dụng trong xe tự hành (autonomous vehicles) khi đối phó với tình huống giao thông phức tạp.
    
    5. Bảo mật và mã hóa
        - Trong an ninh mạng, Minimax được sử dụng để mô phỏng chiến lược tấn công/phòng thủ giữa hacker và hệ thống bảo mật.
        - Dùng trong thiết kế thuật toán phát hiện xâm nhập để tối ưu hóa phản ứng của hệ thống bảo mật.

    6. Xử lý ngôn ngữ tự nhiên (NLP)
        - Minimax có thể dùng trong chatbot đàm phán để chọn phản hồi hợp lý nhất khi thương lượng.
        - Ứng dụng trong AI viết văn bản đối thoại, dự đoán câu trả lời của đối phương. 

    --- Kết luận --- 
    Thuật toán Minimax có ứng dụng rộng rãi trong trí tuệ nhân tạo, trò chơi điện tử, tài chính, bảo mật, 
    robot và xử lý ngôn ngữ. Khi kết hợp với Alpha-Beta Pruning, nó trở thành một công cụ mạnh mẽ giúp đưa 
    ra quyết định tối ưu trong môi trường có hai bên đối kháng. 🚀       
'''

import math

# Hàm minimax đệ quy
def minimax(depth, node_index, is_maximizing, values, max_depth):
    # Điều kiện dừng: Nếu đạt đến nút lá
    if depth == max_depth:
        return values[node_index]

    if is_maximizing:
        best = -math.inf  # Giá trị lớn nhất cho MAX
        # Duyệt qua 2 con của nút hiện tại
        for i in range(2):
            val = minimax(depth + 1, node_index * 2 + i, False, values, max_depth)
            best = max(best, val)
        return best
    else:
        best = math.inf  # Giá trị nhỏ nhất cho MIN
        # Duyệt qua 2 con của nút hiện tại
        for i in range(2):
            val = minimax(depth + 1, node_index * 2 + i, True, values, max_depth)
            best = min(best, val)
        return best

# Danh sách giá trị tại các nút lá
values = [3, 5, 6, 9, 1, 2, 0, -1]

# Số cấp của cây (log2(số lượng nút lá))
max_depth = math.log2(len(values))

# Gọi thuật toán từ gốc (depth = 0, node_index = 0, MAX là người chơi đầu tiên)
optimal_value = minimax(0, 0, True, values, max_depth)

print(f"Giá trị tối ưu mà MAX có thể đạt được là: {optimal_value}")
