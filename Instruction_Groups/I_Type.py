import Registers
from Registers import REG

funct3 = {'JALR':'000', 'LB':'000', 'LH':'001', 'LW':'010', 'LBU':'100', 'LHU':'101',
          'ADDI':'000', 'SLTI':'010', 'SLTIU':'011', 'XORI':'100', 'ORI':'110', 'ANDI':'111'}

def opcode(inst):
    if inst == 'JALR':
        return '1100111'
    elif inst in ('LB', 'LH', 'LW', 'LBU', 'LHU'):
        return '0000011'
    elif inst in ('ADDI', 'SLTI', 'SLTIU', 'XORI', 'ORI', 'ANDI'):
        return '0010011'

def formatter(ins_lst):
    bin_res = '0b'
    
    if ins_lst[0] == 'JR':                                           # Pseudoinstructions
        ins_lst.insert(1, 'A0')
        ins_lst[0] = 'JALR'
        ins_lst.insert(3, '0')
    elif ins_lst[0] == 'JALR' and len(ins_lst) == 2:
        ins_lst.insert(1, 'A1')
        ins_lst.insert(3, '0')
    elif ins_lst[0] == 'RET':
        ins_lst = ['JALR', 'A0', 'A1', '0']
    elif ins_lst[0] == 'CALL':
        ins_lst.insert(1, 'A1')
        ins_lst.insert(2, 'A6')
        ins_lst[0] = 'JALR'
    elif ins_lst[0] == 'TAIL':
        ins_lst.insert(1, 'A0')
        ins_lst.insert(2, 'A6')
        ins_lst[0] = 'JALR'

    if ins_lst[-1].__contains__('X'):                                # Hex immediates
        if len(bin(int(ins_lst[-1], 16))[2:]) > 12:
            raise ValueError("Immediate passed is out of range!!!! \n Enter value <= 0xfff \n")
            return
        else:
            bin_no = bin(int(ins_lst[-1], 16))[2:]
            fin_bin_no = '0' * (12-len(bin_no)) + bin_no
            bin_res += fin_bin_no
    elif ins_lst[-1].__contains__('B'):                              # Bin immediates
        if len(ins_lst[-1][2:]) > 12:
            raise ValueError("Immediate passed is out of range!!!! \n Enter value <= 0b111111111111 \n")
            return
        else:
            bin_no = ins_lst[-1][2:]
            fin_bin_no = '0' * (12-len(bin_no)) + bin_no
            bin_res += fin_bin_no
    elif ins_lst[-1].isnumeric():                                    # Positive Int immediates
        if int(ins_lst[-1]) > 4095:
            raise ValueError("Immediate passed is out of range!!!! \n Enter value <= 4095 \n")
            return
        else:
            bin_no = bin(int(ins_lst[-1]))[2:]
            fin_bin_no = '0' * (12-len(bin_no)) + bin_no
            bin_res += fin_bin_no
    elif ins_lst[-1][1:].isnumeric() and ins_lst[-1][0] is '-':      # Negative Int immediates
        if int(ins_lst[-1][1:]) > 4094:
            raise ValueError("Immediate passed is out of range!!!! \n Enter value >= -4094 \n")
            return
        else:
            bin_no = bin(int(ins_lst[-1][1:]))[2:]
            fin_bin_no = '0' * (12-len(bin_no)) + bin_no
            #Flipping the bits of original number
            flipped_bits = ''.join(['1' if i == '0' else '0' for i in fin_bin_no])
            #Adding 1 to flipped bits, to get 2's complement of the negative immediate passed
            bin_neg_no = bin(int(flipped_bits, 2) + int('1', 2))
            bin_res += bin_neg_no[2:]
    elif ins_lst[-1].__contains__('('):                             # For Offsets
        # Retrieve offset from last element, by getting everything just before '('
        imm = ins_lst[-1][:ins_lst[-1].index('(')]    
        if imm.isnumeric():                                         # Positive Int Offset
            if int(imm) > 4095:
                raise ValueError("Immediate passed is out of range!!!! \n Enter value <= 4095 \n")
                return
            else:
                bin_no = bin(int(imm))[2:]
                fin_bin_no = '0' * (12-len(bin_no)) + bin_no
                bin_res += fin_bin_no
        elif imm[1:].isnumeric() and imm[0] is '-':                 # Negative Int Offset
            if int(imm[1:]) > 4094:
                raise ValueError("Immediate passed is out of range!!!! \n Enter value >= -4094 \n")
                return
            else:
                bin_no = bin(int(imm[1:]))[2:]
                fin_bin_no = '0' * (12-len(bin_no)) + bin_no
                #Flipping the bits of original number
                flipped_bits = ''.join(['1' if i == '0' else '0' for i in fin_bin_no])
                #Adding 1 to flipped bits, to get 2's complement of the negative immediate passed
                bin_neg_no = bin(int(flipped_bits, 2) + int('1', 2))
                bin_res += bin_neg_no[2:]
    else:
        raise ValueError("Passed Immediate not allowed!!!! \nOnly hex/bin/int values are allowed \n")
        return

    if ins_lst[-1].__contains__('('):                               # Source Register in case of Offset
        # Retrieve source register from last element, by getting everything between '(' and ')'
        sr = ins_lst[-1][ins_lst[-1].index('(')+1:ins_lst[-1].index(')')]
        bin_res += '0'*(7-len(bin(REG.index(sr)))) + bin(REG.index(sr))[2:]
    elif ins_lst[1].upper() in REG:
        bin_res += '0'*(7-len(bin(REG.index(ins_lst[2])))) + bin(REG.index(ins_lst[2]))[2:]
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
    
#    print('Binary : ' + bin_res)
#    print('Hex : ' + hex(int(bin_res, 2)))
    hex_res = hex(int(bin_res, 2))[2:]
    fin_hex_res = '0'*(8-len(hex_res)) + hex_res

#   Big Endian Format
    for i in range(len(fin_hex_res)):
        print(' ' + fin_hex_res[i], end='') if i%2==0 else print(fin_hex_res[i], end='')

    print('\t---->\t', end='')

#   Little Endian Format
    le_format = fin_hex_res[::-1]
    ls = [x for x in le_format]
    for i in range(0, len(ls)-1, 2):
        ls[i], ls[i+1] = ls[i+1], ls[i]
    le_format = "".join([str(i) for i in ls])
    le_format = '0x' + le_format
    print(le_format)
