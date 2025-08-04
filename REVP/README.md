# 🧬 Rosalind Problem: Locating Restriction Sites (REVP)

This repository contains my solution to the [REVP problem on Rosalind](https://rosalind.info/problems/revp/). The task is to **identify reverse palindromes** (also known as palindromic recognition sites) in a DNA sequence.

---

## 📚 Problem Overview

A **reverse palindrome** is a DNA substring that matches its **reverse complement**. For example, `GCATGC` is a reverse palindrome because its reverse complement is also `GCATGC` :contentReference[oaicite:1]{index=1}.

**Given:** A DNA string (up to 1,000 base pairs) in FASTA format.  
**Return:** For every reverse palindrome of length **between 4 and 12**, output its **starting position** (1-based) and **length**. Order does not matter :contentReference[oaicite:2]{index=2}.
