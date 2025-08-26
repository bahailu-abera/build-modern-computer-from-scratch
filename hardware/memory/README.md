# Project 03 — Memory

This folder contains the third stage of building the Hack computer: **memory components**.  
We implement registers and RAM modules of increasing size, from a single bit to 16K 16-bit words.

## 📂 Contents

- **small-mem/** → Chips for 1-bit to 64-word memory units (`Bit`, `Register`, `RAM8`, `RAM64`, `PC`)  
- **large-mem/** → Chips for larger RAMs (`RAM512`, `RAM4K`, `RAM16K`)  
- **tests/** → Official `.tst` scripts for verification

### Implemented Chips
- **Single-bit and register:** `Bit`, `Register`, `PC`  
- **Small RAMs:** `RAM8`, `RAM64` (16-bit words)  
- **Large RAMs:** `RAM512`, `RAM4K`, `RAM16K` (16-bit words)

## 🧩 Design Approach
- **Hierarchical composition:** small chips are tested and verified first, then used to build larger RAM units.  
- **Memory addressing:** higher-level RAMs built by composing smaller RAMs with address decoding.  
- **Program counter (PC):** special register chip with incrementing and load capabilities.  

## ▶️ How to Run Tests
1. Open the [Nand2Tetris Hardware Simulator](https://www.nand2tetris.org/software).  
2. Load any `.tst` file from the `tests/` folder.  
3. Run the test — the chip should behave as specified in the `.cmp` file.  

---

✅ All chips in this project pass the official test scripts.  
This stage lays the foundation for the CPU’s memory system in later projects.
