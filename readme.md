# Matrix Calculator

A Python matrix calculator that reduces a randomly generated matrix to **Row Echelon Form (REF)** and **Reduced Row Echelon Form (RREF)** using Gaussian and Gauss-Jordan elimination. Implemented in two versions: pure Python (no external libraries) and NumPy.

![python](https://img.shields.io/badge/Python-3.x-yellow)

## Overview

Given a matrix size (rows × columns), the program generates a random matrix and performs elimination to compute:

- **REF (Row Echelon Form)** via Gaussian elimination
- **RREF (Reduced Row Echelon Form)** via Gauss-Jordan elimination
- Pivot normalization, ensuring pivot elements equal 1

## Versions

### 1. `Matrix.py` — Pure Python

Implements matrix operations from scratch, without NumPy:

- `create(row, col)` — generates a random matrix
- `identity()` — builds an identity matrix matching the input shape
- `find_pivot(x)` — locates pivot values along the diagonal
- `multiply(a, b)` — matrix multiplication
- `Gaussian(main)` — computes the elimination matrix for REF
- `Gauss_J(main)` — computes the elimination matrix for RREF
- `normalize_pivot(matrix)` — scales rows so pivots equal 1

### 2. `Matrix_numpy.py` — NumPy version

A more concise implementation using NumPy arrays and vectorized operations:

- `gaussian(matrix)` — row reduction to REF
- `gauss_jordan(matrix)` — row reduction to RREF
- Uses `np.dot`, `np.eye`, and array slicing instead of manual loops

### 3. `nomalized_pivot.py`

A standalone helper function extracted from `Matrix.py`, used to normalize pivot values to 1 by dividing each row by its pivot element.

## Usage

Run either version and enter the number of rows and columns when prompted:

```bash
python Matrix.py
# or
python Matrix_numpy.py
```

Example prompt:

```
Row: 3
Col: 3
```

The program will print the randomly generated matrix, its identity matrix, the REF, and the RREF (all with normalized pivots).

## Requirements

- Python 3.x
- NumPy (only required for `Matrix_numpy.py`)

Install NumPy if needed:

```bash
pip install numpy
```

## Project Structure

```
├── Matrix.py             # Pure Python implementation (Gaussian / Gauss-Jordan elimination)
├── Matrix_numpy.py        # NumPy-based implementation
├── nomalized_pivot.py     # Standalone pivot normalization helper
└── README.md
```

## Notes

- Matrices are randomly generated with integer values between 1–9 for demonstration purposes.
- The pure Python version implements elimination manually to demonstrate the underlying linear algebra, while the NumPy version favors performance and concise code.
