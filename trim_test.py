opcode = {'AND':'0000', 'EOR':'0001', 'SUB':'0010', 'RSB':'0011', 'ADD':'0100', 'ADC':'0101', 
          'SBC':'0110', 'RSC':'0111', 'TST':'1000', 'TEQ':'1001', 'CMP':'1010', 'CMN':'1011', 
          'ORR':'1100', 'MOV':'1101', 'BIC':'1110', 'MVN':'1111'}

s = ''
while(s is not 'y'):
    s = input()
    ls = s.replace(",", "").split()
    flag = "1" if (ls[0][-1] in ("S", "s")) else "0"
    print("           OpCode : " + ls[0] + "    " + opcode[ls[0]])
    print("               Rd : " + ls[1])
    print("               Rn : " + ls[2])
    print("  shifter operand : " + ls[3])
    print("      status flag : " + flag)
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    s = input("Want to quit?(y/n)")
