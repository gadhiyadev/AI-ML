def tower_of_hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return

    tower_of_hanoi(n - 1, source, auxiliary, target)

    print(f"Move disk {n} from {source} to {target}")

    tower_of_hanoi(n - 1, auxiliary, target, source)

def solve_tower_of_hanoi(n):
    print(f"\n--- Tower of Hanoi with {n} disks ---\n")
    tower_of_hanoi(n, 'A', 'C', 'B')
    print(f"\nTotal moves: {2**n - 1}\n")

if __name__ == "__main__":
    n_disks = 3
    solve_tower_of_hanoi(n_disks)
