# Hướng dẫn cài đặt

## 1. Yêu cầu hệ thống
Trước khi bắt đầu, hãy đảm bảo máy tính của bạn đáp ứng các yêu cầu sau:
- **Python**: Phiên bản 3.8 trở lên.
- **Thư viện bắt buộc**: 
  - `numpy` (hỗ trợ tính toán số học).
  - `tkinter` (thư viện giao diện đồ họa, tích hợp sẵn trong Python).

---

## 2. Các bước cài đặt

### 2.1. Cài đặt Python
1. **Tải Python**:
   - Truy cập [https://www.python.org/](https://www.python.org/) để tải phiên bản phù hợp với hệ điều hành của bạn.
2. **Cài đặt Python**:
   - Trong quá trình cài đặt, chọn **Add Python to PATH** để tiện sử dụng Python từ terminal/command prompt.
3. **Kiểm tra cài đặt**:
   - Mở terminal hoặc command prompt và chạy:
     ```bash
     python --version
     ```
   - Kết quả sẽ hiển thị phiên bản Python, ví dụ: `Python 3.10.0`.

---

### 2.2. Tạo môi trường ảo
1. **Tạo môi trường ảo**:
   - Chạy lệnh sau trong thư mục dự án:
     ```bash
     python -m venv venv
     ```
2. **Kích hoạt môi trường ảo**:
   - Trên Windows:
     ```bash
     venv\Scripts\activate
     ```
   - Trên macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

---

### 2.3. Cài đặt các thư viện cần thiết
1. **Cài đặt thư viện từ requirements.txt**:
   - Chạy lệnh:
     ```bash
     pip install -r setup/requirements.txt
     ```
   - Nếu không có `requirements.txt`, bạn có thể cài thủ công:
     ```bash
     pip install numpy
     ```

2. **Kiểm tra các thư viện đã cài**:
   - Chạy:
     ```bash
     pip list
     ```
   - Đảm bảo các thư viện `numpy` và `tkinter` đã có trong danh sách.

---

### 2.4. Tải hoặc sao chép mã nguồn
1. **Clone dự án từ GitHub**:
   - Nếu dự án được lưu trên GitHub, dùng lệnh:
     ```bash
     git clone <URL_REPOSITORY>
     cd <TÊN_THƯ_MỤC>
     ```
2. **Tải tệp**:
   - Nếu bạn tải về các tệp riêng lẻ (vd: `program_110122227_PhanDangKhoa.py`, `README.md`), hãy đặt chúng trong cùng một thư mục (ví dụ: `src`).

---

## 3. Chạy chương trình
1. **Khởi động chương trình**:
   - Trong terminal hoặc command prompt, chạy:
     ```bash
     python src/program_110122227_PhanDangKhoa.py
     ```
2. **Giao diện đồ họa sẽ xuất hiện**, sẵn sàng để bạn sử dụng.

---

## 4. Gỡ lỗi và hỗ trợ
- **Lỗi thiếu thư viện `tkinter` trên Linux**:
  - Cài đặt thư viện bằng lệnh:
    ```bash
    sudo apt-get install python3-tk
    ```

- **Kiểm tra phiên bản Python**:
  - Nếu gặp lỗi không tương thích, hãy kiểm tra lại phiên bản Python bằng:
    ```bash
    python --version
    ```

- **Liên hệ hỗ trợ**:
  - Email: khoadangphan307@gmail.com
  - Điện thoại: 086-757-0650

---

## 5. Gỡ cài đặt
1. **Xóa thư mục môi trường ảo**:
   - Xóa thư mục `venv` trong thư mục dự án.
2. **Gỡ thư viện cài đặt**:
   - Nếu cần, gỡ từng thư viện bằng lệnh:
     ```bash
     pip uninstall <tên_thư_viện>
     ```
3. **Xóa dự án**:
   - Xóa toàn bộ thư mục chứa mã nguồn.

