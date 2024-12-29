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

### 2.2. Tạo môi trường ảo (khuyến nghị)
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
   - Nếu bạn tải về các tệp riêng lẻ (vd: `main.py`, `tsp_algorithms.py`, `tsp_gui.py`, `README.md`), hãy đặt chúng trong cùng một thư mục (ví dụ: `src`).

---

## 3. Chạy chương trình
1. **Khởi động chương trình**:
   - Trong terminal hoặc command prompt, chạy:
     ```bash
     python src/main.py
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
  - Nếu có vấn đề, vui lòng liên hệ qua:
    - Email: khoadangphan307@gmail.com
    - Điện thoại: 0867570650
---

#  File `setup.py` được sử dụng để đóng gói và cài đặt dự án Python. Sau khi cài đặt, bạn có thể chạy ứng dụng trực tiếp từ terminal mà không cần quản lý thủ công các tệp nguồn.

## 1. Cài đặt gói từ `setup.py`

### 1.1. Chuẩn bị môi trường
1. **Yêu cầu hệ thống**:
   - Python phiên bản 3.8 trở lên.
   - Công cụ `pip` để quản lý thư viện Python.

2. **Cài đặt thư viện cần thiết**:
   - Đảm bảo `setuptools` đã được cài đặt (nếu chưa có, chạy lệnh sau):
     ```bash
     pip install setuptools
     ```

---

### 1.2. Cài đặt dự án
1. Mở terminal hoặc command prompt.
2. Di chuyển đến thư mục chứa file `setup.py`:
   ```bash
   cd <thư mục chứa setup.py>
   ```
3. Chạy lệnh sau để cài đặt dự án:
   ```bash
   pip install .
   ```
   - Lệnh này sẽ:
     - Cài đặt các thư viện phụ thuộc được liệt kê trong `setup.py`.
     - Thêm dự án vào môi trường Python của bạn.

---

## 2. Chạy ứng dụng
Sau khi cài đặt thành công, bạn có thể chạy ứng dụng bằng lệnh:

```bash
tsp_solver
```

Nếu entry point không hoạt động, bạn có thể chạy ứng dụng trực tiếp từ tệp mã nguồn:

```bash
python src/main.py
```

---

## 3. Gỡ cài đặt
Để gỡ cài đặt dự án, sử dụng lệnh sau:

```bash
pip uninstall tsp_solver
```

---

## 4. Lỗi phổ biến và cách khắc phục

1. **`ModuleNotFoundError`**:
   - Đảm bảo bạn đã cài đặt dự án đúng cách.
   - Kiểm tra bạn đang sử dụng đúng môi trường Python.

2. **Không thể chạy lệnh `tsp_solver`**:
   - Kiểm tra entry point trong file `setup.py` (mục `entry_points`).
   - Nếu lỗi vẫn xảy ra, hãy chạy ứng dụng trực tiếp bằng lệnh:
     ```bash
     python src/main.py
     ```

---
