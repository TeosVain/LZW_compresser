import sys


ALPHABET = ' etaoinshrdlucmfwypvbgkjqxz.,!?-'
ALPHABET_CODE = {ch: i+1 for i, ch in enumerate(ALPHABET)}
INVERS_ALPHABET_CODE = {i+1: ch for i, ch in enumerate(ALPHABET)}


def pack(string):
    '''Text packing function using LZW algorithm.'''
    word_dict = {'': 0}
    prev_word = 0
    current_word = ''
    code_list = []
    cur = 1
    for char in string:
        current_word += char
        if current_word in word_dict:
            prev_word = word_dict[current_word]
        else:
            if cur < 2**11:
                word_dict[current_word] = cur
                cur += 1
            code_list.append((prev_word, char))
            current_word = ''
            prev_word = 0
    if current_word != '':
        last_value = word_dict.get(current_word)
        code_list.append((last_value, None))
    return code_list


def unpack(uncode_byte_list):
    '''Text unpacking function using LZW algorithm.'''
    dict_words = {0: ''}
    current_word = ''
    cur = 1
    final_string = ''
    for element in uncode_byte_list:
        if element[1] is not None:
            current_word = dict_words[element[0]] + element[1]
        else:
            current_word = dict_words[element[0]]
        final_string += current_word
        dict_words[cur] = current_word
        cur += 1
        current_word = ''
    return final_string


def code_to_bytes(list_code):
    '''
    Function that packs LZW-compressed data into bytes.
        - 11 bits are used for number encoding.
        - 5 bits for character or letter encoding.
    '''
    ans_list = [0] * (2*len(list_code))
    cur = 0
    for element in list_code:
        if element[1] is not None:
            code_letter = ALPHABET_CODE[element[1]]
        else:
            code_letter = 0
        final_bit = (element[0] << 5) | code_letter
        first_byte = (final_bit >> 8) & 0xFF
        second_byte = final_bit & 0xFF
        ans_list[cur] = first_byte
        cur += 1
        ans_list[cur] = second_byte
        cur += 1

    return ans_list


def bytes_to_code(list_bytes):
    '''Function decoding pairs of bytes into LZW sequence.'''
    code_list = [0] * (len(list_bytes) // 2)
    cur = 0
    for i in range(0, len(list_bytes), 2):
        full_16_bit = (list_bytes[i] << 8) | list_bytes[i+1]
        number = (full_16_bit >> 5) & 0x7FF
        letter_code = full_16_bit & 0x1F

        if letter_code == 0:
            letter = None
        else:
            letter = INVERS_ALPHABET_CODE[letter_code]

        code_list[cur] = (number, letter)
        cur += 1
    return code_list


'''
This code expects the command "pack" as input
and on the next line the English text to be compressed.
Or command "unpack" and sequence of bytes to unpack text.
'''
com = input()

if com == 'pack':
    string = input()
    packed = pack(string)
    bts = code_to_bytes(packed)

    sys.stdout.write(str(len(bts)) + '\n')
    sys.stdout.write(' '.join(map(str, bts)) + '\n')
else:
    bts = list(map(int, input().split()))
    decoded = unpack(bytes_to_code(bts))

    sys.stdout.write(decoded + '\n')

sys.stdout.flush()
