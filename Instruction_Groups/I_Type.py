import Registers
from Registers import REG

funct3 = {'JALR':'000', 'LB':'000', 'LH':'001', 'LW':'010', 'LBU':'100', 'LHU':'101',
          'ADDI':'000', 'SLTI':'010', 'SLTIU':'011', 'XORI':'100', 'ORI':'110', 'ANDI':'111'}

def opcode(inst):
    if inst[0].upper() is 'JALR':
        return '1100111'
    elif inst[0].upper() in ('LB', 'LH', 'LW', 'LBU', 'LHU'):
        return '0000011'
    elif inst[0].upper() in ('ADDI', 'SLTI', 'SLTIU', 'XORI', 'ORI', 'ANDI'):
        return '0010011'

def formatter(ins_lst):
    bin_res = '0b'
    
    if ins_lst[3].__contains__('x'):                    # Hex immediates
        if len(bin(int(ins_lst[3], 16))[2:]) > 12:
            raise ValueError("Immediate passed is out of range!!!! \n Enter value <= 0xfff \n")
            return
        else:
            bin_res += bin(int(ins_lst[3], 16))[2:]
    elif ins_lst[3].__contains__('b'):                  # Bin immediates
        if len(ins_lst[3][2:]) > 12:
            raise ValueError("Immediate passed is out of range!!!! \n Enter value <= 0b111111111111 \n")
            return
        else:
            bin_res += ins_lst[3][2:]
    elif type(ins_lst[3]) is int:                       # Int immediates
        if ins_lst[3] > 4095:
            raise ValueError("Immediate passed is out of range!!!! \n Enter value <= 4095 \n")
            return
        else:
            bin_res += bin(ins_lst[3])[2:]
    else:
        raise ValueError("Passed Immediate not allowed!!!! \n Only hex/bin/int values are allowed \n")
        return

    if ins_lst[1].upper() in REG:
        bin_res += '0'*(7-len(bin(REG.index(ins_lst[1])))) + bin(REG.index(ins_lst[1]))[2:]
    else:
        raise ValueError("1st Source Register is unknown!!!!\n")
        return
    
    bin_res += funct3[ins_lst[0]]
    
    if ins_lst[1].upper() in REG:
        bin_res += '0'*(7-len(bin(REG.index(ins_lst[1])))) + bin(REG.index(ins_lst[1]))[2:]
    else:
        raise ValueError("Destination Register is unknown!!!!\n")
        return

    bin_res += opcode(ins_lst[0])
    
    print('Binary : ' + bin_res)
    print('Hex : ' + hex(int(bin_res, 2)))
