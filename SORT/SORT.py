from collections import deque


def bfs_reversal_distance(start, target, max_states=5_000_000):
    """
    Accurate reversal distance using BFS.
    Returns (distance, list of reversal steps (i, j)).
    """
    visited = set()
    queue = deque([(start, 0)])
    visited.add(tuple(start))

    parent_map = {tuple(start): (None, None)}

    while queue:
        curr, dist = queue.popleft()

        if curr == target:
            # Reconstruct the path
            path = []
            node = tuple(curr)
            while parent_map[node][0] is not None:
                _, reversal = parent_map[node]
                path.append(reversal)
                node = parent_map[node][0]
            path.reverse()
            return dist, path

        for i in range(len(curr)):
            for j in range(i + 1, len(curr)):
                new_perm = curr[:i] + curr[i : j + 1][::-1] + curr[j + 1 :]
                t_new = tuple(new_perm)
                if t_new not in visited:
                    visited.add(t_new)
                    queue.append((new_perm, dist + 1))
                    parent_map[t_new] = (tuple(curr), (i, j))

                    if len(visited) > max_states:
                        print("⚠️ Too many states explored. Aborting.")
                        return -1, []

    return -1, []

def parse_input_file(filepath):
    """
    Reads exactly 2 lines: start and target permutation.
    """
    with open(filepath) as f:
        lines = list(filter(None, (line.strip() for line in f)))
    if len(lines) != 2:
        raise ValueError("Input file must contain exactly two non-empty lines.")
    start = list(map(int, lines[0].split()))
    target = list(map(int, lines[1].split()))
    return start, target

def main():
    input_file = "SORT/rosalind_sort.txt"  # <-- Update path if needed
    start, target = parse_input_file(input_file)

    dist, steps = bfs_reversal_distance(start, target, max_states=5_000_000)

    if dist == -1:
        print("❌ Reversal distance could not be computed (too many states).")
    else:
        print(f"✅ Reversal distance: {dist}")
        print("🔁 Reversal steps (1-based indices):")
        for i, j in steps:
            print(f"  - Reverse from index {i+1} to {j+1}")

if __name__ == "__main__":
    main()
