import itertools
import math
import time
import json
import numpy as np

class TSPSolver:
    def __init__(self, cities=None):
        self.cities = cities if cities else []
        self.distance_matrix = []
        self.log = []

    def add_city(self, x, y):
        self.cities.append((x, y))

    def generate_random_cities(self, n):
        canvas_width, canvas_height = 1200, 600
        self.cities = [(np.random.randint(50, canvas_width - 50), np.random.randint(50, canvas_height - 50)) for _ in range(n)]
        self.calculate_distance_matrix()

    def calculate_distance_matrix(self):
        self.distance_matrix = []
        for i in range(len(self.cities)):
            distances = []
            for j in range(len(self.cities)):
                dist = np.linalg.norm(np.array(self.cities[i]) - np.array(self.cities[j]))
                distances.append(dist)
            self.distance_matrix.append(distances)

    def log_result(self, algorithm, time_taken, cost, steps, path):
        self.log.append({
            "Thuật toán": algorithm,
            "Thời gian": time_taken,
            "Chi phí": cost,
            "Bước": steps,
            "Đường đi": path
        })

    def brute_force(self):
        min_cost = float('inf')
        best_path = None
        start_time = time.time()
        for perm in itertools.permutations(range(len(self.cities))):
            cost = sum(self.distance_matrix[perm[i]][perm[i + 1]] for i in range(len(perm) - 1))
            cost += self.distance_matrix[perm[-1]][perm[0]]
            if cost < min_cost:
                min_cost = cost
                best_path = perm
        time_taken = time.time() - start_time
        self.log_result("Brute Force", time_taken, min_cost, len(list(itertools.permutations(range(len(self.cities))))), best_path)
        return best_path, min_cost

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

        total_cost += self.distance_matrix[path[-1]][path[0]]
        time_taken = time.time() - start_time
        self.log_result("Nearest Neighbor", time_taken, total_cost, len(path), path)
        return path, total_cost

    def two_opt(self, max_iterations=100):
        def calculate_cost(route):
            return sum(self.distance_matrix[route[i]][route[i + 1]] for i in range(len(route) - 1)) + \
                self.distance_matrix[route[-1]][route[0]]

        route = list(range(len(self.cities)))
        best_cost = calculate_cost(route)
        start_time = time.time()

        for _ in range(max_iterations):
            improved = False
            for i in range(1, len(route) - 1):
                for j in range(i + 1, len(route)):
                    new_route = route[:i] + route[i:j][::-1] + route[j:]
                    new_cost = calculate_cost(new_route)
                    if new_cost < best_cost:
                        route, best_cost = new_route, new_cost
                        improved = True
                        break
                if improved:
                    break
            if not improved:
                break

        time_taken = time.time() - start_time
        self.log_result("2-opt", time_taken, best_cost, max_iterations, route)
        return route, best_cost

    def backtracking(self):
        def backtrack(current_city, visited, current_cost):
            nonlocal min_cost, best_path
            if len(visited) == len(self.cities):
                total_cost = current_cost + self.distance_matrix[current_city][visited[0]]
                if total_cost < min_cost:
                    min_cost = total_cost
                    best_path = visited[:]
                return

            for next_city in range(len(self.cities)):
                if next_city not in visited:
                    visited.append(next_city)
                    backtrack(next_city, visited, current_cost + self.distance_matrix[current_city][next_city])
                    visited.pop()

        min_cost = float('inf')
        best_path = None
        start_time = time.time()
        backtrack(0, [0], 0)
        time_taken = time.time() - start_time
        self.log_result("Backtracking", time_taken, min_cost, len(self.cities), best_path)
        return best_path, min_cost

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            json.dump({"cities": self.cities, "distance_matrix": self.distance_matrix, "log": self.log}, file)

    def load_from_file(self, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
            self.cities = data["cities"]
            self.distance_matrix = data["distance_matrix"]
            self.log = data.get("log", [])

    def save_log_to_file(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.log, file)

    def load_log_from_file(self, filename):
        with open(filename, 'r') as file:
            self.log = json.load(file)
