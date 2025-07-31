# Complementing a Strand of DNA


def rev_comp_strand(file_loc):
    with open(file_loc) as file:
        dna_sequence = file.read().strip()

        # Create complement using a mapping dictionary
        complement = {"A": "T", "T": "A", "C": "G", "G": "C"}
        # Reverse the sequence and apply the complement
        reverse_complement = "".join(
            complement[base] for base in reversed(dna_sequence)
        )
        print(reverse_complement)


rev_comp_strand("REVC/rosalind_chal_revc.txt")
