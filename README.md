# ♟️ Chess Putting Board

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)

A simple Python program that places chess pieces on an **8×8 chessboard** based on user input and displays the completed board in the terminal.

## ✨ Features

- Place chess pieces using standard board coordinates
- Supports an 8×8 chessboard
- Alternating chessboard pattern using `#` and `.`
- Accepts multiple pieces until `Done` is entered
- Displays the completed board directly in the terminal

## 🚀 Getting Started

### Requirements

- Python 3

### Clone the repository

```bash
git clone https://github.com/guntichainma/chess-putting-board.git
cd chess-putting-board
```

### Run the program

```bash
python3 main.py
```

## 🎮 Example

### Input

```text
R
a
8
N
b
8
p
e
2
k
e
1
Done
```

### Output

```text
+---+---+---+---+---+---+---+---+
| R | N | . | # | . | # | . | # | 8
+---+---+---+---+---+---+---+---+
| # | . | # | . | # | . | # | . | 7
+---+---+---+---+---+---+---+---+
| . | # | . | # | . | # | . | # | 6
+---+---+---+---+---+---+---+---+
| # | . | # | . | # | . | # | . | 5
+---+---+---+---+---+---+---+---+
| . | # | . | # | . | # | . | # | 4
+---+---+---+---+---+---+---+---+
| # | . | # | . | # | . | # | . | 3
+---+---+---+---+---+---+---+---+
| . | # | . | # | p | # | . | # | 2
+---+---+---+---+---+---+---+---+
| # | . | # | . | k | . | # | . | 1
+---+---+---+---+---+---+---+---+
  a   b   c   d   e   f   g   h
```

## 📁 Project Structure

```text
chess-putting-board/
├── main.py
└── README.md
```

## 🛠️ Built With

- Python 3
- Git
- GitHub

## 🎯 What I Learned

This project helped me practice:

- Python lists
- Nested loops
- User input
- Coordinate conversion
- Conditional statements
- Building and displaying a 2D board

## 👤 Author

Created by [@guntichainma](https://github.com/guntichainma)