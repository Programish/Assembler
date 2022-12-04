import Instruction_Groups
from Instruction_Groups import I_Type, R_Type, B_Type#, J_Type, S_Type, U_Type

R = ['SLLI', 'SRLI', 'SRAI', 'ADD', 'SUB', 'SLL', 'SLT', 'SLTU', 'XOR', 'SRL', 'SRA', 'OR', 'AND']
I = ['JALR', 'LB', 'LH', 'LW', 'LBU', 'LHU', 'ADDI', 'SLTI', 'SLTIU', 'XORI', 'ORI', 'ANDI']
S = ['SB', 'SH', 'SW']
B = ['BEQ', 'BNE', 'BLT', 'BGE', 'BLTU', 'BGEU']
U = ['LUI', 'AUIPC']
J = ['JAL']

s = ''
while(s is not 'y'):
    s = input()
    s = s.upper()
    ls = s.replace(",", "").split()
    flag = "1" if (ls[0][-1] in ("S", "s")) else "0"
    
    print("           OpCode : " + ls[0])
    print("               Rd : " + ls[1])

    if ls[-1].__contains__('('):
        print("               Rn : " + ls[-1][ls[-1].index('(')+1:ls[-1].index(')')])
    else:
        print("               Rn : " + ls[2])
    
    if ls[-1].__contains__('('): 
        print("  shifter operand : " + ls[-1][:ls[-1].index('(')])
    else:
        print("  shifter operand : " + ls[-1])
    
    print("      status flag : " + flag)
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    try:
        if ls[0].upper() in R:
            R_Type.formatter(ls)
        elif ls[0].upper() in J:
            J_Type.formatter(ls)
        elif ls[0].upper() in U:
            U_Type.formatter(ls)
        elif ls[0].upper() in B:
            B_Type.formatter(ls)
        elif ls[0].upper() in I:
            I_Type.formatter(ls)
        elif ls[0].upper() in S:
            S_Type.formatter(ls)
    except ValueError as err:
        print(str(err))
    
    s = input("Want to quit?(y/n)")
