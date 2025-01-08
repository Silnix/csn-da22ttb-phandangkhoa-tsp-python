# Mô phỏng bài toán người du lịch - TSP_Project

## Mô tả đồ án
Dự án này mô phỏng bài toán Người Du Lịch (Traveling Salesman Problem - TSP) bằng Python. Mục tiêu là tìm đường đi ngắn nhất qua tất cả các thành phố và quay lại điểm xuất phát. Dự án cung cấp giao diện đồ họa thân thiện để người dùng tương tác.

Thuật toán được triển khai:
- **Nearest Neighbor**: Chọn thành phố gần nhất chưa được ghé thăm.

---

## Tính năng chính
- **Giao diện đồ họa**: Cung cấp giao diện trực quan cho phép nhập dữ liệu thành phố, chạy thuật toán, và hiển thị kết quả.
- **Quản lý dữ liệu**: Lưu và tải lại log kết quả tính toán từ tệp JSON.
- **Hiển thị kết quả chi tiết**: Bao gồm chi phí, đường đi, và thời gian thực hiện thuật toán.

---

## Cấu trúc thư mục
- `progress-report/`: Nơi lưu các báo cáo tiến độ.
- `setup/`: Chứa tệp hướng dẫn cài đặt và các tập tin cần thiết.
- `scr/`: Chứa mã nguồn chính của dự án.
- `thesis/`: Chứa các tài liệu liên quan đến đồ án với các thư mục con:
  - `doc/`: Tài liệu Word (.doc).
  - `pdf/`: Tài liệu PDF.
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
1. **Cài đặt Python**: Tải và cài đặt từ [https://www.python.org/](https://www.python.org/).
2. **Cài đặt thư viện**:
   - Sử dụng lệnh sau để cài đặt các thư viện từ tệp `requirements.txt`:
     ```bash
     pip install -r setup/requirements.txt
     ```

### 3. Chạy chương trình
1. Thực hiện lệnh sau trong terminal:
   ```bash
   python src/program_110122227_PhanDangKhoa.py
   ```
2. Giao diện sẽ được mở ra để bạn có thể tương tác.

---

## Cách sử dụng
1. **Nhập dữ liệu**:
   - Tạo ngẫu nhiên các thành phố.
   - Nhập tọa độ các thành phố thủ công.
2. **Chọn thuật toán**: Hiện tại, chương trình hỗ trợ thuật toán Nearest Neighbor.
3. **Xem kết quả**:
   - Đường đi được hiển thị trên giao diện đồ họa.
   - Các thông tin chi tiết như chi phí, thời gian được lưu trong bảng log.

---

## Thông tin liên hệ
- **Tác giả**: Phan Đăng Khoa
- **Email**: [khoadangphan307@gmail.com](mailto:khoadangphan307@gmail.com)
- **Số điện thoại**: (+84) 086-756-0650
