from alu import ALU
from memory import Memory

class CPU:
    def __init__(self, memory_size=256):
        self.registers = {f"R{i}": 0 for i in range(8)}
        self.program_counter = 0
        self.memory = Memory(memory_size)
        self.alu = ALU()
        self.halted = False
    
    def load_program(self, instructions):
        #Load a program into memory
        for i, instruction in enumerate(instructions):
            self.memory.write(i, instruction)

    def fetch(self):
        #Fetch the next instruction from memory
        instruction = self.memory.read(self.program_counter)
        self.program_counter += 1
        return instruction
    
    def decode_execute(self, instruction):
        #Decode and execute a single instruction
        parts = instruction.split()
        op =parts[0]

        if op == "LOAD":
            reg, addr = parts[1], int(parts[2])
            self.registers[reg] = self.memory.read(addr)
        elif op == "STORE":
            addr, reg = int(parts[1]), parts[2]
            self.memory.write(addr, self.registers[reg])
        elif op == "ADD":
            dest, src1, src2 = parts[1], parts[2], parts[3]
            self.registers[dest] = self.alu.add(self.registers[src1], self.registers[src2])
        elif op == "HALT":
            self.halted = True
        else:
            raise ValueError(f"Unknown instruction: {instruction}")
        
    def run(self):
        #Run the program until HALT is encountered
        while not self.halted:
            instruction = self.fetch()
            self.decode_execute(instruction)
            