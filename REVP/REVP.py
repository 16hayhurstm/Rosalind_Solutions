from Bio import SeqIO

# read in sequence from FASTA file format
seq = str(next(SeqIO.parse("REVP/rosalind_revp.txt", "fasta")).seq)

# Make base compliment dictionary
complement = {"A": "T", "T": "A", "C": "G", "G": "C"}

for i in range(len(seq)):
    for length in range(4, 13):  # from 4 to 12 inclusive
        if i + length <= len(seq):
            substr = seq[i : i + length]
            rev_comp = "".join(complement[c] for c in substr[::-1])
            if substr == rev_comp:
                print(i + 1, length)
