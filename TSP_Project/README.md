# Mô phỏng bài toán người du lịch - TSP Project

## Giới thiệu
Dự án này là mô phỏng bài toán người du lịch (Traveling Salesman Problem) với giao diện đồ họa trực quan và các thuật toán tối ưu hóa như:
- Brute Force
- Nearest Neighbor
- 2-opt
- Backtracking

Dự án được phát triển bằng Python và sử dụng thư viện Tkinter để xây dựng giao diện đồ họa.

## Cấu trúc thư mục
- `setup/`: Chứa tệp hướng dẫn cài đặt và các tập tin cần thiết.
- `scr/`: Chứa mã nguồn chính của dự án.
- `progress-report/`: Nơi lưu các báo cáo tiến độ.
- `thesis/`: Chứa các tài liệu liên quan đến đồ án với các thư mục con:
  - `doc/`: Tài liệu Word (.doc).
  - `pdf/`: Tài liệu PDF.
  - `html/`: Tài liệu web.
  - `abs/`: Báo cáo (PPT, AVI, ...).
  - `refs/`: Tài liệu tham khảo.

## Hướng dẫn cài đặt và sử dụng
1. **Cài đặt môi trường**: Xem chi tiết trong [INSTALL.md](setup/INSTALL.md).
2. **Chạy chương trình**:
    ```bash
    python scr/main.py
    ```
3. **Các thuật toán hỗ trợ**:
   - Brute Force: Thử tất cả các hoán vị để tìm đường đi tối ưu.
   - Nearest Neighbor: Chọn thành phố gần nhất chưa được thăm.
   - 2-opt: Tối ưu hóa đường đi ban đầu bằng cách hoán đổi các cạnh.
   - Backtracking: Duyệt tất cả các đường đi khả dĩ với cắt tỉa (pruning).

## Thông tin liên hệ
- Email: khoadangphan307@gmail.com
- Điện thoại: 0867570650
