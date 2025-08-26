# Memory

This folder contains the **Memory chip** of the Hack computer.  
It implements the full memory map, including RAM, Screen memory, and Keyboard input.

## 📂 Contents

- **chips/Memory.hdl** → Memory implementation  
- **tests/Memory.tst** → Test script  

## 🧩 Design Approach
- Uses `RAM16K` for general-purpose RAM  
- Maps addresses for screen memory and keyboard input  
- Selects output from RAM, Screen, or Keyboard based on address  

## ▶️ How to Run Tests
1. Open the [Nand2Tetris Hardware Simulator](https://www.nand2tetris.org/software)  
2. Load `Memory.tst` from `tests/`  
3. Run the test — outputs must match expected `.cmp` file
