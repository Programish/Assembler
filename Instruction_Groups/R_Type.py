import Registers
from Registers import REG

funct3 = {'SLLI':'001', 'SRLI':'101', 'SRAI':'101', 'ADD':'000', 'SUB':'000', 'SLL':'001','SLT':'010',
          'SLTU':'011', 'XOR':'100', 'SRL':'101', 'SRA':'101', 'OR':'110', 'AND':'111'} 

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
                raise ValueError("Shift amount passed is out of range!!!! \n Enter value <= 0x19 \n")
                return
            else:
                bin_no = bin(int(ins_lst[3], 16))[2:]
                fin_bin_no = '0' * (5-len(bin_no)) + bin_no
                bin_res += fin_bin_no
        elif ins_lst[3].__contains__('b'):                  # Bin immediates
            if len(ins_lst[3][2:]) > 5:
                raise ValueError("Shift amount passed is out of range!!!! \n Enter value <= 0b11111 \n")
                return
            else:
                bin_no = ins_lst[3][2:]
                fin_bin_no = '0' * (5-len(bin_no)) + bin_no
                bin_res += fin_bin_no 
        elif type(ins_lst[3]) is int:                       # Int immediates
            if ins_lst[3] > 31:
                raise ValueError("Shift amount passed is out of range!!!! \n Enter value <= 31 \n")
                return
            else:
                bin_no = bin(int(ins_lst[3]))[2:]
                fin_bin_no = '0' * (12-len(bin_no)) + bin_no
                bin_res += fin_bin_no 
        else:
            raise ValueError("Passed Shift amount not allowed!!!! \n Only hex/bin/int values are allowed \n")
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
