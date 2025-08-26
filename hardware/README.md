# Hardware Projects — Build a Modern Computer from First Principles

This folder contains all **hardware projects** from the Nand2Tetris course, implementing the Hack computer from the ground up.  
The projects are organized into stages, starting with basic logic gates and progressing to a fully functional CPU and Computer.

## 📂 Subprojects

### 1. Elementary Logic
Folder: `elementary-logic/`  
- Implements **basic and multi-way logic gates** using only NAND gates.  
- Provides the foundation for building arithmetic circuits, registers, and memory.  
- Chips include: `Not`, `And`, `Or`, `Xor`, `Mux`, `DMux`, and their 16-bit / multi-way versions.  
- [See README](./hardware/elementary-logic/README.md)

### 2. Boolean Arithmetic
Folder: `boolean-arithmetic/`  
- Implements **arithmetic circuits** including half/full adders and the 16-bit ALU.  
- Chips include: `HalfAdder`, `FullAdder`, `Add16`, `Inc16`, `ALU`.  
- Provides the computational core for the CPU.  
- [See README](./hardware/boolean-arithmetic/README.md)

### 3. Memory
Folder: `memory/`  
- Implements **registers and RAM modules**, from single-bit memory to 16K-word RAM.  
- Organizes memory into `small-mem/` (Bit, Register, RAM8, RAM64, PC) and `large-mem/` (RAM512, RAM4K, RAM16K).  
- [See README](./hardware/memory/README.md)

### 4. CPU & Computer
Folder: `cpu-computer/`  
- Implements the **CPU**, the **Memory-mapped Computer**, and top-level integration.  
- CPU handles instruction execution, ALU operations, and register/memory control.  
- Computer connects CPU + Memory + ROM to run Hack programs (`Add`, `Max`, `Rect`).  
- Organized into subfolders:  
  - `cpu/` → CPU chip + tests  
  - `memory/` → top-level Memory chip + tests  
  - `computer/` → top-level Computer chip + tests  
- [See README](./hardware/cpu-computer/README.md)

## 🧩 Design Approach
- Projects are **hierarchical and modular**: small chips are verified first, then composed into larger systems.  
- Each stage builds on the previous, culminating in a fully functional Hack computer hardware.  
- Official `.tst` scripts are used for testing each chip.  

## ▶️ How to Run Tests
1. Open the [Nand2Tetris Hardware Simulator](https://www.nand2tetris.org/software)  
2. Navigate to any subproject folder (`chips/` and `tests/`)  
3. Load a `.tst` file and run — outputs must match the corresponding `.cmp` file  

---

✅ All hardware projects pass the official Nand2Tetris test scripts, forming the foundation for software, OS, and CPU integration in later projects.
