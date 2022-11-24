import Registers
from Registers import REG

funct3 = {'JALR':'000', 'LB':'000', 'LH':'001', 'LW':'010', 'LBU':'100', 'LHU':'101',
          'ADDI':'000', 'SLTI':'010', 'SLTIU':'011', 'XORI':'100', 'ORI':'110', 'ANDI':'111'}

def opcode(inst):
    if inst is 'JALR':
        return '1100111'
    elif inst in ('LB', 'LH', 'LW', 'LBU', 'LHU'):
        return '0000011'
    elif inst in ('ADDI', 'SLTI', 'SLTIU', 'XORI', 'ORI', 'ANDI'):
        return '0010011'

def formatter(ins_lst):
    bin_res = '0b'
    print() 
    if ins_lst[3].__contains__('X'):                                # Hex immediates
        if len(bin(int(ins_lst[3], 16))[2:]) > 12:
            raise ValueError("Immediate passed is out of range!!!! \n Enter value <= 0xfff \n")
            return
        else:
            bin_no = bin(int(ins_lst[3], 16))[2:]
            fin_bin_no = '0' * (12-len(bin_no)) + bin_no
            bin_res += fin_bin_no
    elif ins_lst[3].__contains__('B'):                              # Bin immediates
        if len(ins_lst[3][2:]) > 12:
            raise ValueError("Immediate passed is out of range!!!! \n Enter value <= 0b111111111111 \n")
            return
        else:
            bin_no = ins_lst[3][2:]
            fin_bin_no = '0' * (12-len(bin_no)) + bin_no
            bin_res += fin_bin_no
    elif ins_lst[3].isnumeric():                                    # Positive Int immediates
        if int(ins_lst[3]) > 4095:
            raise ValueError("Immediate passed is out of range!!!! \n Enter value <= 4095 \n")
            return
        else:
            bin_no = bin(int(ins_lst[3]))[2:]
            fin_bin_no = '0' * (12-len(bin_no)) + bin_no
            bin_res += fin_bin_no

    elif ins_lst[3][1:].isnumeric() and ins_lst[3][0] is '-':       # Negative Int immediates
        if int(ins_lst[3][1:]) > 4094:
            raise ValueError("Immediate passed is out of range!!!! \n Enter value >= -4094 \n")
            return
        else:
            bin_no = bin(int(ins_lst[3][1:]))[2:]
            fin_bin_no = '0' * (12-len(bin_no)) + bin_no
            flipped_bits = ''.join(['1' if i == '0' else '0' for i in fin_bin_no])
            bin_neg_no = bin(int(flipped_bits, 2) + int('1', 2))
            bin_res += bin_neg_no[2:]

    else:
        raise ValueError("Passed Immediate not allowed!!!! \nOnly hex/bin/int values are allowed \n")
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
