import itertools

distances = {
    ('a', 'b'): 4, ('b', 'a'): 4,
    ('a', 'c'): 1, ('c', 'a'): 1,
    ('a', 'd'): 3, ('d', 'a'): 3,
    ('b', 'c'): 2, ('c', 'b'): 2,
    ('b', 'd'): 3, ('d', 'b'): 3,
    ('c', 'd'): 5, ('d', 'c'): 5,
}

def get_route_cost(route):
    cost = 0
    for i in range(len(route) - 1):
        pair = (route[i], route[i + 1])
        if pair in distances:
            cost += distances[pair]
        else:
            return float('inf')
    return cost

def solve_tsp(start_city, cities):
    other_cities = [c for c in cities if c != start_city]
    best_route = None
    min_cost = float('inf')

    for perm in itertools.permutations(other_cities):
        current_route = [start_city] + list(perm) + [start_city]
        cost = get_route_cost(current_route)

        if cost < min_cost:
            min_cost = cost
            best_route = current_route

    return best_route, min_cost

if __name__ == "__main__":
    all_cities = ['a', 'b', 'c', 'd']
    start = 'a'

    print("\n--- Travelling Salesman Problem ---")
    print(f"Cities: {all_cities}")
    print(f"Start City: '{start}'\n")

    optimal_route, optimal_cost = solve_tsp(start, all_cities)

    print("Optimal Route:", " -> ".join(optimal_route))
    print(f"Optimal Cost: {optimal_cost}\n")
