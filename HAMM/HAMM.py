# Counting Point Mutations


def count_point_mutations(file_loc):
    with open(file_loc, "r") as file:
        lines = file.readlines()
    s = lines[0]
    d = lines[1]

    hamming_distance = 0

    # zipping together each letter at each index of the strings and comparing if they are the same
    for x, y in zip(s, d):
        if x != y:
            hamming_distance += 1

    print(hamming_distance)


count_point_mutations("HAMM/rosalind_hamm.txt")
