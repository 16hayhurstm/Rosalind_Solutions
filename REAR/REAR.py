import pyperclip
from collections import deque


def bfs_reversal_distance(start, target, max_states=1000000):
    """
    Accurate reversal distance using BFS.
    Returns -1 if max_states is exceeded.
    """
    visited = set()
    queue = deque([(start, 0)])
    visited.add(tuple(start))

    while queue:
        curr, dist = queue.popleft()

        if curr == target:
            return dist

        for i in range(len(curr)):
            for j in range(i + 1, len(curr)):
                new_perm = curr[:i] + curr[i : j + 1][::-1] + curr[j + 1 :]
                t_new = tuple(new_perm)
                if t_new not in visited:
                    visited.add(t_new)
                    queue.append((new_perm, dist + 1))
                    if len(visited) > max_states:
                        return -1  # Too many states
    return -1  # Should not happen


def greedy_reversal_distance(start, target):
    """
    Approximate reversal distance using a greedy approach.
    """
    perm = start[:]
    count = 0
    for i in range(len(perm)):
        if perm[i] != target[i]:
            j = perm.index(target[i])
            perm[i : j + 1] = perm[i : j + 1][::-1]
            count += 1
    return count


def parse_input_file(filepath):
    """
    Reads and parses permutation pairs from file.
    """
    with open(filepath) as f:
        lines = [line.strip() for line in f if line.strip()]
    perms = [list(map(int, line.split())) for line in lines]
    return [(perms[i], perms[i + 1]) for i in range(0, len(perms), 2)]


def log_fallback(start, target, bfs_result, greedy_result):
    """
    Logs fallback case to a file for review.
    """
    with open("fallback_log.txt", "a") as f:
        f.write("Fallback case:\n")
        f.write(f"Start:  {start}\n")
        f.write(f"Target: {target}\n")
        f.write(f"BFS failed (returned -1), Greedy result: {greedy_result}\n")
        f.write("-" * 40 + "\n")


def main():
    input_file = (
        "REAR/rosalind_rear.txt"  # Change if your input file has a different name
    )
    pairs = parse_input_file(input_file)

    results = []
    compare_results = True  # Set to False if you don't want to compare BFS vs Greedy

    for start, target in pairs:
        bfs_dist = bfs_reversal_distance(start, target, max_states=5_000_000)

        if bfs_dist == -1:
            greedy_dist = greedy_reversal_distance(start, target)
            log_fallback(start, target, bfs_dist, greedy_dist)
            print(f"⚠️  Falling back to greedy for pair:\n   {start}\n   {target}")
            results.append(str(greedy_dist))
        else:
            if compare_results:
                greedy_dist = greedy_reversal_distance(start, target)
                if bfs_dist != greedy_dist:
                    print(
                        f"ℹ️  Difference detected: BFS={bfs_dist}, Greedy={greedy_dist}"
                    )
            results.append(str(bfs_dist))

    output_text = "\n".join(results)
    print(output_text)
    pyperclip.copy(output_text)
    print("\n✅ Output copied to clipboard!")
    print("📄 Fallback cases saved to fallback_log.txt (if any).\n")


if __name__ == "__main__":
    main()
