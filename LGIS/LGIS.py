# Longest Increasing Subsequence


def get_the_sequence(file_loc):
    # Read the second line from file and split into list
    with open(file_loc, "r") as file:
        lines = file.readlines()
    pi = lines[1].split()
    return pi


# Get input sequence from file
pi = get_the_sequence("LGIS/rosalind_lgis.txt")


def LIS(sequences):

    # Initialize tuples: one per element, holding just itself
    tups = [(int(c),) for c in pi]

    # Build LIS for each position from right to left
    for i_index in reversed(range(len(pi))):
        best = ()  # Track best following subsequence

        # Check all elements to the right
        for j in range(i_index + 1, len(pi)):
            # Compare values: build LIS if increasing
            if int(pi[j]) > int(pi[i_index]):
                # Choose longer sequence if multiple options
                if len(tups[j]) > len(best):
                    best = tups[j]

        # Prepend current value to best subsequence found
        tups[i_index] = (int(pi[i_index]),) + best

    # Get the longest sequence found overall
    answer = sorted(tups, key=len)[-1]

    # Print as space-separated string
    print("LIS;" + " ".join(map(str, answer)))


def LDS(sequences):

    # Initialize tuples: one per element, holding just itself
    tups = [(int(c),) for c in pi]

    # Build LDS for each position from right to left
    for i_index in reversed(range(len(pi))):
        best = ()  # Track best following subsequence

        # Check all elements to the right
        for j in range(i_index + 1, len(pi)):
            # Compare values
            if int(pi[j]) < int(pi[i_index]):
                # Choose longer sequence if multiple options
                if len(tups[j]) > len(best):
                    best = tups[j]

        # Prepend current value to best subsequence found
        tups[i_index] = (int(pi[i_index]),) + best

    # Get the longest sequence found overall
    answer = sorted(tups, key=len)[-1]

    # Print as space-separated string
    print("LDS;" + " ".join(map(str, answer)))


# Print answers
LIS(pi)
LDS(pi)
