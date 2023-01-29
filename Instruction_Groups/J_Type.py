import Registers
from Registers import REG

def formatter(ins_lst):
    bin_res = '0b'
    fin_bin_no = ''

    if len(ins_lst) == 2 and ins_lst[0] == 'J':                          # Pseudoinstrunctions
        ins_lst.insert(1, 'A0')
        ins_lst[0] == 'JAL'
    elif len(ins_lst) == 2 and ins_lst[0] == 'JAL':
        ins_lst.insert(1, 'A1')

    if ins_lst[-1].__contains__('X'):                                    # Hex immediates
        if len(bin(int(ins_lst[-1], 16))[2:]) > 20:
            raise ValueError("Immediate passed is out of range!!!! \n Enter value <= 0xfffff \n")
            return
        else:
            bin_no = bin(int(ins_lst[-1], 16))[2:]
            fin_bin_no = '0'*(20-len(bin_no)) + bin_no
    elif ins_lst[-1].__contains__('B'):                                  # Bin immediates
        if len(ins_lst[-1][2:]) > 20:
            raise ValueError("Immediate passed is out of range!!!! \n Enter value <= 0b11111111111111111111 \n")
            return
        else:
            bin_no = ins_lst[-1][2:]
            fin_bin_no = '0'*(20-len(bin_no)) + bin_no
    elif ins_lst[-1].isnumeric():                                        # Positive Int immediates
        if ins_lst[-1] > 1048575:
            raise ValueError("Immediate passed is out of range!!!! \n Enter value <= 1048575 \n")
            return
        else:
            bin_no = bin(int(ins_lst[-1]))[2:]
            fin_bin_no = '0'*(20-len(bin_no)) + bin_no
    elif ins_lst[-1][1:].isnumeric() and ins_lst[-1][0] is '-':          # Negative Int immediates
        if int(ins_lst[-1][1:]) > 1048574:
            raise ValueError("Immediate passed is out of range!!!! \n Enter value >= -1048574 \n")
            return
        else:
            bin_no = bin(int(ins_lst[-1][1:]))[2:]
            fin_bin_no = '0' * (20-len(bin_no)) + bin_no
            #Flipping the bits of original number
            flipped_bits = ''.join(['1' if i == '0' else '0' for i in fin_bin_no])
            #Adding 1 to flipped bits, to get 2's complement of the negative immediate passed
            fin_bin_no = bin(int(flipped_bits, 2) + int('1', 2))
    else:
        raise ValueError("Passed Immediate not allowed!!!! \n Only hex/bin/int values are allowed \n")
        return

    bin_res += fin_bin_no[-20] + fin_bin_no[-10:] + fin_bin_no[-11] + fin_bin_no[-19:-11] 

    if ins_lst[1].upper() in REG:
        bin_res += '0'*(7-len(bin(REG.index(ins_lst[1])))) + bin(REG.index(ins_lst[1]))[2:]
    else:
        raise ValueError("Given Register is unknown!!!!\n")
        return

    bin_res += '1101111'
   
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
