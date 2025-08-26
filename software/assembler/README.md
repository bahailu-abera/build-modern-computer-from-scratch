# Hack Assembler

This project implements an assembler for the Hack computer platform, as defined in *"The Elements of Computing Systems"* by Nisan and Schocken. The assembler translates Hack assembly language (`.asm`) programs into binary machine code (`.hack`).


## Components Overview


### `assembler.py`
- Orchestrates the assembly process.
- Performs a **first pass** to resolve labels (L-instructions) and store them in the symbol table.
- Performs a **second pass** to translate A- and C-instructions into 16-bit binary codes and writes the output `.hack` file.

### `Parser/`
- `FileStream` reads the file line by line.
- `Parser` strips whitespace and comments, determines instruction types (`A`, `C`, `L`), and parses symbols, `dest`, `comp`, and `jump` fields.

### `Code/`
- Translates assembly mnemonics to their binary equivalents.
- `comp_table.py`, `dest_table.py`, and `jump_table.py` store lookup tables according to the Hack specification.
- `code.py` provides static methods `Code.comp()`, `Code.dest()`, and `Code.jump()`.

### `SymbolTable/`
- `builtin_symbols.py` initializes pre-defined Hack symbols (R0–R15, SP, LCL, ARG, THIS, THAT, SCREEN, KBD).
- `symbol_table.py` manages user-defined symbols and variable addresses starting at memory location 16.



## Usage

```bash
# Make the assembler executable
chmod +x assembler.py

# Run the assembler on an assembly file
./assembler.py Prog.asm

# This will produce Prog.hack in the same directory

```

## References

- [Nand2Tetris Project 6: Assembler](https://www.nand2tetris.org/project06)
