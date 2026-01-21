# ==========================================================
#                ADVANCED SUDOKU SOLVER
# ==========================================================
# This project demonstrates the implementation of:
# 1. Linked List      -> Tracking empty Sudoku cells
# 2. Binary Search Tree (BST) -> Storing solved values
# 3. Hash Tables     -> Fast constraint checking
# 4. File Handling   -> Saving and loading Sudoku
# Algorithm Used:
# Backtracking Algorithm
# ==========================================================

# ----------------------------------------------------------
# SECTION 1: LINKED LIST IMPLEMENTATION
# ----------------------------------------------------------
class Node:
    """
    Node class represents a single empty cell position
    Each node stores:
    - Row index
    - Column index
    - Reference to next node
    """
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.next = None
class LinkedList:
    """
    Linked List stores all empty positions in the Sudoku grid.
    It helps in systematic traversal of empty cells.
    """
    def __init__(self):
        self.head = None
    def add(self, row, col):
        new_node = Node(row, col)
        new_node.next = self.head
        self.head = new_node
    def is_empty(self):
        return self.head is None
    def get_cells(self):
        cells = []
        current = self.head
        while current:
            cells.append((current.row, current.col))
            current = current.next
        return cells
    def count(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count
    def display(self):
        temp = self.head
        while temp:
            print(f"({temp.row}, {temp.col}) -> ", end="")
            temp = temp.next
        print("NULL")
# ----------------------------------------------------------
# SECTION 2: BINARY SEARCH TREE (BST)
# ----------------------------------------------------------
class BSTNode:
    """
    BST Node stores a solved Sudoku number.
    """
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
class BST:
    """
    Binary Search Tree stores solved numbers
    and displays them in sorted order using inorder traversal.
    """
    def __init__(self):
        self.root = None
    def insert(self, key):
        self.root = self._insert(self.root, key)
    def _insert(self, root, key):
        if root is None:
            return BSTNode(key)
        if key < root.key:
            root.left = self._insert(root.left, key)
        elif key > root.key:
            root.right = self._insert(root.right, key)
        return root
    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result
    def _inorder(self, root, result):
        if root:
            self._inorder(root.left, result)
            result.append(root.key)
            self._inorder(root.right, result)
    def is_empty(self):
        return self.root is None
# ----------------------------------------------------------
# SECTION 3: HASH TABLES (DICTIONARIES)
# ----------------------------------------------------------
rows = {}
cols = {}
boxes = {}
def initialize_hash_tables():
    for i in range(9):
        rows[i] = set()
        cols[i] = set()
        boxes[i] = set()
def calculate_box_index(row, col):
    return (row // 3) * 3 + (col // 3)
def add_number(row, col, num):
    rows[row].add(num)
    cols[col].add(num)
    boxes[calculate_box_index(row, col)].add(num)
def remove_number(row, col, num):
    rows[row].remove(num)
    cols[col].remove(num)
    boxes[calculate_box_index(row, col)].remove(num)
def is_valid(row, col, num):
    box = calculate_box_index(row, col)
    return (
        num not in rows[row] and
        num not in cols[col] and
        num not in boxes[box]
    )
# ----------------------------------------------------------
# SECTION 4: FILE HANDLING
# ----------------------------------------------------------

def save_sudoku(grid):
    try:
        with open("sudoku.txt", "w") as file:
            for row in grid:
                file.write(" ".join(map(str, row)) + "\n")
        print("Sudoku saved to file successfully.")
    except IOError as e:
        print(f"Error saving Sudoku: {e}")
def load_sudoku():
    try:
        grid = []
        with open("sudoku.txt", "r") as file:
            for line in file:
                grid.append(list(map(int, line.split())))
        print("Sudoku loaded from file successfully.")
        return grid
    except IOError as e:
        print(f"Error loading Sudoku: {e}")
        return None
    except ValueError as e:
        print(f"Invalid file format: {e}")
        return None
# ----------------------------------------------------------
# SECTION 5: DISPLAY UTILITIES
# ----------------------------------------------------------
def print_separator():
    print("=" * 40)
def display_grid(grid):
    print("\nCurrent Sudoku Grid:")
    for i, row in enumerate(grid):
        if i % 3 == 0 and i != 0:
            print("-" * 25)
        row_str = ""
        for j, cell in enumerate(row):
            if j % 3 == 0 and j != 0:
                row_str += "| "
            row_str += str(cell) + " "
        print(row_str)
# ----------------------------------------------------------
# SECTION 6: BACKTRACKING SOLVER
# ----------------------------------------------------------
def solve(grid, empty_cells, index):
    if index == len(empty_cells):
        return True
    row, col = empty_cells[index]
    for num in range(1, 10):
        if is_valid(row, col, num):
            grid[row][col] = num
            add_number(row, col, num)
            if solve(grid, empty_cells, index + 1):
                bst.insert(num)
                return True
            grid[row][col] = 0
            remove_number(row, col, num)
    return False
# ----------------------------------------------------------
# SECTION 7: SUDOKU INITIALIZATION
# ----------------------------------------------------------
def get_default_sudoku():
    return [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
def setup_structures(grid, ll):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                ll.add(i, j)
            else:
                add_number(i, j, grid[i][j])
# ----------------------------------------------------------
# SECTION 8: MAIN PROGRAM (MENU DRIVEN)
# ----------------------------------------------------------
bst = BST()
def reinitialize_all(sudoku, ll):
    """Reset all data structures for a new puzzle."""
    global bst
    initialize_hash_tables()
    bst = BST()
    ll = LinkedList()
    setup_structures(sudoku, ll)
    return ll
def main():
    global bst
    initialize_hash_tables()
    sudoku = get_default_sudoku()
    ll = LinkedList()
    setup_structures(sudoku, ll)
    while True:
        print_separator()
        print("1. Display Sudoku")
        print("2. Solve Sudoku")
        print("3. Save Sudoku")
        print("4. Load Sudoku")
        print("5. Display BST (Inorder Traversal)")
        print("6. Exit")
        print_separator()
        choice = input("Enter your choice: ")
        if choice == '1':
            display_grid(sudoku)
        elif choice == '2':
            empty_cells = ll.get_cells()
            if solve(sudoku, empty_cells, 0):
                print("Sudoku Solved Successfully!")
                display_grid(sudoku)
            else:
                print("No solution exists.")
        elif choice == '3':
            save_sudoku(sudoku)
        elif choice == '4':
            loaded_sudoku = load_sudoku()
            if loaded_sudoku:
                sudoku[:] = loaded_sudoku
                ll = reinitialize_all(sudoku, ll)
            else:
                print("Failed to load. Using current Sudoku.")
        elif choice == '5':
            print("BST Inorder Traversal:", bst.inorder())
        elif choice == '6':
            print("Program Terminated.")
            break
        else:
            print("Invalid choice! Please try again.")
# ----------------------------------------------------------
# PROGRAM EXECUTION
# ----------------------------------------------------------
main() 
