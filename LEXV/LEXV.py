from itertools import product
import pyperclip


def LEXV(file_loc):
    # Reading in data and setting variables in correct data type
    with open(file_loc, "r") as file:
        lines = file.readlines()

    alpha = lines[0].strip()
    alpha = " ".join(alpha).split()
    result = "".join(alpha)

    n = int(lines[1])

    # Making custom dictionary based of input
    order = {ch: i for i, ch in enumerate(result)}
    print(order)
    # creating tupple of all combinations
    tups = []
    for i in range(1, n + 1):
        raw_strings = product(result, repeat=i)
        tups += raw_strings

    # Converting tupples into lists
    all_strings = ["".join(p) for p in tups]

    # Sorting into lexigraphical order
    sorted_strings = sorted(all_strings, key=lambda s: [order[ch] for ch in s])

    # Print each string
    with open("output.txt", "w") as out_file:
        for s in sorted_strings:
            print(s)
            print(s, file=out_file)


LEXT("LEXT/rosalind_lexv.txt")
