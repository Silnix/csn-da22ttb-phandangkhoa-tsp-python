import tkinter as tk
from tkinter import messagebox, filedialog, ttk
from tsp_algorithms import TSPSolver
import time

class TSPApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mô phỏng bài toán người du lịch")
        self.root.geometry("1600x900") # Điều chỉnh kích thước
        self.solver = TSPSolver()
        self.skip_animation = False

        # Khởi tạo giao diện
        self.main_frame = tk.Frame(root, padx=10, pady=10)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Phần Trên
        self.top_frame = tk.Frame(self.main_frame)
        self.top_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Phần Trái
        self.left_panel = tk.Frame(self.top_frame, width=300)
        self.left_panel.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

        # Phần Phải (Canvas + Log)
        self.right_panel = tk.Frame(self.top_frame)
        self.right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Canvas
        self.canvas = tk.Canvas(self.right_panel, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Khu vực Log Dưới
        self.log_tree = ttk.Treeview(self.right_panel, columns=("Thuật toán", "Thời gian", "Chi phí", "Bước", "Đường đi"), show="headings", height=10)
        self.log_tree.heading("Thuật toán", text="Thuật toán")
        self.log_tree.heading("Thời gian", text="Thời gian")
        self.log_tree.heading("Chi phí", text="Chi phí")
        self.log_tree.heading("Bước", text="Bước")
        self.log_tree.heading("Đường đi", text="Đường đi")
        self.log_tree.pack(fill=tk.X, pady=5)

        # Khu vực Thành phố
        self.city_frame = tk.LabelFrame(self.left_panel, text="Thành phố", padx=10, pady=10)
        self.city_frame.pack(fill=tk.X, padx=5, pady=5)

        self.city_count_label = tk.Label(self.city_frame, text="Số lượng thành phố:")
        self.city_count_label.grid(row=0, column=0, sticky="w")

        self.city_count_entry = tk.Entry(self.city_frame)
        self.city_count_entry.grid(row=0, column=1, padx=5, pady=5)

        self.generate_button = tk.Button(self.city_frame, text="Tạo", command=self.generate_cities)
        self.generate_button.grid(row=1, column=0, columnspan=2, pady=5)

        self.coordinates_label = tk.Label(self.city_frame, text="Tọa độ:")
        self.coordinates_label.grid(row=2, column=0, columnspan=2)

        self.coordinates_text = tk.Text(self.city_frame, height=10, width=25)
        self.coordinates_text.grid(row=3, column=0, columnspan=2, pady=5)

        self.generate_matrix_button = tk.Button(self.city_frame, text="Tạo ma trận", command=self.generate_distance_matrix)
        self.generate_matrix_button.grid(row=4, column=0, columnspan=2, pady=5)

        # Khu vực Thuật toán
        self.algorithm_frame = tk.LabelFrame(self.left_panel, text="Thuật toán", padx=10, pady=10)
        self.algorithm_frame.pack(fill=tk.X, padx=5, pady=5)

        self.algorithm_var = tk.StringVar(value="Brute Force")
        self.algorithms = {
            "Brute Force": "Thử tất cả các hoán vị để tìm đường ngắn nhất.",
            "Nearest Neighbor": "Chọn thành phố chưa thăm gần nhất lần lượt.",
            "2-opt": "Tối ưu hóa một đường ban đầu bằng cách đảo ngược các đoạn.",
            "Backtracking": "Khám phá tất cả các đường đi đệ quy với cắt tỉa."
        }
        
        for algo, desc in self.algorithms.items():
            tk.Radiobutton(self.algorithm_frame, text=algo, variable=self.algorithm_var, value=algo, 
                           command=lambda desc=desc: self.show_algorithm_description(desc)).pack(anchor="w")

        self.algorithm_description = tk.Label(self.algorithm_frame, text="", wraplength=250, justify="left")
        self.algorithm_description.pack(pady=5)

        # Khu vực Điều khiển
        self.control_frame = tk.LabelFrame(self.left_panel, text="Điều khiển", padx=10, pady=10)
        self.control_frame.pack(fill=tk.X, padx=5, pady=5)

        self.solve_button = tk.Button(self.control_frame, text="Mô phỏng", command=self.solve)
        self.solve_button.grid(row=0, column=0, columnspan=2, pady=5, sticky="ew")

        self.save_button = tk.Button(self.control_frame, text="Lưu kết quả", command=self.save_results)
        self.save_button.grid(row=1, column=0, pady=5, sticky="ew")

        self.load_button = tk.Button(self.control_frame, text="Tải thành phố", command=self.load_cities)
        self.load_button.grid(row=1, column=1, pady=5, sticky="ew")

        self.save_log_button = tk.Button(self.control_frame, text="Lưu Log", command=self.save_log)
        self.save_log_button.grid(row=2, column=0, pady=5, sticky="ew")

        self.load_log_button = tk.Button(self.control_frame, text="Tải Log", command=self.load_log)
        self.load_log_button.grid(row=2, column=1, pady=5, sticky="ew")

        self.clearlog_button = tk.Button(self.control_frame, text="Xóa log", command=self.clear_log)
        self.clearlog_button.grid(row=3, column=0, pady=5, sticky="ew")

        self.refresh_button = tk.Button(self.control_frame, text="Làm mới", command=self.refresh_app)
        self.refresh_button.grid(row=3, column=1, pady=5, sticky="ew")

        self.show_plot_button = tk.Button(self.control_frame, text="Xóa đường đi", command=self.show_plot)
        self.show_plot_button.grid(row=4, column=0, pady=5, sticky="ew")

        self.skip_animation_button = tk.Button(self.control_frame, text="Bật/Tắt hoạt hình mô phỏng", command=self.toggle_animation)
        self.skip_animation_button.grid(row=4, column=1, pady=5, sticky="ew")

    def toggle_animation(self):
        self.skip_animation = not self.skip_animation
        status = "đã tắt" if self.skip_animation else "đã bật"
        messagebox.showinfo("Hoạt hình", f"Hoạt hình hiện tại {status}.")

    def show_algorithm_description(self, desc):
        self.algorithm_description.config(text=desc)

    def generate_cities(self):
        try:
            n = int(self.city_count_entry.get())
            self.solver.generate_random_cities(n)
            self.coordinates_text.delete(1.0, tk.END)
            for x, y in self.solver.cities:
                self.coordinates_text.insert(tk.END, f"{x},{y}\n")
        except ValueError:
            messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ.")

    def generate_distance_matrix(self):
        try:
            self.solver.cities = []
            for line in self.coordinates_text.get(1.0, tk.END).strip().split("\n"):
                x, y = map(int, line.split(","))
                if 0 <= x <= 1200 and 0 <= y <= 600:
                    self.solver.add_city(x, y)
                else:
                    raise ValueError(f"Tọa độ thành phố ({x}, {y}) vượt quá giới hạn khu vực tọa độ mô phỏng được.")
            self.solver.calculate_distance_matrix()
            self.plot_cities()
            messagebox.showinfo("Thành công", "Ma trận khoảng cách đã được tạo và thành phố đã được mô phỏng thành công.")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Dữ liệu không hợp lệ: {e}")

    def plot_cities(self):
        self.canvas.delete("all")
        radius = 5
        for i, city in enumerate(self.solver.cities):
            x, y = city
            self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill="blue")
            self.canvas.create_text(x + 10, y, text=str(i), anchor="w")

    def solve(self):
        algorithm = self.algorithm_var.get()
        if not self.solver.cities:
            messagebox.showerror("Lỗi", "Không có thành phố để mô phỏng.")
            return

        start_time = time.time()

        if algorithm == "Brute Force":
            path, cost = self.solver.brute_force()
        elif algorithm == "Nearest Neighbor":
            path, cost = self.solver.nearest_neighbor()
        elif algorithm == "2-opt":
            path, cost = self.solver.two_opt()
        elif algorithm == "Backtracking":
            path, cost = self.solver.backtracking()
        else:
            messagebox.showerror("Lỗi", "Thuật toán không hợp lệ.")
            return

        elapsed_time = time.time() - start_time
        self.log_tree.insert("", "end", values=(algorithm, f"{elapsed_time:.2f}", cost, len(path), path))

        if self.skip_animation:
            self.plot_path(path)
        else:
            self.animate_path(path)

        messagebox.showinfo("Kết quả", f"Chi phí: {cost}\nThời gian: {elapsed_time:.2f} giây")

    def plot_path(self, path):
        self.canvas.delete("all")
        radius = 5
        for i, city in enumerate(self.solver.cities):
            x, y = city
            self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill="blue")
            self.canvas.create_text(x + 10, y, text=str(i), anchor="w")

        for i in range(len(path)):
            x1, y1 = self.solver.cities[path[i]]
            x2, y2 = self.solver.cities[path[(i + 1) % len(path)]]
            self.canvas.create_line(x1, y1, x2, y2, fill="red", width=2)

    def animate_path(self, path):
        self.canvas.delete("all")
        radius = 5
        for i, city in enumerate(self.solver.cities):
            x, y = city
            self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill="blue")
            self.canvas.create_text(x + 10, y, text=str(i), anchor="w")

        for i in range(len(path)):
            x1, y1 = self.solver.cities[path[i]]
            x2, y2 = self.solver.cities[path[(i + 1) % len(path)]]
            self.canvas.create_line(x1, y1, x2, y2, fill="red", width=2)
            self.canvas.update()
            time.sleep(0.3)

    def show_plot(self):
        self.canvas.delete("all")
        radius = 5
        for i, city in enumerate(self.solver.cities):
            x, y = city
            self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill="blue")
            self.canvas.create_text(x + 10, y, text=str(i), anchor="w")

    def save_results(self):
        filename = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("Tệp JSON", "*.json")])
        if filename:
            self.solver.save_to_file(filename)
            messagebox.showinfo("Thành công", "Kết quả đã được lưu.")

    def load_cities(self):
        filename = filedialog.askopenfilename(filetypes=[("Tệp JSON", "*.json")])
        if filename:
            self.solver.load_from_file(filename)
            self.coordinates_text.delete(1.0, tk.END)
            for x, y in self.solver.cities:
                self.coordinates_text.insert(tk.END, f"{x},{y}\n")
            messagebox.showinfo("Thành công", "Thành phố đã được tải.")

    def save_log(self):
        filename = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("Tệp JSON", "*.json")])
        if filename:
            self.solver.save_log_to_file(filename)
            messagebox.showinfo("Thành công", "Log đã được lưu.")

    def load_log(self):
        filename = filedialog.askopenfilename(filetypes=[("Tệp JSON", "*.json")])
        if filename:
            self.solver.load_log_from_file(filename)
            self.log_tree.delete(*self.log_tree.get_children())
            for entry in self.solver.log:
                self.log_tree.insert("", "end", values=(entry["Thuật toán"], f"{entry['Thời gian']:.2f}", entry["Chi phí"], entry["Bước"], entry["Đường đi"]))
            messagebox.showinfo("Thành công", "Log đã được tải.")

    def refresh_app(self):
        self.solver = TSPSolver()
        self.city_count_entry.delete(0, tk.END)
        self.coordinates_text.delete(1.0, tk.END)
        self.canvas.delete("all")
        messagebox.showinfo("Thành công", "Đã làm mới thành công.")
    
    def clear_log(self):
        self.log_tree.delete(*self.log_tree.get_children())
        messagebox.showinfo("Thông báo", "Log đã được xóa.")
