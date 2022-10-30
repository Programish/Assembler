import sys
#from Assembler.main import REG
#sys.path.insert(0, '/home/programish/Assembler')

funct3 = {'SLLI':'001', 'SRLI':'101', 'SRAI':'101', 'ADD':'000', 'SUB':'000', 'SLL':'001','SLT':'010',
          'SLTU':'011', 'XOR':'100', 'SRL':'101', 'SRA':'101', 'OR':'110', 'AND':'111'} 

REG = ['ZERO', 'RA', 'SP', 'GP', 'TP', 'T0', 'T1', 'T2', 'FP', 'S1', 'A0', 'A1', 'A2', 'A3', 'A4', 'A5',
       'A6', 'A7', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'T3', 'T4', 'T5', 'T6']

def funct7(inst):
    if(inst.upper() in ['SRAI', 'SUB', 'SRA']):
        return str('01'+'0'*5)
    else:
        return str('0'*7)

def opcode(inst):
    if inst[0].upper() is 'S':
        return '0010011'
    else:
        return '0110011'

def formatter(ins_lst):
    bin_res = '0b' + funct7(ins_lst[0])
    
    if ins_lst[0][0].upper() is 'S':                        # Shift operations
        if ins_lst[3].__contains__('x'):                    # Hex immediates
            if len(bin(int(ins_lst[3], 16))[2:]) > 5:
                raise ValueError("Immediate passed is out of range!!!! \n Enter value <= 0x19 \n")
                return
            else:
                bin_res += bin(int(ins_lst[3], 16))[2:]
        elif ins_lst[3].__contains__('b'):                  # Bin immediates
            if len(ins_lst[3][2:]) > 5:
                raise ValueError("Immediate passed is out of range!!!! \n Enter value <= 0b11111 \n")
                return
            else:
                bin_res += ins_lst[3][2:]
        elif ins_lst[3] is int:                             # Int immediates
            if ins_lst[3] > 31:
                raise ValueError("Immediate passed is out of range!!!! \n Enter value <= 31 \n")
                return
            else:
                bin_res += bin(ins_lst[3])[2:]
        else:
            raise ValueError("Passed Immediate not allowed!!!! \n Only hex/bin/int values are allowed \n")
            return
    elif ins_lst[3].upper() in REG:                         # Except shift operations
        bin_res += '0'*(7-len(bin(REG.index(ins_lst[3])))) + bin(REG.index(ins_lst[3]))[2:]
    else:
        raise ValueError("2nd Source Register is unknown!!!!\n")
        return
    
    if ins_lst[2].upper() in REG:
        bin_res += '0'*(7-len(bin(REG.index(ins_lst[2])))) + bin(REG.index(ins_lst[2]))[2:]
    else:
        raise ValueError("1st Source Register is unknown!!!!\n")
        return
    
    bin_res += funct3[ins_lst[0]]
    
    if ins_lst[2].upper() in REG:
        bin_res += '0'*(7-len(bin(REG.index(ins_lst[1])))) + bin(REG.index(ins_lst[2]))[2:]
    else:
        raise ValueError("Destination Register is unknown!!!!\n")
        return
    
    bin_res += opcode(ins_lst[0])
    
    print('Binary : ' + bin_res)
    print('Hex : ' + hex(int(bin_res[2:], 2)))
