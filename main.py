from cpu import CPU

def main():
    cpu = CPU()
    program = [
        "LOAD R1, 10",
        "LOAD R2, 20",
        "ADD R3, R1, R2",
        "STORE 30, R3",
        "HALT"
    ]
    cpu.load_program(program)
    cpu.run()
    print(cpu.registers)

if __name__ == "__main__":
    main()