# Longest Increasing Subsequence


def get_the_sequence(file_loc):
    with open(file_loc, "r") as file:
        lines = file.readlines()
    pi = lines[1].split()
    return pi


pi = get_the_sequence("LGIS/trial.txt")


def lisRec(nums, index, prev_index, memo):
    # Base case
    if index == len(nums):
        return []

    # Check memo
    key = (index, prev_index)
    if key in memo:
        return memo[key]

    # Option 1: skip current
    not_take = lisRec(nums, index + 1, prev_index, memo)

    # Option 2: take current if valid
    take = []
    if prev_index == -1 or nums[index] > nums[prev_index]:
        take = [nums[index]] + lisRec(nums, index + 1, index, memo)

    # Choose longer one
    if len(take) > len(not_take):
        memo[key] = take
    else:
        memo[key] = not_take

    return memo[key]


def longestIncreasingSubsequence(nums):
    memo = {}
    return lisRec(nums, 0, -1, memo)


LIS = longestIncreasingSubsequence(pi)
LDS = longestIncreasingSubsequence(pi[::-1])[::-1]
print("LIS:", LIS)
print("LDS:", LDS)
