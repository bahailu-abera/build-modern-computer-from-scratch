# Project 01 — Elementary Logic

This folder contains the first stage of building the Hack computer: **elementary logic gates**.  
All chips here are implemented using only the primitive `Nand` gate, then composed hierarchically into more complex circuits.

## 📂 Contents

- **chips/** → HDL implementations of logic gates  
- **tests/** → Official test scripts (`.tst`) for verification  

### Implemented Chips
- **Basic gates:** `Not`, `And`, `Or`, `Xor`, `Mux`, `DMux`
- **16-bit gates:** `Not16`, `And16`, `Or16`, `Mux16`
- **Multi-way gates:** `Or8Way`, `Mux4Way16`, `Mux8Way16`, `DMux4Way`, `DMux8Way`

## 🧩 Design Approach
- Start with the primitive **NAND** gate as the only building block.
- Build simple gates (`Not`, `And`, `Or`) and verify correctness.
- Reuse verified gates to construct larger chips (e.g., `Xor`, `Mux`, 16-bit, and multi-way versions).
- Follow a **hierarchical, modular design**: small chips tested in isolation, then composed into more complex circuits.

## ▶️ How to Run Tests
1. Open the [Nand2Tetris Hardware Simulator](https://www.nand2tetris.org/software).  
2. Load any `.tst` file from the `tests/` folder.  
3. Run the test — the corresponding `.hdl` chip should match the expected `.cmp` output.  

---

✅ All chips in this project pass the official test scripts.  
This stage establishes the foundation for arithmetic and memory components in later projects.
