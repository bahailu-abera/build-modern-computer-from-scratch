# Computer

This folder contains the **top-level Computer chip** of the Hack computer.  
It integrates the CPU and Memory, allowing programs stored in ROM to execute.

## 📂 Contents

- **chips/Computer.hdl** → Computer implementation  
- **tests/Computer.tst** → Test script  

## 🧩 Design Approach
- Connects CPU outputs to Memory inputs  
- Provides a `reset` input to restart program execution  
- Interfaces with ROM to fetch instructions  

## ▶️ How to Run Tests
1. Open the [Nand2Tetris Hardware Simulator](https://www.nand2tetris.org/software)  
2. Load `Computer.tst` from `tests/`  
3. Run the test — outputs must match expected `.cmp` file
