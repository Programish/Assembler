import Registers
from Registers import REG

def formatter(ins_lst):
    bin_res = '0b'
    imm = ''
    
    if ins_lst[2].__contains__('x'):                    # Hex immediates
        if len(bin(int(ins_lst[2], 16))[2:]) > 20:
            raise ValueError("Immediate passed is out of range!!!! \n Enter value <= 0xfffff \n")
            return
        else:
            imm = bin(int(ins_lst[2], 16))[2:]
    elif ins_lst[2].__contains__('b'):                  # Bin immediates
        if len(ins_lst[2][2:]) > 20:
            raise ValueError("Immediate passed is out of range!!!! \n Enter value <= 0b11111111111111111111 \n")
            return
        else:
            imm = ins_lst[2][2:]
    elif type(ins_lst[2]) is int:                       # Int immediates
        if ins_lst[2] > 1048575:
            raise ValueError("Immediate passed is out of range!!!! \n Enter value <= 1048575 \n")
            return
        else:
            imm = bin(ins_lst[2])[2:]
    else:
        raise ValueError("Passed Immediate not allowed!!!! \n Only hex/bin/int values are allowed \n")
        return

    if len(imm) < 20:
       imm = '0'*(20-len(imm)) + imm 

    bin_res += imm[-20] + imm[-10:] + imm[-11] + imm[-19:-11] 

    if ins_lst[1].upper() in REG:
        bin_res += '0'*(7-len(bin(REG.index(ins_lst[1])))) + bin(REG.index(ins_lst[1]))[2:]
    else:
        raise ValueError("Given Register is unknown!!!!\n")
        return

    bin_res += '1101111'
   
    print('Binary : ' + bin_res)
    print('Hex : ' + hex(int(bin_res, 2)))
