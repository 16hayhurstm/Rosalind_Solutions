from Bio.Seq import Seq
import pyperclip


def rna2prot_string(file_loc):
    with open(file_loc) as file:
        rna = file.read().strip()
    rna = Seq(rna)
    print(type(rna))
    protein = str(rna.translate(to_stop=True))
    print(protein)
    pyperclip.copy(protein)


rna2prot_string("PROT/rosalind_prot.txt")
