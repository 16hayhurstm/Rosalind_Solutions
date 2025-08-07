# 🐇 Rosalind Problem: Wabbit Season (FIBD)

This repository contains my solution to the [WABBIT problem on Rosalind](https://rosalind.info/problems/fibd/), which is a variation of the classical Fibonacci problem involving mortal rabbits.

---

## 📚 Problem Description

This problem builds on the recurrence relation from the classical Fibonacci model:

> In the classic model, rabbits mature after one month and produce a new pair every month afterward. They never die.

In this **mortal rabbits** version:

- Rabbits live for **exactly _m_ months**.
- They **reproduce** starting from their **second month** of life.
- After reaching _m_ months of age, they **die**.

---

## 🧩 Task

**Given:**
- Two positive integers:
  - `n` (months to simulate, where \(1 \leq n \leq 100\))
  - `m` (lifespan in months, where \(1 \leq m \leq 20\))

**Return:**
- The total number of rabbit pairs alive after the `n`-th month.

---
