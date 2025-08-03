
# Merkle Tree Insurance System

This project demonstrates the use of Merkle Trees in an insurance claim system, providing both a backend implementation and a graphical user interface (GUI).

## Features

- **Merkle Tree Implementation:**  
  - Two Python modules (`Merkle_Tree.py` and `ammended.py`) provide different approaches to building and managing Merkle Trees, including insertion, proof generation, and verification.
- **Insurance Claim GUI:**  
  - `GUI.py` offers a Tkinter-based interface for users to submit, insert, and verify insurance claims, all backed by a Merkle Tree for data integrity.
- **LaTeX Report:**  
  - The workspace includes a LaTeX report (`L2_Group_2.tex` and related files) documenting the project.

## Main Files

- `Merkle_Tree.py`:  
  Object-oriented Merkle Tree implementation with node-based structure and methods for building, inserting, and verifying tree data.

- `ammended.py`:  
  Alternative Merkle Tree implementation using lists to represent tree levels, with functions for root calculation, proof generation, and verification.

- `GUI.py`:  
  Tkinter GUI for interacting with the insurance claim system. Users can build a tree from claims, insert new claims, and verify claim inclusion.

- `L2_Group_2.tex` and related files:  
  LaTeX source and output for the project report.

- `Hash_Tree.png`:  
  Image resource, likely used in the report or documentation.

## Usage

1. **Run the GUI:**  
   Execute `GUI.py` to launch the insurance claim form and interact with the Merkle Tree system.

   ```bash
   python3 GUI.py
   ```

2. **Explore Merkle Tree Implementations:**  
   Review or run `Merkle_Tree.py` and `ammended.py` for different approaches to Merkle Tree logic and testing.

## Notes

- The project is a prototype and may not be fully complete.
- Some features (like deletion in the GUI) may be placeholders or under development.
