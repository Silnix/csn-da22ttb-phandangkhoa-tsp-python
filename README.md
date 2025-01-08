# Viết chương trình mô phỏng bài toán người du lịch (Traveling Salesman Problem - TSP)

## Giới thiệu

Bài toán người du lịch (Traveling Salesman Problem - TSP) là một trong những bài toán nổi tiếng trong lý thuyết đồ thị và tối ưu hóa. Mục tiêu là tìm hành trình ngắn nhất qua tất cả các thành phố trong một danh sách, ghé thăm mỗi thành phố đúng một lần trước khi trở lại điểm xuất phát. Ứng dụng rộng rãi trong logistics, lập lịch trình, và tối ưu hóa mạng.

**Giải pháp của dự án:** 
- Sử dụng thuật toán Nearest Neighbor, một phương pháp heuristic đơn giản nhưng hiệu quả.
- Giao diện đồ họa trực quan, hỗ trợ nhập liệu và hiển thị kết quả chi tiết.

## Chức năng chính
- **Nhập dữ liệu**: Người dùng có thể tạo thành phố ngẫu nhiên hoặc nhập tọa độ thủ công.
- **Hiển thị đồ thị**: Biểu diễn trực quan các thành phố và kết nối giữa chúng.
- **Chạy thuật toán**: Tìm đường đi ngắn nhất bằng thuật toán Nearest Neighbor.
- **Quản lý log**: Lưu và tải kết quả tính toán dưới dạng file JSON.
- **Hiển thị ma trận**: Hiển thị ma trận khoảng cách và trọng số.

## Công nghệ sử dụng
- **Ngôn ngữ lập trình**: Python.
- **Thư viện chính**:
  - Tkinter: Tạo giao diện người dùng.
  - NumPy: Tính toán ma trận.
  - JSON: Quản lý lưu trữ log.
  - itertools, random, math: Hỗ trợ các tính toán và thuật toán cơ bản.

## Hướng dẫn sử dụng
1. **Cài đặt Python**: Đảm bảo Python đã được cài đặt trên máy (>= phiên bản 3.7).
2. **Cài đặt thư viện**: Chạy lệnh sau để cài đặt các thư viện cần thiết:
   ```bash
   pip install numpy
   ```
3. **Chạy chương trình**:
   ```bash
   python program_110122227_PhanDangKhoa.py
   ```
4. **Thực hiện các chức năng**:
   - Tạo ngẫu nhiên các thành phố.
   - Nhập tọa độ thành phố thủ công.
   - Chạy thuật toán và xem kết quả trực tiếp trên giao diện.

## Kết quả nổi bật
- Tìm được đường đi và chi phí gần tối ưu cho các bài toán kích thước nhỏ đến trung bình.
- Giao diện trực quan, dễ sử dụng và thân thiện với người dùng.
- Hỗ trợ quản lý log kết quả và tải lại để phân tích.

## Hướng phát triển
- Tích hợp các thuật toán tối ưu khác như Genetic Algorithm, Simulated Annealing.
- Nâng cấp giao diện thành ứng dụng web.
- Hỗ trợ nhập dữ liệu từ bản đồ thực tế hoặc API địa lý.

## Liên hệ
- **Tác giả**: Phan Đăng Khoa
- **Email**: [khoadangphan307@gmail.com](mailto:khoadangphan307@gmail.com)
- **Số điện thoại**: 0867570650
- **GVHD**: Trầm Hoàng Nam
