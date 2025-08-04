from itertools import product


def org_perm(file_loc):
    with open(file_loc, "r") as file:
        lines = file.readlines()

    alpha = lines[0].strip()
    alpha = " ".join(alpha).split()
    sorted_alpha = sorted(alpha)
    result = "".join(sorted_alpha)

    n = int(lines[1])

    order = {ch: i for i, ch in enumerate(result)}

    raw_strings = product(result, repeat=n)
    all_strings = ["".join(p) for p in raw_strings]

    sorted_strings = sorted(all_strings, key=lambda s: [order[ch] for ch in s])

    for s in sorted_strings:
        print(s)


org_perm("LEXF/rosalind_lexf.txt")
