import Instruction_Groups
from Instruction_Groups import R_Type

R = ['SLLI', 'SRLI', 'SRAI', 'ADD', 'SUB', 'SLL', 'SLT', 'SLTU', 'XOR', 'SRL', 'SRA', 'OR', 'AND']
I = ['JALR', 'LB', 'LH', 'LW', 'LBU', 'LHU', 'ADDI', 'SLTI', 'SLTIU', 'XORI', 'ORI', 'ANDI']
S = ['SB', 'SH', 'SW']
B = ['BEQ', 'BNE', 'BLT', 'BGE', 'BLTU', 'BGEU']
U = ['LUI', 'AUIPC']
J = ['JAL']

REG = ['ZERO', 'SP', 'GP', 'TP', 'T0', 'T1', 'T2', 'FP', 'S1', 'A0', 'A1', 'A2', 'A3', 'A4', 'A5',  
       'A6', 'A7', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'T3', 'T4', 'T5', 'T6']          
s = ''
while(s is not 'y'):
    s = input()
    ls = s.replace(",", "").split()
#    flag = "1" if (ls[0][-1] in ("S", "s")) else "0"
#    print("           OpCode : " + ls[0] + "    " + opcode[ls[0]])
#    print("               Rd : " + ls[1])
#    print("               Rn : " + ls[2])
#    print("  shifter operand : " + ls[3])
#    print("      status flag : " + flag)
#    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    if ls[0] in R:
       R_Type.formatter(ls)
    s = input("Want to quit?(y/n)")
