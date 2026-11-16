"""
ISM2411 Lab 13 — First DataFrame — Retail Sales Explorer
Author: Layton Niemier
Run with: python explore.py   (from the ism2411-lab13 folder)

SELF-ASSESSMENT
1. What does a boolean filter do, in plain English?
   A boolean filter is a thing that asks a yes and no question for every row,
   and then keeps only the rows where the answer is yes.

2. What is the difference between df["revenue"] and df[["revenue"]]?
   df["revenue"] (single brackets) gives back a Series: one column of values.
   df[["revenue"]] (double brackets, a list of names) gives back a DataFrame
   that happens to have one column. It matters when the next step expects a
   table, like saving with to_csv, merging, or adding more columns to the
   list later. Series-only methods like .unique() work on the single-bracket
   version.

3. Why pandas instead of Excel for this task?
   pandas is easier to add rows and columns with sets of data in a single
   script, and since it is all in one script I can rerun it on new data and
   get the same steps every time instead of redoing it by hand.
"""

import os

import pandas as pd

# ---------------------------------------------------------------
# Exercise 1 — Load it
# ---------------------------------------------------------------
print("=== Exercise 1: Load it ===")
df = pd.read_csv("data/retail_sales.csv")
print(df.head())
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print(df.dtypes)
print()

# ---------------------------------------------------------------
# Exercise 2 — Filter by region
# ---------------------------------------------------------------
print("=== Exercise 2: Filter by region ===")
south = df[df["region"] == "South"]
print("South rows:", len(south))
print(south.head())
print()

# ---------------------------------------------------------------
# Exercise 3 — Top 5 by revenue
# (index values are not 0-4 because the index was not reset)
# ---------------------------------------------------------------
print("=== Exercise 3: Top 5 by revenue ===")
top5 = df.sort_values("revenue", ascending=False).head(5)
print(top5)
print()

# ---------------------------------------------------------------
# Exercise 4 — Two-condition filter (& and parentheses required)
# ---------------------------------------------------------------
print("=== Exercise 4: Two-condition filter ===")
big_south = df[(df["region"] == "South") & (df["revenue"] > 1000)]
print("South AND revenue > 1000:", len(big_south))
print(big_south.head())
print()

# ---------------------------------------------------------------
# Exercise 5 — A new column
# ---------------------------------------------------------------
print("=== Exercise 5: A new column ===")
df["per_unit"] = df["revenue"] / df["quantity"]
print(df.head())
print("Mean per-unit price:", df["per_unit"].mean())
print()

# ---------------------------------------------------------------
# Exercise 6 — Unique values
# ---------------------------------------------------------------
print("=== Exercise 6: Unique values ===")
print(df["region"].unique())
print(df["region"].value_counts(dropna=False))
print()

# ---------------------------------------------------------------
# Exercise 7 — Select columns
# ---------------------------------------------------------------
print("=== Exercise 7: Select columns ===")
subset = df[["region", "product", "revenue"]]
print("Subset shape:", subset.shape)
print()

# ---------------------------------------------------------------
# Exercise 8 — Save
# ---------------------------------------------------------------
print("=== Exercise 8: Save ===")
df.to_csv("data/explored.csv", index=False)
print("data/explored.csv exists:", os.path.exists("data/explored.csv"))
