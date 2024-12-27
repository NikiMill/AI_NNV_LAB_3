#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#С помощью алгоритма поиска в глубину находим минимальное расстояние между начальным и конечным пунктами
import itertools


def dfs(start, end, visited, current_distance, min_distance, distance_matrix):
    """Поиск в глубину для нахождения минимального расстояния."""
    if start == end:
        return min(current_distance, min_distance)

    for next_city in range(len(distance_matrix)):
        if not visited[next_city]:
            visited[next_city] = True
            current_distance += distance_matrix[start][next_city]
            min_distance = dfs(next_city, end, visited, current_distance, min_distance, distance_matrix)
            current_distance -= distance_matrix[start][next_city]
            visited[next_city] = False  # Backtrack

    return min_distance


def find_min_distance_dfs(distance_matrix, start, end):
    """Ищем минимальное расстояние между начальным и конечным пунктами."""
    visited = [False] * len(distance_matrix)
    visited[start] = True
    return dfs(start, end, visited, 0, float('inf'), distance_matrix)


# Пример использования
if __name__ == "__main__":
    # Матрица расстояний между городами для 10 узлов
    distance_matrix = [
        [0, 634, 246, 420, 98, 181, 853, 462, 457, 199],
        [634, 0, 719, 545, 732, 815, 1487, 1096, 983, 833],
        [246, 719, 0, 174, 183, 100, 938, 708, 703, 284],
        [420, 545, 174, 0, 357, 274, 1112, 882, 877, 458],
        [98, 732, 183, 357, 0, 83, 755, 560, 555, 101],
        [181, 815, 100, 274, 83, 0, 838, 643, 638, 184],
        [853, 1487, 938, 1112, 755, 838, 0, 462, 674, 654],
        [462, 1096, 708, 882, 560, 643, 462, 0, 212, 661],
        [457, 983, 703, 877, 555, 638, 674, 212, 0, 656],
        [199, 833, 284, 458, 101, 184, 654, 661, 656, 0],
    ]

    start_city = 0  # Начальный пункт
    end_city = 9  # Конечный пункт

    # Поиск с помощью DFS
    min_distance_dfs = find_min_distance_dfs(distance_matrix, start_city, end_city)


    # Решение задачи коммивояжера
    def calculate_total_distance(route, distance_matrix):
        """Вычисление общей дистанции для данного маршрута."""
        total_distance = 0
        for i in range(len(route) - 1):
            total_distance += distance_matrix[route[i]][route[i + 1]]
        return total_distance

    print(f"Минимальное расстояние с помощью DFS от пункта {start_city} до {end_city}: {min_distance_dfs}")

