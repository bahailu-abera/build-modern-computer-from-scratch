"""
code_writer.py

Translates VM commands into Hack assembly using predefined templates.
"""

from constants.command_types import (
    UNARY_COMMANDS,
    ADD,
    SUB,
    NEG,
    AND,
    OR,
    NOT,
    EQ,
    LT,
    GT,
    PUSH,
    POP
)

from constants.compute_asm_template import (
    LOAD_SP_TO_A,
    LOAD_SP_TO_D,
    INCREMENT_SP,
    DECREMENT_SP,
    BINARY_ADD,
    BINARY_SUB,
    BINARY_AND,
    BINARY_OR,
    UNARY_NEG,
    UNARY_NOT,
    COMPARE_EQ,
    COMPARE_LT,
    COMPARE_GT,
)

from constants.memory_segment_mapping import (
    TEMP,
    STATIC,
    POINTER,
    CONSTANT,
    SEGMENT_BASE
)

from constants.memory_asm_template import (
    POP_SEGMENT,
    POP_POINTER,
    POP_STATIC,
    POP_TEMP,
    PUSH_SEGMENT,
    PUSH_POINTER,
    PUSH_STATIC,
    PUSH_CONSTANT,
    PUSH_TEMP,
    PUSH_M_TO_STACK
)


class CodeWriter:
    def __init__(self, output_filename: str = None) -> None:
        self.output_filename = output_filename
        self.vm_file_name = None
        self.file = open(self.output_filename, "w")
        self.label_counter = 0  # unique label counter

        self.__write_init()

    def __write_asm_instructions(self, instructions: str) -> None:
        """
        Writes the generated asm instructions to the output file.
        """
        self.file.write(instructions)

    def __write_init(self) -> None:
        """Writes the bootstrap code (SP=256)."""
        bootstrap = "// Bootstrap\n@256\nD=A\n@SP\nM=D\n"
        self.__write_asm_instructions(bootstrap)

    def __get_label(self) -> int:
        """Returns a unique integer label ID for comparison commands."""
        self.label_counter += 1
        return self.label_counter

    def __handle_unary_command(self, command: str) -> None:
        """
        Handles unary operations (neg, not).
        """
        if command == NEG:
            asm_instruction = UNARY_NEG.format(
                INCREMENT_SP=INCREMENT_SP,
                DECREMENT_SP=DECREMENT_SP,
                LOAD_SP_TO_A=LOAD_SP_TO_A,
            )
        elif command == NOT:
            asm_instruction = UNARY_NOT.format(
                INCREMENT_SP=INCREMENT_SP,
                DECREMENT_SP=DECREMENT_SP,
                LOAD_SP_TO_A=LOAD_SP_TO_A,
            )
        else:
            raise NotImplementedError(f"Unsupported unary command: {command}")

        self.__write_asm_instructions(asm_instruction)

    def __handle_binary_command(self, command: str) -> None:
        """
        Handles binary arithmetic, logical, and comparison commands.
        """
        if command == ADD:
            asm_instruction = BINARY_ADD.format(
                INCREMENT_SP=INCREMENT_SP,
                DECREMENT_SP=DECREMENT_SP,
                LOAD_SP_TO_A=LOAD_SP_TO_A,
                LOAD_SP_TO_D=LOAD_SP_TO_D,
            )
        elif command == SUB:
            asm_instruction = BINARY_SUB.format(
                INCREMENT_SP=INCREMENT_SP,
                DECREMENT_SP=DECREMENT_SP,
                LOAD_SP_TO_A=LOAD_SP_TO_A,
                LOAD_SP_TO_D=LOAD_SP_TO_D,
            )
        elif command == AND:
            asm_instruction = BINARY_AND.format(
                INCREMENT_SP=INCREMENT_SP,
                DECREMENT_SP=DECREMENT_SP,
                LOAD_SP_TO_A=LOAD_SP_TO_A,
                LOAD_SP_TO_D=LOAD_SP_TO_D,
            )
        elif command == OR:
            asm_instruction = BINARY_OR.format(
                INCREMENT_SP=INCREMENT_SP,
                DECREMENT_SP=DECREMENT_SP,
                LOAD_SP_TO_A=LOAD_SP_TO_A,
                LOAD_SP_TO_D=LOAD_SP_TO_D,
            )
        elif command in (EQ, LT, GT):
            label_id = self.__get_label()
            if command == EQ:
                template = COMPARE_EQ
            elif command == LT:
                template = COMPARE_LT
            else:  # GT
                template = COMPARE_GT

            asm_instruction = template.format(
                INCREMENT_SP=INCREMENT_SP,
                DECREMENT_SP=DECREMENT_SP,
                LOAD_SP_TO_A=LOAD_SP_TO_A,
                LOAD_SP_TO_D=LOAD_SP_TO_D,
                label=label_id,
            )
        else:
            raise NotImplementedError(f"Unsupported binary command: {command}")

        self.__write_asm_instructions(asm_instruction)

    def write_compute(self, command: str) -> None:
        """
        Writes assembly code that is the translation of the given compute command.
        """
        if command in UNARY_COMMANDS:
            self.__handle_unary_command(command)
        else:
            self.__handle_binary_command(command)

    def __handle_pop_command(self, segment: str, index: int) -> None:
        """
        Handle pop commands for all segments.
        """
        base = SEGMENT_BASE.get(segment)

        # Prepare placeholders
        helpers = {
            "DECREMENT_SP": DECREMENT_SP,
            "LOAD_SP_TO_D": LOAD_SP_TO_D,
        }

        if segment == TEMP or segment == POINTER:
            addr = int(base) + index
            template = POP_TEMP if segment == TEMP else POP_POINTER
            asm_instruction = template.format(addr=addr, index=index, **helpers)
        elif segment == STATIC:
            asm_instruction = POP_STATIC.format(filename=self.vm_file_name, index=index, **helpers)
        else:
            # dynamic segments: local, argument, this, that
            if base is None:
                raise ValueError(f"Unknown segment: {segment}")
            asm_instruction = POP_SEGMENT.format(segment=segment, index=index, base=base, **helpers)

        self.__write_asm_instructions(asm_instruction)

    def __handle_push_command(self, segment: str, index: int) -> None:
        """
        Handle push commands for all segments.
        """
        base = SEGMENT_BASE.get(segment)

        # Prepare PUSH_M_TO_STACK with helpers
        push_m_to_stack_expanded = PUSH_M_TO_STACK.format(
            LOAD_SP_TO_A=LOAD_SP_TO_A,
            INCREMENT_SP=INCREMENT_SP
        )

        helpers = {
            "PUSH_M_TO_STACK": push_m_to_stack_expanded
        }

        if segment == TEMP or segment == POINTER:
            addr = int(base) + index
            template = PUSH_TEMP if segment == TEMP else PUSH_POINTER
            asm_instruction = template.format(addr=addr, index=index, **helpers)
        elif segment == CONSTANT:
            asm_instruction = PUSH_CONSTANT.format(index=index, LOAD_SP_TO_A=LOAD_SP_TO_A,
                                                   INCREMENT_SP=INCREMENT_SP)
        elif segment == STATIC:
            asm_instruction = PUSH_STATIC.format(filename=self.vm_file_name, index=index, **helpers)
        else:
            if base is None:
                raise ValueError(f"Unknown segment: {segment}")
            asm_instruction = PUSH_SEGMENT.format(segment=segment, index=index, base=base, **helpers)

        self.__write_asm_instructions(asm_instruction)

    def write_push_pop(self, command: str, segment: str, index: int) -> None:
        """
        Writes assembly code for push/pop commands.
        (To be implemented in memory access templates.)
        """
        if command == POP:
            self.__handle_pop_command(segment, index)
        elif command == PUSH:
            self.__handle_push_command(segment, index)
        else:
            raise NotImplementedError("Push/pop handling not implemented yet.")

    def set_file_name(self, vm_file_name: str) -> None:
        """
        Informs the code writer that the translation of a new VM file has started.
        """
        self.vm_file_name = vm_file_name
        self.__write_asm_instructions(f"// Translating {self.vm_file_name}\n")

    def close(self):
        """
        Closes the output file.
        """
        self.file.close()
