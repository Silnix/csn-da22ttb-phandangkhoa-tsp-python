# Mô phỏng bài toán người du lịch - TSP-Project

## Mô tả dự án
Dự án này mô phỏng bài toán Người Du Lịch (Traveling Salesman Problem - TSP) bằng Python. Mục tiêu là tìm đường đi ngắn nhất qua tất cả các thành phố và quay lại điểm xuất phát. Dự án cung cấp giao diện đồ họa thân thiện để người dùng tương tác.

Các thuật toán được triển khai:
- Brute Force: Thử tất cả các hoán vị để tìm đường đi tối ưu.
- Nearest Neighbor: Chọn thành phố gần nhất chưa được thăm.
- 2-opt: Tối ưu hóa đường đi ban đầu bằng cách hoán đổi các cạnh.
- Backtracking: Duyệt tất cả các đường đi khả dĩ với cắt tỉa (pruning).

---

## Tính năng chính
- **Giao diện đồ họa**: Cho phép nhập dữ liệu thành phố, chọn thuật toán, và xem kết quả trực quan.
- **Thuật toán tối ưu**: Triển khai nhiều phương pháp khác nhau để giải bài toán TSP.
- **Quản lý dữ liệu**: Lưu và tải dữ liệu thành phố hoặc kết quả tính toán từ tệp JSON.

---

## Cấu trúc thư mục
- `progress-report/`: Nơi lưu các báo cáo tiến độ.
- `setup/`: Chứa tệp hướng dẫn cài đặt và các tập tin cần thiết.
- `scr/`: Chứa mã nguồn chính của dự án.
- `thesis/`: Chứa các tài liệu liên quan đến đồ án với các thư mục con:
  - `doc/`: Tài liệu Word (.doc).
  - `pdf/`: Tài liệu PDF.
  - `html/`: Tài liệu web.
  - `abs/`: Báo cáo (PPT, AVI, ...).
  - `refs/`: Tài liệu tham khảo.
- `README.md`: Tệp mô tả đồ án
---

## Hướng dẫn cài đặt

### 1. Yêu cầu hệ thống
- **Python**: Phiên bản 3.8 trở lên.
- **Thư viện bắt buộc**:
  - `numpy`
  - `tkinter`

### 2. Cài đặt
Xem tệp [INSTALL.md](setup/INSTALL.md) trong thư mục `setup/` để biết chi tiết về cách thiết lập môi trường.
1. **Cài đặt Python**: Tải và cài đặt từ [https://www.python.org/](https://www.python.org/).
2. **Cài đặt thư viện**:
   - Dùng `pip` để cài các thư viện từ tệp `requirements.txt`:
     ```bash
     pip install -r setup/requirements.txt
     ```
	 
### 3. Chạy chương trình
1. Chạy lệnh sau trong terminal:
   ```bash
   python src/main.py
   ```
2. Giao diện sẽ mở ra, cho phép bạn tương tác.

3. Tương tác với giao diện
Nhập số lượng thành phố hoặc tọa độ các thành phố.
Chọn thuật toán để giải bài toán.
Nhấn Mô phỏng để xem kết quả.

## Thông tin liên hệ
Email: khoadangphan307@gmail.com
Điện thoại: 0867560650
