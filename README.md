# Thực tập đồ án cơ sở ngành: Viết chương trình mô phỏng bài toán người du lịch 

## Giới thiệu
Bài toán Người Du Lịch (Travelling Salesman Problem - TSP) là một trong những bài toán tối ưu hóa nổi tiếng trong khoa học máy tính. Mục tiêu của bài toán là tìm con đường ngắn nhất để đi qua một tập hợp các thành phố, mỗi thành phố chỉ được thăm một lần và cuối cùng quay lại thành phố xuất phát.

Đồ án này thực hiện việc mô phỏng và giải quyết bài toán TSP sử dụng các thuật toán khác nhau như Brute Force, Nearest Neighbor, 2-opt và Backtracking. Ứng dụng được xây dựng với giao diện đồ họa người dùng (GUI) sử dụng thư viện `tkinter` trong Python.

## Các thuật toán sử dụng
1. **Brute Force**: Thử tất cả các hoán vị của các thành phố để tìm ra đường đi ngắn nhất.
2. **Nearest Neighbor**: Chọn thành phố gần nhất chưa thăm để tiếp tục hành trình cho đến khi thăm hết tất cả các thành phố.
3. **2-opt**: Tối ưu hóa đường đi hiện tại bằng cách đảo ngược các đoạn đường để giảm tổng chi phí.
4. **Backtracking**:  Duyệt tất cả các đường đi khả dĩ với cắt tỉa (pruning).

## Sau khi chạy chương trình, cửa sổ giao diện người dùng sẽ hiện ra với các chức năng:
   
    - **Thêm Thành Phố**: Nhập số lượng thành phố và tọa độ của các thành phố.
    - **Chọn Thuật Toán**: Chọn thuật toán để giải quyết bài toán TSP.
    - **Mô Phỏng**: Chạy thuật toán đã chọn và hiển thị kết quả.
    - **Lưu/Tải Dữ Liệu**: Lưu kết quả và log vào file JSON hoặc tải dữ liệu từ file JSON.
    - **Xóa Log**: Xóa log kết quả hiện tại.
    
**Mô phỏng và kết quả**:

    - **Thêm Thành Phố**: Nhập số lượng thành phố và tọa độ thành phố hoặc tạo ngẫu nhiên các thành phố trong giới hạn của canvas.
    - **Chọn Thuật Toán**: Chọn một trong các thuật toán Brute Force, Nearest Neighbor, 2-opt hoặc Backtracking.
    - **Mô Phỏng**: Bấm nút "Mô phỏng" để chạy thuật toán và xem kết quả trên canvas.
    - **Lưu/Tải Dữ Liệu**: Sử dụng các nút "Lưu kết quả", "Tải thành phố", "Lưu Log", và "Tải Log" để lưu hoặc tải dữ liệu từ file JSON.
    - **Xóa Log**: Bấm nút "Xóa log" để xóa log kết quả hiện tại.

## Thông Tin

Nếu gặp bất kỳ vấn đề nào trong quá trình cài đặt hoặc sử dụng, vui lòng liên hệ với `Phan Đăng Khoa` qua email khoadangphan307@gmail.com.

MSSV: 110122227

Mã lớp: DA22TTB

`GVHD: Trầm Hoàng Nam`
