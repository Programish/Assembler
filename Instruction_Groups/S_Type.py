import Registers
from Registers import REG

funct3 = {'SB':'000', 'SH':'001', 'SW':'010'}

def formatter(ins_lst):
    bin_res = '0b'
    imm = ''
    
    if ins_lst[3].__contains__('x'):                    # Hex immediates
        if len(bin(int(ins_lst[3], 16))[2:]) > 12:
            raise ValueError("Immediate passed is out of range!!!! \n Enter value <= 0xfff \n")
            return
        else:
            imm = bin(int(ins_lst[3], 16))[2:]
    elif ins_lst[3].__contains__('b'):                  # Bin immediates
        if len(ins_lst[3][2:]) > 12:
            raise ValueError("Immediate passed is out of range!!!! \n Enter value <= 0b111111111111 \n")
            return
        else:
            imm = ins_lst[3][2:]
    elif type(ins_lst[3]) is int:                       # Int immediates
        if ins_lst[3] > 4095:
            raise ValueError("Immediate passed is out of range!!!! \n Enter value <= 4095 \n")
            return
        else:
            imm = bin(ins_lst[3])[2:]
    else:
        raise ValueError("Passed Immediate not allowed!!!! \n Only hex/bin/int values are allowed \n")
        return

    bin_res += imm[-12:-5]

    if ins_lst[2].upper() in REG:
        bin_res += '0'*(7-len(bin(REG.index(ins_lst[2])))) + bin(REG.index(ins_lst[2]))[2:]
    else:
        raise ValueError("2nd Source Register is unknown!!!!\n")
        return
    
    if ins_lst[1].upper() in REG:
        bin_res += '0'*(7-len(bin(REG.index(ins_lst[1])))) + bin(REG.index(ins_lst[1]))[2:]
    else:
        raise ValueError("1st Source Register is unknown!!!!\n")
        return
    
    bin_res += funct3[ins_lst[0]]
    
    bin_res += imm[-5:]
    
    bin_res += '0100011'
    
    print('Binary : ' + bin_res)
    print('Hex : ' + hex(int(bin_res, 2)))
