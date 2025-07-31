# Transcribing DNA into RNA


def dna_to_rna(file_loc):
    with open(file_loc) as file:
        dna_sequence = file.read().strip()

    rna_sequence = ""
    for base in dna_sequence:
        if base == "T":
            rna_sequence += "U"
        else:
            rna_sequence += base

    print(rna_sequence)


dna_to_rna("RNA/rosalind_chal_rna.txt")


# def dna_to_rna(file_loc):
#     with open(file_loc) as file:
#         dna = file.read().strip()
#     print(dna.replace("T", "U"))

# Better solution but mine is still functional
