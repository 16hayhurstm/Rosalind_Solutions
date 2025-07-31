from collections import Counter


def count_nucleotides(file_loc):
    with open(file_loc) as file:
        dna_sequence = file.read().strip()
    counts = Counter(dna_sequence)
    print(counts["A"], counts["C"], counts["G"], counts["T"])


count_nucleotides("DNA/rosalind_chal_dna.txt")
