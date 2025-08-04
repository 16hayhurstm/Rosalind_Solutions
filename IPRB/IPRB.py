import math
import pyperclip


def extract_values(file_path):
    with open(file_path, "r") as file:
        line = file.read().strip()
        k, m, n = map(int, line.split())
        return k, m, n


k, m, n = extract_values("IPRB/rosalind_iprb.txt")
s = k + m + n

# total number of possible breeding pairs
tot_pairs = math.comb(s, 2)

# number pairs by cross

tot_kk = math.comb(k, 2)
tot_mm = math.comb(m, 2)
tot_nn = math.comb(n, 2)

tot_km = k * m
tot_kn = k * n
tot_mn = m * n

# caluclate percentage of outcomes that result in offspring containign a dominant allel
prob_cont_dom = (
    tot_kk * 1.0
    + tot_km * 1.0
    + tot_kn * 1.0
    + tot_mm * 0.75
    + tot_mn * 0.5
    + tot_nn * 0.0
) / tot_pairs

print(prob_cont_dom)
pyperclip.copy(prob_cont_dom)
