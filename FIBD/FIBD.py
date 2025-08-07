def FIBD(n, m):
    # Array to track rabbit pairs of each age
    # Index 0: newborns, Index 1: 1 month old, ..., Index m-1: rabbits about to die
    ages = [1] + [0] * (m - 1)

    # Simulate each month
    for month in range(1, n):
        # Rabbits that are mature (1 month or older) reproduce
        newborns = sum(ages[1:])

        # Age the rabbits: shift right, oldest die, newborns at index 0
        ages = [newborns] + ages[:-1]

    # Total number of rabbit pairs alive
    print(sum(ages))


FIBD(99, 17)
