import Instruction_Groups
from Instruction_Groups import R_Type

R = ['SLLI', 'SRLI', 'SRAI', 'ADD', 'SUB', 'SLL', 'SLT', 'SLTU', 'XOR', 'SRL', 'SRA', 'OR', 'AND']
I = ['JALR', 'LB', 'LH', 'LW', 'LBU', 'LHU', 'ADDI', 'SLTI', 'SLTIU', 'XORI', 'ORI', 'ANDI']
S = ['SB', 'SH', 'SW']
B = ['BEQ', 'BNE', 'BLT', 'BGE', 'BLTU', 'BGEU']
U = ['LUI', 'AUIPC']
J = ['JAL']

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
    if ls[0].upper() in R:
       R_Type.formatter(ls)
    elif ls[0].upper() in J:
       R_Type.formatter(ls)
    elif ls[0].upper() in U:
       R_Type.formatter(ls)

    s = input("Want to quit?(y/n)")
