import time
from queue import PriorityQueue


def BreadthFirstSearch(map, start, finish, aster):
    times = time.time()
    # Починаємо розміщення вершини графа в кінці черги тобто корабля
    queue = [start]
    parents = {start: None}
    Time_func(times)
    # Продовжуємо виконувати кроки 2 і 3 поки очередь не стане пустою.
    while len(queue) != 0:
        # 2 Взяли передній елемент черги і додали як відвідану.
        present_node = queue.pop(0)
        # уникаємо метеорити
        for i in range(len(aster)):
            if present_node == aster[i]:
                continue
        # якщо знайшли ворога то відображаємо шлях
        if present_node == finish:
            return get_line(parents, finish)
        # 3 Створюємо список суміжних вузлів цієї вершини parents.
        for node in map[present_node]:
            if node not in parents:
                parents[node] = present_node
                # 3 Додаємо ті яких немає в списку відвіданих, в кінець черги.
                queue.append(node)

def DepthFirstSearch(map, start, finish, aster):
    times = time.time()
    visited_nodes = []
    path = []
    # Починаємо розміщення вершины графа на вершині стека.
    List = PriorityQueue()
    # 2 Беремо верхній елемент в ньому і додаємо в список відвіданих.
    List.put((0, start, path, visited_nodes))
    Time_func(times)
    while not List.empty():
        depth, present_node, path, visited_nodes = List.get()
        # уникаємо метеорити
        for i in range(len(aster)):

            if present_node == aster[i]:
                continue
        if present_node == finish:
            return path + [present_node]

        visited_nodes = visited_nodes + [present_node]
        # 3 Створюємо список суміжних вершин для цієї вершини(для кожної вершини в списку відвіданих).
        for node in map[present_node]:
            if node not in visited_nodes:
                if node == finish:
                    return path + [node]
                nodeDepth = len(path)
                # 3 Додаємо ті, яких немає в списку відвіданих, в початок стеку.
                List.put((-nodeDepth, node, path + [node], visited_nodes))
    return path


def UniformCostSearch(map, start, finish):
    times = time.time()
    queue = [start]
    parents = {start: None}
    Time_func(times)
    while len(queue) != 0:
        present_node = queue.pop(0)
        if present_node == finish:

            return get_line(parents, finish)

        neighbors = map[present_node]

        for node in neighbors:
            if node not in parents:
                parents[node] = present_node
                queue.append(node)


def Time_func(startTime):
    result = time.time() - startTime
    if result != 0.0:
        print(result)














def get_line(parents, finish_nodes):
    arr = []
    current = finish_nodes
    while current != None:
        arr.insert(0, current)
        current = parents[current]

    return arr
