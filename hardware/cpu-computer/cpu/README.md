# CPU

This folder contains the **CPU chip** of the Hack computer.  
The CPU executes instructions according to the Hack machine language, reading from memory and controlling ALU operations, registers, and program flow.

## 📂 Contents

- **chips/CPU.hdl** → CPU implementation  
- **tests/CPU.tst** → Test script  

## 🧩 Design Approach
- Parses instructions into A- or C-type operations  
- Computes ALU operations and sets flags  
- Controls memory writes (`outM`, `writeM`, `addressM`) and program counter (`pc`)  

## ▶️ How to Run Tests
1. Open the [Nand2Tetris Hardware Simulator](https://www.nand2tetris.org/software)  
2. Load `CPU.tst` from `tests/`  
3. Run the test — outputs must match expected `.cmp` file
