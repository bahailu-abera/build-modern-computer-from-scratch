# Project 02 — Boolean Arithmetic

This folder contains the second stage of building the Hack computer: **arithmetic logic circuits**.  
Starting from half and full adders, we construct multi-bit adders and the **Arithmetic Logic Unit (ALU)**.

## 📂 Contents

- **chips/** → HDL implementations  
- **tests/** → Test scripts (`.tst`) for verification  

### Implemented Chips
- **Adders:** `HalfAdder`, `FullAdder`, `Add16`, `Inc16`
- **ALU:** 16-bit Arithmetic Logic Unit (supports add, and, not, or, zeroing, negation, conditional outputs)

## 🧩 Design Approach
- **Compositional design:** HalfAdder → FullAdder → 16-bit adder.  
- **Incrementer:** built by chaining a constant +1 input into the 16-bit adder.  
- **ALU:** integrates arithmetic and logic, with control bits for flexible operations and status flags (zero/negative).

## ▶️ How to Run Tests
1. Open the [Nand2Tetris Hardware Simulator](https://www.nand2tetris.org/software).  
2. Load any `.tst` file from the `tests/` folder.  
3. Run the test — the chip’s behavior should match the expected `.cmp` file.  

---

✅ All chips in this project pass the official test scripts.  
This stage introduces arithmetic and logic operations, forming the foundation of the CPU in later projects.
