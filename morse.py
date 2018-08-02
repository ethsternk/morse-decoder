def decodeBits(bits):

    bit_list_1s = []
    bit_list_0s = []
    group = []
    latest = bits.strip('0')[0]
    for bit in bits.strip('0'):
        if bit == latest:
            group.append(bit)
        else:
            latest = bit
            if bit == '1':
                bit_list_0s.append(len(group))
            if bit == '0':
                bit_list_1s.append(len(group))
            group = [bit]
    if group[-1] == '1':
        bit_list_0s.append(len(group))
    if group[-1] == '0':
        bit_list_1s.append(len(group))
    
    if bit_list_0s and bit_list_1s:
        length = min([min(bit_list_0s), min(bit_list_1s)])
    elif bit_list_0s:
        length = min(bit_list_0s)
    else:
        length = min(bit_list_1s)
    
    return bits.strip('0').replace('0000000' * length, '   ').replace('000' * length, ' ').replace('111' * length, '-').replace('1' * length, '.').replace('0' * length, '')

def decodeMorse(morseCode):
    decoded = []
    for letter in morseCode.strip().replace('   ', ' & ').split(' '):
        if letter == '&':
            decoded.append(' ')
        else:
            decoded.append(MORSE_CODE[letter])
    return ''.join(decoded)