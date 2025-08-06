# 🧬 Rosalind Problem: Reconstructing Evolutionary Histories (SORT)

This repository contains my solution to the [SORT problem on Rosalind](https://rosalind.info/problems/sort/), which focuses on finding the shortest sequence of **reversals** to sort one permutation into another — a key concept in comparative genomics.

---

## 📚 Problem Description

A **reversal** of a permutation inverts the order of a contiguous subsequence.  
For example, the reversal that transforms:

✨ Task

**Given:**  
- Two permutations \( \pi \) and \( \gamma \), each of length 10

**Return:**  
- The **reversal distance** \( d_{\text{rev}}(\pi, \gamma) \) — the minimum number of reversals needed to transform \( \pi \) into \( \gamma \)
- A **collection of reversals** (as index pairs) that accomplish this transformation

> If multiple valid reversal paths exist, any one may be returned.