'''
    By-Lalita Sharma
    Exp3:CRC
'''
def xor(a, b): 
    xor = [] 
    # Traverse all bits, if bits are same, then XOR is 0, else 1 
    # starting from 1 beacuse we are here in xor only if first bit is 1
    for i in range(1, len(b)): 
        if a[i] == b[i]: 
            xor.append('0') 
        else: 
            xor.append('1')
    result=''.join(xor) 
    return result
# *******************************************************************************
def mod2div(divident, divisor): 
    # Number of bits to be XORed at a time. 
    leng = len(divisor) 
    # Slicing the divident to appropriate length for particular step 
    tmp = divident[0 : leng] 
  
    while leng < len(divident): 
  
        if tmp[0] == '1': 
  
            # replace the divident by the result of XOR and pull 1 bit down 
            tmp = xor(divisor, tmp) + divident[leng] 
  
        else:   
            # If leftmost bit is '0'  If the leftmost bit of the dividend (or the part used in each step) is 0, the step cannot 
            # use the regular divisor; we need to use an  all-0s divisor. 
            tmp = xor('0'*leng, tmp) + divident[leng] 
  
        # increment length to move further 
        leng += 1
  
    # For the last n bits, we have to carry it out normally as increased value of pick will cause Index Out of Bounds. 
    if tmp[0] == '1': 
        tmp = xor(divisor, tmp) 
    else: 
        tmp = xor('0'*leng, tmp) 
    checkword = tmp 
    return checkword 
# *******************************************************************************
def RoughCRCcode(msg,generatorpolynomial):
    toaddbits='0' *(len(generatorpolynomial)-1)
    return msg+toaddbits
# *******************************************************************************
def CRCcode(msg,generatorpolynomial,roughCRCcode):
    data=msg # copy original msg i.e without crc wala in data
    remainder = mod2div(roughCRCcode, generatorpolynomial) 
  
    # Append remainder in the original data 
    finaldata = data + remainder 
    print("Remainder : ", remainder) 
    print("Encoded Data (Data + Remainder) : ", 
          finaldata)
    return finaldata 
# *******************************************************************************
def CRCreceiver(dataR,generatorpolynomial):
    remainder = mod2div(dataR, generatorpolynomial) 
    print("Remainder at receiver=",remainder)
    if remainder=='0'*(len(generatorpolynomial)-1):
        print("No error")
    else:
        print("Error!!!!")
# *******************************************************************************

if __name__ == "__main__":
    i=1
    while(i==1):
        msglength=int(input("Enter the data length\n"))
        msg=input("Enter the data\n")
        generatorpolynomial=input("Enter generator polynomial\n")
        roughCRCcode=RoughCRCcode(msg,generatorpolynomial)
        print("Rough crc code= {}\n".format(roughCRCcode))
        finalcrc=CRCcode(msg,generatorpolynomial,roughCRCcode)
        print("Final CRC= ",finalcrc)
        dataR=input('Enter data at receiver side:\n')
        CRCreceiver(dataR,generatorpolynomial)

        i=int(input("Do you want to continue??(enter 1 for yes)\n"))
        if i!=1:
            print("Terminating.....\n\n")