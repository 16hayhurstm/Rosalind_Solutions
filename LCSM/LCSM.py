from collections import Counter


def LCSM(file_loc):
    with open(file_loc, "r") as file:
        dict = {}
        current_name = ""
        for line in file:
            line = line.strip()
            if line.startswith(">"):
                current_name = line[1:]
                dict[current_name] = ""
            else:
                dict[current_name] += line

    # Make a list of all the squences
    sequences = list(dict.values())

    subs1 = []

    for sequence in sequences:
        subs = []
        for i in range(len(sequence)):
            for j in range(i + 1, len(sequence)):
                subs.append(sequence[i:j])
        if sequence == sequences[0]:
            subs1 = subs
        else:
            subs1 = list(set(subs1) & set(subs))

    answer = max(subs1, key=len)

    print(answer)


LCSM("LCSM/rosalind_lcsm2.txt")
