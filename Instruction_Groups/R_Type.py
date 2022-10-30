import sys
#from Assembler.main import REG
#sys.path.insert(0, '/home/programish/Assembler')

funct3 = {'SLLI':'001', 'SRLI':'101', 'SRAI':'101', 'ADD':'000', 'SUB':'000', 'SLL':'001','SLT':'010',
          'SLTU':'011', 'XOR':'100', 'SRL':'101', 'SRA':'101', 'OR':'110', 'AND':'111'} 

REG = ['ZERO', 'RA', 'SP', 'GP', 'TP', 'T0', 'T1', 'T2', 'FP', 'S1', 'A0', 'A1', 'A2', 'A3', 'A4', 'A5',
       'A6', 'A7', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'T3', 'T4', 'T5', 'T6']

def funct7(inst):
    if(inst in ['SRAI', 'SUB', 'SRA']):
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
    
#    bin_res += bin(int(str(REG.index(ins_lst[3])), 16))[2:]
#    bin_res += bin(int(str(REG.index(ins_lst[2]), 16))[2:]
    bin_res += bin(REG.index(ins_lst[3]))[2:]
    bin_res += bin(REG.index(ins_lst[2]))[2:]
    bin_res += funct3[ins_lst[0]]
#    bin_res += bin(int(str(REG.index(ins_lst[1])), 16))[2:]
    bin_res += bin(REG.index(ins_lst[1]))[2:]
    bin_res += opcode(ins_lst[0])
    print('Binary : ' + bin_res)
    print('Hex : ' + hex(int(bin_res[2:], 2)))
