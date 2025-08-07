# Open and read the file
with open("IEV/rosalind_iev.txt", "r") as file:
    content = file.read().strip()

# Split the content into a list of integers
numbers = list(map(int, content.split()))

# Proportion of cross' offspiring displaying dominant phenotype as a list
proportions = [1, 1, 1, 0.75, 0.5, 0]

Answer = sum([proportions[i] * numbers[i] * 2 for i in range(len(numbers))])

print(Answer)
