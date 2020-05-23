ENCRYPTION_DICT = {
    'A': 'T',
    'B': 'H',
    'C': 'E',
    'D': 'Q',
    'E': 'U',
    'F': 'I',
    'G': 'C',
    'H': 'K',
    'I': 'B',
    'J': 'R',
    'K': 'O',
    'L': 'W',
    'M': 'N',
    'N': 'F',
    'O': 'X',
    'P': 'J',
    'Q': 'M',
    'R': 'P',
    'S': 'S',
    'T': 'V',
    'U': 'A',
    'V': 'L',
    'W': 'Z',
    'X': 'Y',
    'Y': 'D',
    'Z': 'G'
}


def encrypt(plaintext):
    """
    Takes in plaintext as an input and returns 'ciphertext': the result 
    of substituting each letter in the plaintext by its corresponding 
    encrypted character in ENCRYPTION_DICT. 

    The plaintext comprises entirely of uppercase letters and non-alphabetic 
    characters like punctuation. Non-alphabetic characters needn't be encrypted, 
    but rather should appear in the plaintext in their original form. 

    >>> encrypt("HEY, HOW'S IT GOING?")
    "KUD, KXZ'S BV CXBFC?"
    >>> encrypt("I LOVE CS 106A!")
    'B WXLU ES 106T!'
    >>> encrypt("UNICORNS ARE THE MOST BEAUTIFUL ANIMALS IN EXISTENCE")
    'AFBEXPFS TPU VKU NXSV HUTAVBIAW TFBNTWS BF UYBSVUFEU'
    """
    ciphertext = ''
    for i in range(len(plaintext)):
        if plaintext[i] not in ENCRYPTION_DICT:
            ciphertext += plaintext[i]
        else:
            i_cipher = ENCRYPTION_DICT.get(plaintext[i])
            ciphertext += i_cipher
    return ciphertext

def decrypt(ciphertext):
    """
    Uses ENCRYPTION_DICT to decrypt each of the alphabetic characters of
    ciphertext.

    >>> decrypt("KUD, KXZ'S BV CXBFC?")
    "HEY, HOW'S IT GOING?"
    >>> decrypt('B WXLU ES 106T!')
    'I LOVE CS 106A!'
    >>> decrypt('AFBEXPFS TPU VKU NXSV HUTAVBIAW TFBNTWS BF UYBSVUFEU')
    'UNICORNS ARE THE MOST BEAUTIFUL ANIMALS IN EXISTENCE'
    """
    decrypt_dic = {}
    for key in ENCRYPTION_DICT:
        temp = ENCRYPTION_DICT[key]
        decrypt_dic[temp] = key


    plaintext = ''
    for i in range(len(ciphertext)):
        if ciphertext[i] not in decrypt_dic:
            plaintext += ciphertext[i]
        else:
            i_cipher = decrypt_dic.get(ciphertext[i])
            plaintext += i_cipher
    return plaintext
