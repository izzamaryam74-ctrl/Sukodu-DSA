# 🧩 Sudoku Solver System (DSA-Based Project)

## 📌 Project Overview
Solving Sudoku puzzles efficiently is a common challenge in **programming** and **Artificial Intelligence** applications.  
Manual solving becomes difficult when users need to **validate moves**, **track board states**, and **store progress**.

This project implements an **Advanced Sudoku Solver System** using **Data Structures and Algorithms (DSA)**.  
Instead of relying only on a simple **2D array**, the system integrates:

- **Linked Lists**
- **Binary Search Trees (BST)**
- **Hash Tables**

to achieve **efficient searching, validation, history tracking, and persistence**.

---

## 🎯 Problem Statement
Users often face difficulties in:

- ❌ Manually solving Sudoku puzzles  
- ❌ Checking whether a number placement is valid  
- ❌ Tracking the order of inputs  
- ❌ Saving and loading puzzle progress  

A simple **2D array** is insufficient for advanced operations like fast validation, ordered history, and persistence.

---

## ✅ Project Goals
The goal of this project is to design and implement a **Sudoku Solver System** that allows users to:

### 🔹 A. Add / Input Puzzle
- Input Sudoku manually  
- Load Sudoku from a **CSV file**
- Use attributes: **(Row, Column, Number)**

### 🔹 B. Solve / Compute
- Solve Sudoku using the **Backtracking Algorithm**

### 🔹 C. Validate
- Check whether a number can be placed at a specific cell safely

### 🔹 D. Display
Display the board in multiple formats:
- **Sequential entry order** (user input order)
- **Solved Sudoku board**

### 🔹 E. Persist
- Save and load board state using **file handling**
- Resume the puzzle later

---

## 🏗️ Chosen Data Structures & Justification
To demonstrate strong understanding of **DSA concepts**, the same Sudoku data is maintained across **three synchronized data structures**.

---

### 🔹 1. Hash Table — *Fast Cell Lookup*
**Usage**
- Stores filled positions for quick validation of:
  - Rows
  - Columns
  - 3×3 sub-grids

**Justification**
- Provides **O(1)** average-time lookup
- Greatly speeds up validation during backtracking
- Collisions handled using **chaining**

---

### 🔹 2. Binary Search Tree (BST) — *Sorted Storage / Move History*
**Usage**
- Stores moves using a unique **Cell ID**
- Cell ID = (Row × 9) + Column


**Justification**
- Maintains data in **sorted order**
- **Inorder traversal** displays moves in ascending order
- Helps in understanding and debugging the solving process

---

### 🔹 3. Singly Linked List — *Input / Entry Order*
**Usage**
- Stores Sudoku entries exactly in the order entered by the user

**Justification**
- Preserves **insertion order**
- Demonstrates **dynamic memory allocation**
- Acts as a historical log of user input

---

## ⚙️ Implementation Details
- Implemented in **Python**
- Uses a **class-based modular approach**
- Central controller: **`SudokuSolver` class**

### 🔸 SudokuSolver Responsibilities
- Coordinates:
- Linked List
- BST
- Hash Table
- Keeps all data structures **synchronized**

---

## 📊 Complexity Analysis

| Operation | Data Structure | Algorithm | Average Time | Worst Case |
|---------|---------------|----------|-------------|------------|
| Insert Cell | Linked List | Tail Insert | O(1) | O(n) |
| Validate Number | Hash Table | Hashing | O(1) | O(n) |
| Store Move | BST | Recursive Insert | O(log n) | O(n) |
| Solve Puzzle | Backtracking | Recursive | O(9^m) | O(9^m) |
| Display Board | LL / BST | Traversal | O(n) | O(n) |
| Save File | Linked List | CSV Write | O(n) | O(n) |
| Load File | Linked List | CSV Read | O(n) | O(n) |

> **m = number of empty cells**

---

## 💾 File Handling (Persistence)

### 🔹 Saving Sudoku
- Method: **`save_board()`**
- Iterates through the Linked List
- Writes `(row, column, number)` to **`sudoku_data.csv`**

### 🔹 Loading Sudoku
- Method: **`load_board()`**
- Reads CSV line-by-line
- Reconstructs:
- Linked List
- BST
- Hash Table

---

## 🖥️ Program Features & Menu

### 📋 Menu Options
- Display Sudoku
- Solve Sudoku
- Load Sudoku
- Save Sudoku
- Display BST Inorder Traversal
- Exit

<img width="709" height="471" alt="image" src="https://github.com/user-attachments/assets/a4989336-2a3c-4720-9a77-795dd61bf626" />

---

### 1️⃣ Display Sudoku
- Prints the current grid
- Empty cells shown as **0**

---

### 2️⃣ Solve Sudoku
- Uses **Backtracking Algorithm**
- Validates using **Hash Table**
- Stores solved moves in **BST**
- Displays solved board if solution exists

---

### 3️⃣ Save Sudoku
- Saves current grid to **sudoku.txt**

---

### 4️⃣ Load Sudoku
- Loads Sudoku from file
- Displays confirmation message

---

### 5️⃣ BST Inorder Traversal
- Displays BST contents in **sorted order**
- Shows move history by Cell ID

---

### 6️⃣ Exit Program
- Safely terminates execution

---

## ✅ Conclusion
The **Sudoku Solver System** is a **DSA-focused, exam-ready project** that demonstrates:

- ✔ Linked Lists for insertion order  
- ✔ Hash Tables for fast validation  
- ✔ BST for sorted history  
- ✔ Backtracking Algorithm  
- ✔ File handling and persistence  

This project is ideal for:
- **DSA coursework**
- **Practical exams**
- **GitHub portfolio**
- **Viva preparation**

---

⭐ **If you like this project, don’t forget to star the repository!**

