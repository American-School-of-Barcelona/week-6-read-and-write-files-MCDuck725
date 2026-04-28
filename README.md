[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/d-G81BYE)
# Week 6: File I/O

This week you'll complete 4 problems that work with **files** — reading CSVs, counting lines of code, and even overlaying images. Instead of typing input at the keyboard, your programs will read data from files and write results back out.

## Learning Resources

### Full Lecture (~1.5 hours)
https://cs50.harvard.edu/python/weeks/6/

### Read the Notes
https://cs50.harvard.edu/python/notes/6/

### Short Videos
- **File I/O:** https://cs50.harvard.edu/python/shorts/file_io/
- **CSV Files:** https://cs50.harvard.edu/python/shorts/csv/

### Jump Right In
The problem descriptions will guide you. The data files you need are already in each folder.

---

## Assignment Overview

Complete **ALL** of the following problems from CS50P Week 6:

1. **Lines of Code** — count the real lines in a Python file (skip blanks and comments)
2. **Pizza Py** — read a CSV menu and print it as a formatted table
3. **Scourgify** — clean up messy CSV data and write a new file
4. **CS50 Shirt** — overlay a shirt graphic onto a photo using image compositing

---

## The Big Idea This Week: Files

Up to now, your programs have lived entirely in memory — input comes in, output goes out, and nothing persists. This week your programs will **read from files** and **write to files**, which is how most real software actually works.

```python
with open("data.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["name"])
```

The `with open(...)` pattern handles opening and closing the file safely, even if something goes wrong.

---

## Problem 1: Lines of Code
📁 `lines/lines.py`
🔗 https://cs50.harvard.edu/python/psets/6/lines/

Write a program that counts the **real** lines of code in a Python file — skipping blank lines and comment lines.

**Usage:**
```
python lines.py sample.py
```

A `sample.py` is already in this folder so you can test right away.

**Rules:**
- Accept exactly one command-line argument: the name of a `.py` file
- Exit with error if no argument, too many arguments, or the file doesn't end in `.py`
- Exit with error if the file doesn't exist
- **Don't count:** lines that are blank (only whitespace) or lines that start with `#`
- **Do count:** everything else, including docstrings

**Error handling:**
```
Too few command-line arguments
Too many command-line arguments
Not a Python file
File does not exist
```

**Example:** `sample.py` has 12 lines total — 3 comment lines, 3 blank lines, leaving **6 lines of real code**. Your program should output `6`.

**Hints:**
- `sys.argv` gives you command-line arguments
- `open(filename)` opens a file; loop over it line by line with `for line in f:`
- `.strip()` removes leading/trailing whitespace
- `line.strip().startswith("#")` checks for comments

---

## Problem 2: Pizza Py
📁 `pizza/pizza.py`
🔗 https://cs50.harvard.edu/python/psets/6/pizza/

> 📦 **Run this once in the terminal before you start:** `pip install tabulate`

Read a pizza menu CSV file and print it as a nicely formatted ASCII table.

**The data files are already in this folder:** `sicilian.csv` and `regular.csv`.

**Usage:**
```
python pizza.py sicilian.csv
python pizza.py regular.csv
```

**Rules:**
- Accept exactly one command-line argument: a `.csv` filename
- Exit with error if the file doesn't end in `.csv` or doesn't exist
- Print the table using `tabulate` with the `grid` format

**Expected output for `sicilian.csv`:**
```
+------------------+---------+---------+
| Sicilian Pizza   | Small   | Large   |
+==================+=========+=========+
| Cheese           | $25.50  | $39.95  |
+------------------+---------+---------+
| 1 item           | $27.50  | $41.95  |
+------------------+---------+---------+
...
```

**Hints:**
- `import csv` — use `csv.reader` to read the file row by row
- `from tabulate import tabulate`
- The first row of the CSV is the header — `tabulate(data, headers=first_row, tablefmt="grid")`

---

## Problem 3: Scourgify
📁 `scourgify/scourgify.py`
🔗 https://cs50.harvard.edu/python/psets/6/scourgify/

Read a messy CSV (`before.csv`), clean it up, and write a new clean CSV (`after.csv`).

**`before.csv` is already in this folder.** Take a look at it — the `name` column has names in "Last, First" format all jammed into one field.

**Usage:**
```
python scourgify.py before.csv after.csv
```

**The transformation:**

| before.csv | after.csv |
|---|---|
| `"Potter, Harry",Gryffindor` | `Harry,Potter,Gryffindor` |
| `"Granger, Hermione",Gryffindor` | `Hermione,Granger,Gryffindor` |

**Rules:**
- Accept exactly two arguments: input file, output file
- Exit with error if the wrong number of arguments
- Exit with error if the input file doesn't exist
- Output columns in order: `first`, `last`, `house`

**Hints:**
- `import csv`
- Read with `csv.DictReader` — each row becomes a dictionary with keys `name` and `house`
- Split the name: `last, first = row["name"].split(", ")`
- Write with `csv.DictWriter` — define the fieldnames, call `writer.writeheader()`, then `writer.writerow()`

---

## Problem 4: CS50 Shirt
📁 `shirt/shirt.py`
🔗 https://cs50.harvard.edu/python/psets/6/shirt/

> 📦 **Run this once in the terminal before you start:** `pip install Pillow`

Overlay a CS50 shirt graphic onto a photo using image compositing.

**The files you need are already in this folder:**
- `shirt.png` — the shirt overlay (transparent background, 600×600)
- `before1.jpg`, `before2.jpg`, `before3.jpg` — sample muppet photos to test with

**Usage:**
```
python shirt.py before1.jpg after1.jpg
python shirt.py before2.jpg after2.jpg
```

This creates a new image with the shirt composited on top of the input photo.

**Rules:**
- Accept exactly two arguments: input file, output file
- Input and output must have matching extensions (`.jpg`/`.jpeg` or `.png`)
- Exit with error if the input file doesn't exist, or if extensions don't match or aren't supported

**Hints:**
- `from PIL import Image, ImageOps`
- Open the shirt: `shirt = Image.open("shirt/shirt.png")`
- Resize/crop the input photo to match the shirt dimensions: `ImageOps.fit(photo, shirt.size)`
- Paste the shirt on top using the shirt as its own mask: `photo.paste(shirt, shirt)`
- Save: `photo.save("after1.jpg")`

---

## Testing Your Code

```bash
check50 --local cs50/problems/2024/python/lines
check50 --local cs50/problems/2024/python/pizza
check50 --local cs50/problems/2024/python/scourgify
check50 --local cs50/problems/2024/python/shirt
```

---

## Saving Your Work

After completing each problem:

1. Click the **Source Control** icon (left sidebar)
2. Stage your changes (click the **+** button)
3. Type a commit message (e.g., "Complete scourgify")
4. Click **Commit**
5. Click **Sync Changes**

---

## Submission

When you've completed all four problems, make sure all files are committed and synced.
