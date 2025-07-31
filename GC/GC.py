# Computing GC Content
from collections import Counter


def computing_GC_content(file_loc):
    # Read FASTA file into a dictionary; ID:Sequence
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

        GC_content_list = []

        # Calculate GC content for each sequence
        for sequence in sequences:
            counts = Counter(sequence)
            GC_count = counts["C"] + counts["G"]
            base_count = len(sequence)
            GC_content = GC_count / base_count * 100
            GC_content_list.append(GC_content)

        # Find max GC content
        max_GC = max(GC_content_list)

        # Find sequence with the highest GC content
        index = GC_content_list.index(max_GC)
        desired_sequence = sequences[index]

        # FInd ID of that sequence
        id = [id for id, val in dict.items() if val == desired_sequence]

        # Print ID and GC content
        print(id)
        print(max_GC)


computing_GC_content("GC/rosalind_gc.txt")
