import itertools
import random
import math
import time
import json
import tkinter as tk
from tkinter import messagebox, filedialog, ttk
import numpy as np

class TSPSolver:
    def __init__(self, cities=None):
        self.cities = cities if cities else []
        self.distance_matrix = []
        self.weight_matrix = []
        self.log = []

    def add_city(self, x, y):
        self.cities.append((x, y))

    def generate_random_cities(self, n):
        canvas_width, canvas_height = 1220, 550
        self.cities = [(random.randint(50, canvas_width - 50), random.randint(50, canvas_height - 50)) for _ in range(n)]
        self.calculate_distance_matrix()

    def calculate_distance_matrix(self):
        self.distance_matrix = []
        self.weight_matrix = []
        for i in range(len(self.cities)):
            distances = []
            weights = []
            for j in range(len(self.cities)):
                dist = np.linalg.norm(np.array(self.cities[i]) - np.array(self.cities[j]))
                distances.append(dist)
                weights.append(1 / dist if dist != 0 else 0)  # Example of weight calculation
            self.distance_matrix.append(distances)
            self.weight_matrix.append(weights)

    def nearest_neighbor(self):
        start = 0
        unvisited = set(range(len(self.cities)))
        unvisited.remove(start)
        path = [start]
        total_cost = 0
        start_time = time.time()

        while unvisited:
            last = path[-1]
            nearest = min(unvisited, key=lambda city: self.distance_matrix[last][city])
            total_cost += self.distance_matrix[last][nearest]
            path.append(nearest)
            unvisited.remove(nearest)

        total_cost += self.distance_matrix[path[-1]][path[0]]  # Return to start
        time_taken = time.time() - start_time
        self.log_result("Nearest Neighbor", time_taken, total_cost, len(path), path)
        return path, total_cost

    def log_result(self, algorithm, time_taken, cost, steps, path):
        self.log.append({
            "Thuật toán": algorithm,
            "Thời gian": time_taken,
            "Chi phí": cost,
            "Bước": steps,
            "Đường đi": path
        })

    def save_log_to_file(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.log, file)

    def load_log_from_file(self, filename):
        with open(filename, 'r') as file:
            self.log = json.load(file)

class TSPApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mô phỏng bài toán người du lịch")
        self.solver = TSPSolver()
        self.skip_animation = False

        self.root.geometry("1920x1080")
        self.main_frame = tk.Frame(root, padx=10, pady=10)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.canvas_frame = tk.Frame(self.main_frame)
        self.canvas_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)

        self.canvas = tk.Canvas(self.canvas_frame, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.log_display_frame = tk.Frame(self.canvas_frame)
        self.log_display_frame.pack(fill=tk.X, padx=5, pady=5)

        self.log_tree = ttk.Treeview(self.log_display_frame, columns=("Thuật toán", "Thời gian", "Chi phí", "Bước", "Đường đi"), show="headings")
        self.log_tree.heading("Thuật toán", text="Thuật toán")
        self.log_tree.heading("Thời gian", text="Thời gian")
        self.log_tree.heading("Chi phí", text="Chi phí")
        self.log_tree.heading("Bước", text="Bước")
        self.log_tree.heading("Đường đi", text="Đường đi")
        self.log_tree.pack(fill=tk.BOTH, expand=True)

        self.control_frame = tk.Frame(self.main_frame, padx=10, pady=10)
        self.control_frame.pack(side=tk.LEFT, fill=tk.Y)

        self.city_control_frame = tk.LabelFrame(self.control_frame, text="Quản lý Thành phố", padx=5, pady=5)
        self.city_control_frame.pack(fill=tk.X, padx=5, pady=5)

        tk.Label(self.city_control_frame, text="Số lượng thành phố:").grid(row=0, column=0, sticky="w")
        self.city_count_entry = tk.Entry(self.city_control_frame)
        self.city_count_entry.grid(row=0, column=1, padx=5, pady=5)

        self.generate_button = tk.Button(self.city_control_frame, text="Tạo ngẫu nhiên", command=self.generate_cities)
        self.generate_button.grid(row=1, column=0, columnspan=2, pady=5)

        tk.Label(self.city_control_frame, text="Tọa độ:").grid(row=2, column=0, columnspan=2, sticky="w")
        self.coordinates_text = tk.Text(self.city_control_frame, height=10, width=30)
        self.coordinates_text.grid(row=3, column=0, columnspan=2, pady=5)

        self.add_city_button = tk.Button(self.city_control_frame, text="Thêm Tọa độ", command=self.add_city_from_input)
        self.add_city_button.grid(row=4, column=0, columnspan=2, pady=5)

        self.algorithm_frame = tk.LabelFrame(self.control_frame, text="Thuật toán", padx=5, pady=5)
        self.algorithm_frame.pack(fill=tk.X, padx=5, pady=5)

        self.solve_button = tk.Button(self.algorithm_frame, text="Chạy Nearest Neighbor", command=self.solve)
        self.solve_button.pack(fill=tk.X, padx=5, pady=5)

        self.show_matrix_button = tk.Button(self.algorithm_frame, text="Hiển thị Ma trận", command=self.show_matrices)
        self.show_matrix_button.pack(fill=tk.X, padx=5, pady=5)

        self.animation_button = tk.Button(self.algorithm_frame, text="Bật/Tắt hoạt hình", command=self.toggle_animation)
        self.animation_button.pack(fill=tk.X, padx=5, pady=5)

        self.log_frame = tk.LabelFrame(self.control_frame, text="Quản lý Log", padx=5, pady=5)
        self.log_frame.pack(fill=tk.X, padx=5, pady=5)

        self.save_log_button = tk.Button(self.log_frame, text="Lưu Log", command=self.save_log)
        self.save_log_button.pack(fill=tk.X, padx=5, pady=5)

        self.load_log_button = tk.Button(self.log_frame, text="Tải Log", command=self.load_log)
        self.load_log_button.pack(fill=tk.X, padx=5, pady=5)

        self.refresh_button = tk.Button(self.control_frame, text="Làm mới", command=self.refresh_app)
        self.refresh_button.pack(fill=tk.X, padx=5, pady=5)

    def toggle_animation(self):
        self.skip_animation = not self.skip_animation
        status = "đã tắt" if self.skip_animation else "đã bật"
        messagebox.showinfo("Hoạt hình", f"Hoạt hình hiện tại {status}.")

    def generate_cities(self):
        try:
            n = int(self.city_count_entry.get())
            if n <= 0:
                raise ValueError("Số thành phố phải lớn hơn 0.")
            self.solver.generate_random_cities(n)
            self.draw_cities()
        except ValueError as e:
            messagebox.showerror("Lỗi", str(e))

    def add_city_from_input(self):
        try:
            coordinates = self.coordinates_text.get("1.0", tk.END).strip().split("\n")
            for line in coordinates:
                x, y = map(int, line.split(","))
                self.solver.add_city(x, y)
            self.solver.calculate_distance_matrix()
            self.draw_cities()
        except Exception as e:
            messagebox.showerror("Lỗi", "Tọa độ không hợp lệ.")

    def solve(self):
        if not self.solver.cities:
            messagebox.showwarning("Cảnh báo", "Chưa có dữ liệu thành phố.")
            return
        path, cost = self.solver.nearest_neighbor()
        self.animate_path(path)
        self.update_log_display()
        messagebox.showinfo("Kết quả", f"Đường đi: {path}\nChi phí: {cost}")

    def animate_path(self, path):
        self.canvas.delete("path")
        if self.skip_animation:
            self.draw_path(path)
            return
        for i in range(len(path)):
            x1, y1 = self.solver.cities[path[i]]
            x2, y2 = self.solver.cities[path[(i + 1) % len(path)]]
            self.canvas.create_line(x1, y1, x2, y2, fill="red", tags="path")
            self.root.update()
            time.sleep(0.5)

    def show_matrices(self):
        if not self.solver.distance_matrix:
            messagebox.showwarning("Cảnh báo", "Chưa có dữ liệu thành phố.")
            return

        distance_text = "Ma trận khoảng cách:\n" + "\n".join(["\t".join(map(lambda x: f"{x:.2f}", row)) for row in self.solver.distance_matrix])
        weight_text = "\nMa trận trọng số:\n" + "\n".join(["\t".join(map(lambda x: f"{x:.2f}", row)) for row in self.solver.weight_matrix])
        messagebox.showinfo("Ma trận", distance_text + weight_text)

    def save_log(self):
        filename = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if filename:
            self.solver.save_log_to_file(filename)

    def load_log(self):
        filename = filedialog.askopenfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if filename:
            self.solver.load_log_from_file(filename)
            self.update_log_display()

    def refresh_app(self):
        self.solver = TSPSolver()
        self.canvas.delete("all")
        self.city_count_entry.delete(0, tk.END)
        self.coordinates_text.delete("1.0", tk.END)
        self.log_tree.delete(*self.log_tree.get_children())

    def draw_cities(self):
        self.canvas.delete("all")
        for i, (x, y) in enumerate(self.solver.cities):
            self.canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill="blue")
            self.canvas.create_text(x, y - 10, text=str(i))

    def draw_path(self, path):
        self.canvas.delete("path")
        for i in range(len(path)):
            x1, y1 = self.solver.cities[path[i]]
            x2, y2 = self.solver.cities[path[(i + 1) % len(path)]]
            self.canvas.create_line(x1, y1, x2, y2, fill="red", tags="path")

    def update_log_display(self):
        self.log_tree.delete(*self.log_tree.get_children())
        for entry in self.solver.log:
            self.log_tree.insert("", "end", values=(entry["Thuật toán"], f"{entry['Thời gian']:.2f}s", f"{entry['Chi phí']:.2f}", entry['Bước'], entry['Đường đi']))

if __name__ == "__main__":
    root = tk.Tk()
    app = TSPApp(root)
    root.mainloop()
