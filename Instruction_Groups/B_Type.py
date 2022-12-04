import Registers
from Registers import REG

funct3 = {'BEQ':'000', 'BNE':'001', 'BLT':'100',
          'BGE':'101', 'BLTU':'110', 'BGEU':'111'} 

def formatter(ins_lst):
    bin_res = '0b'
    imm = ''
    
    if ins_lst[-1].__contains__('X'):                                # Hex immediates
        if len(bin(int(ins_lst[-1], 16))[2:]) > 12:
            raise ValueError("Immediate passed is out of range!!!! \n Enter value <= 0xfff \n")
            return
        else:
            bin_no = bin(int(ins_lst[-1], 16))[2:]
            fin_bin_no = '0' * (12-len(bin_no)) + bin_no
    elif ins_lst[-1].__contains__('B'):                              # Bin immediates
        if len(ins_lst[-1][2:]) > 12:
            raise ValueError("Immediate passed is out of range!!!! \n Enter value <= 0b111111111111 \n")
            return
        else:
            bin_no = ins_lst[-1][2:]
            fin_bin_no = '0' * (12-len(bin_no)) + bin_no
    elif ins_lst[-1].isnumeric():                                    # Positive Int immediates
        if int(ins_lst[-1]) > 4095:
            raise ValueError("Immediate passed is out of range!!!! \n Enter value <= 4095 \n")
            return
        else:
            bin_no = bin(int(ins_lst[-1]))[2:]
            fin_bin_no = '0' * (12-len(bin_no)) + bin_no
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
            fin_bin_no = bin(int(flipped_bits, 2) + int('1', 2))
    else:
        raise ValueError("Passed Immediate not allowed!!!! \n Only hex/bin/int values are allowed \n")
        return

    imm = fin_bin_no[-12] + fin_bin_no[-10:] + fin_bin_no[-11]
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
    
    bin_res += '1100011'
    
    print('Binary : ' + bin_res)
    print('Hex : ' + hex(int(bin_res, 2)))
