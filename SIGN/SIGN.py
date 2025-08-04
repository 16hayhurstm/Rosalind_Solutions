import itertools


def signed_permutations(n):
    nums = list(range(1, n + 1))
    permutations = list(itertools.permutations(nums))
    signs = list(itertools.product([-1, 1], repeat=n))

    result = []
    for perm in permutations:
        for sign_combo in signs:
            signed = [a * b for a, b in zip(perm, sign_combo)]
            result.append(signed)
    return result


def write_signed_permutations_to_file(n, filename):
    signed_perms = signed_permutations(n)
    with open(filename, "w") as f:
        f.write(f"{len(signed_perms)}\n")
        for perm in signed_perms:
            f.write(" ".join(map(str, perm)) + "\n")


n = 4
write_signed_permutations_to_file(n, "signed_permutations_output.txt")
