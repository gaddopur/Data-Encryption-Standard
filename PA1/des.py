import random

'''I have did everything in 0-base indexing
but for block size of 64 i copied the permutation 
from book so they are in 1-base so i update them 
in zero base indexing'''

def generate_permutation(n:int):
    '''It generate the initial permutation 
    n denotes here block size'''
    if n == 64:
        perm = [ 58, 50, 42, 34, 26, 18, 10, 2, 
               60, 52, 44, 36, 28, 20, 12, 4, 
               62, 54, 46, 38, 30, 22, 14, 6, 
               64, 56, 48, 40, 32, 24, 16, 8, 
               57, 49, 41, 33, 25, 17, 9, 1, 
               59, 51, 43, 35, 27, 19, 11, 3, 
               61, 53, 45, 37, 29, 21, 13, 5, 
               63, 55, 47, 39, 31, 23, 15, 7 ]
        upd(perm)##converting in 0-base index
        return perm

    perm = [x for x in range(n)]
    random.shuffle(perm)
    return perm

def generate_half_permutation(n:int):
    '''It generate the permutation  here n
    denotes half width of block size'''
    if n == 32:
        perm = [ 16, 7, 20, 21, 
                 29, 12, 28, 17, 
                 1, 15, 23, 26, 
                 5, 18, 31, 10, 
                 2, 8, 24, 14, 
                 32, 27, 3, 9, 
                 19, 13, 30, 6, 
                 22, 11, 4, 25 ]
        upd(perm)##converting in 0-base index
        return perm

    perm = [x for x in range(n)]
    random.shuffle(perm)
    return perm

def generate_inv_permutation(n:int, perm):
    '''It generate the inverse of initial permutation''' 
    if n == 64:
        inv_perm = [ 40, 8, 48, 16, 56, 24, 64, 32, 
             39, 7, 47, 15, 55, 23, 63, 31, 
             38, 6, 46, 14, 54, 22, 62, 30, 
             37, 5, 45, 13, 53, 21, 61, 29, 
             36, 4, 44, 12, 52, 20, 60, 28, 
             35, 3, 43, 11, 51, 19, 59, 27, 
             34, 2, 42, 10, 50, 18, 58, 26, 
             33, 1, 41, 9, 49, 17, 57, 25 ]
        upd(inv_perm)##converting in 0-base index
        return inv_perm

    inv_perm = [x for x in range(n)]
    for i in range(n):
        inv_perm[perm[i]] = i
    return inv_perm

def generate_expansion_permutation(n:int, m:int): 
    ## n denotes expansion permutation length
    ## m denotes half of blocksize
    '''It genereate the expansion permutation 
    which required in for expansion of the hlaf of the message''' 
    if m == 32:
        exp_perm = [ 32, 1, 2, 3, 4, 5,
             4, 5, 6, 7, 8, 9, 
             8, 9, 10, 11, 12, 13, 
             12, 13, 14, 15, 16, 17, 
             16, 17, 18, 19, 20, 21, 
             20, 21, 22, 23, 24, 25,
             24, 25, 26, 27, 28, 29,
             28, 29, 30, 31, 32, 1 ] 
        upd(exp_perm)##converting in 0-base index
        return exp_perm

    exp_perm = [0]*n
    perm = [i for i in range(m)]
    random.shuffle(perm)
    for i in range(n):
        exp_perm[i] = perm[i%m]
    random.shuffle(exp_perm)
    return exp_perm

def generate_pc1_permutation(n):
    ''' It generates the PC1 which is known 
    as permutated choice one is required for 
    key generation'''
    if n == 64:
        PC1 = [ 57, 49, 41, 33, 25, 17, 9, 
             1, 58, 50, 42, 34, 26, 18, 
             10, 2, 59, 51, 43, 35, 27, 
             19, 11, 3, 60, 52, 44, 36, 
             63, 55, 47, 39, 31, 23, 15, 
             7, 62, 54, 46, 38, 30, 22, 
             14, 6, 61, 53, 45, 37, 29, 
             21, 13, 5, 28, 20, 12, 4 ]
        upd(PC1)##converting in 0-base index
        return PC1
    x = [i for i in range(n)]
    random.shuffle(x)
    perm = []
    for i in range(n):
        if (i+1)%8 != 0:
            perm.append(x[i])
    return perm

def generate_pc2_permutation(n):
    ''' It generates the PC1 which is known 
    as permutated choice one is required for 
    key generation'''
    if n == 56:
        PC2 = [ 14, 17, 11, 24, 1, 5, 
             3, 28, 15, 6, 21, 10, 
             23, 19, 12, 4, 26, 8, 
             16, 7, 27, 20, 13, 2, 
             41, 52, 31, 37, 47, 55, 
             30, 40, 51, 45, 33, 48, 
             44, 49, 39, 56, 34, 53, 
             46, 42, 50, 36, 29, 32 ]
        upd(PC2)
        return PC2

    x = [i for i in range(n)]
    random.shuffle(x)
    perm = []
    for i in range(n):
        if (i+1)%7 != 0:
            perm.append(x[i])
    return perm

def upd(perm):
    '''I did everything with 0-base indexing 
    but for 64 block size i copied all the permutation from 
    book which is 1-base indexing so need to decreas by one
    so it take a permutation decrease there value'''
    for i in range(len(perm)):
        perm[i] -= 1

def permutaion(msg:str, perm):
    '''It permuates the given string with help of given of permutation 
    and return permutated string, returned string size depend 
    on the size of given permutation '''  
    per_msg = []
    for i in range(len(perm)):
        per_msg.append(msg[perm[i]])
    return "".join(per_msg)

def leftshift(msg, k):
    '''it just to left shift with given k'''
    return msg[k:] + msg[:k]

def xor(msg1, msg2):
    '''it just return xor two binary message'''
    x = []
    for i in range(len(msg1)):
        if msg1[i] == msg2[i]:
            x.append('0')
        else: x.append('1')
    return "".join(x)

def S_box(msg, s):
    '''Compressed the message with the help of s box''' 
    new_msg = []
    num = 0
    assert len(msg)%6 == 0, print("length of message must be divisible by 6")
    for i in range(0, len(msg), 6):
        cur = msg[i:i+6]
        r = int(cur[0]+cur[5], 2)
        c = int(cur[1:5], 2)
        new_msg.append(str(bin(s[num][r][c])[2:].rjust(4, '0')))
        num += 1
        num %= 8

    return "".join(new_msg)

def diff_bit(txt: str, hamming_dist: int) -> str:
    '''takes one binary string and return a string such that 
    the hamming distance between returned string and given string is hamming_dist'''
    ## getting the length of txt.
    length = len(txt) 
    
    ## slecting "hamming dist" numbers from 0 to length-1 randomly.
    random_pos = random.sample(range(0,length),hamming_dist) 
    
    random_pos.sort() ## just sort position in increasing order
    diff_txt = "" ## for storing the changed txt.
    i = 0
    for pos in random_pos:
        ## copying the text which we don't need to change
        diff_txt += txt[i:pos] 
        i = pos+1
        if(txt[pos] == '1'):
            diff_txt += '0'
        else:
            diff_txt += '1'
  
    diff_txt += txt[i:]
    return diff_txt

def preprocess_key(key: str, halfwidth:int =32, hamming_dist:int =0) -> str:
    ''' It preprocess the key so that size key become
    size of block cipher if the key size is greater 
    remove then have ignored last unused value and if size is smaller
    then added zero in starting'''
    if(len(key) > 2*halfwidth):
        key = key[:2*halfwidth]
    key = key.zfill(2*halfwidth)

    if(hamming_dist != 0):
        key = diff_bit(key,hamming_dist)

    return key

def Weak_key_demonstration(key, num_rounds, block_size):
    ''' this return a list of keys after every round
    in key generation '''
    PC1 = generate_pc1_permutation(block_size)
    PC2 = generate_pc2_permutation(len(PC1))
    key = permutaion(key, PC1)
    keys = []
    L_key = key[:len(key)//2]
    R_key = key[len(key)//2:]
    for i in range(num_rounds):
        L_key = leftshift(L_key, 1)
        R_key = leftshift(R_key, 1)

        cur_key = permutaion((L_key+R_key), PC2)
        keys.append(cur_key)
    return keys

def encrypt(msg, perm, inv_perm, exp_perm, key, PC1, PC2, half_perm, s_boxes, num_rounds):
    ''' does encyption as DES algorithm work'''
    half = len(half_perm)

    msg = permutaion(msg, perm)
    L_msg = msg[0:half]
    R_msg = msg[half:]

    key = permutaion(key, PC1)
    L_key = key[:len(key)//2]
    R_key = key[len(key)//2:]

    msg = []

    for i in range(num_rounds):
        newL_msg = R_msg
        R_msg = permutaion(R_msg, exp_perm)

        L_key = leftshift(L_key, 1)
        R_key = leftshift(R_key, 1)

        cur_key = permutaion((L_key+R_key), PC2)
        assert len(cur_key) == len(R_msg), print("lenght of current key and R_msg should be equal")
        R_msg = xor(cur_key, R_msg)
        R_msg = S_box(R_msg, s_boxes)
        R_msg = permutaion(R_msg, half_perm)
        R_msg = xor(R_msg, L_msg)
        L_msg = newL_msg
        if i != num_rounds-1:
            msg.append(L_msg+R_msg)

    L_msg, R_msg = R_msg, L_msg
    msg.append(permutaion(L_msg+R_msg, inv_perm))
    return msg


def txt_bin(s:str):
    '''It convert message to binary form'''
    bin_msg = []
    for c in s:
        bin_msg.append(str(bin(ord(c)))[2:].rjust(8, '0'))
    return "".join(bin_msg)

def bin_txt(msg):
    '''It conver binary string to normal message'''
    enc_msg = []
    for i in range(0, len(msg), 8):
        ascii_val = int(msg[i:i+8], 2)
        ch = chr(ascii_val)
        enc_msg.append(ch)
    return "".join(enc_msg)

def preprocess(s, half, block_size, num_rounds, key):
    '''It took the plaintext, block size, number of rounds
    and the key and returned the encrypted message
    How I did?
    Ans: first have converted the given string into binary from 
    and then make sure that size of message in binary form is 
    multiple of block size if not added some zero in front.
    then make 8 s box and stored in s_boxes if more s boxes needed then 
    I took in circular form mean after 8th box took 1 box
    then store initial permutataion(perm), final permutation(inv_permutation)
    PC1, PC2, expansion permutation(exp_perm), and half permutation
    After that have broke the message of length block size for each message of block size 
    called an encrypted function which encrypt the given the message'''
    bin_msg = txt_bin(s)
    mul = (len(bin_msg)+block_size-1)//block_size*block_size
    bin_msg = bin_msg.rjust(mul, '0')

    s_boxes = [
       [ 
         [ 14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7], 
         [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8], 
         [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0], 
         [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
       ], 
       [ 
         [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10], 
         [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
         [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
         [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
       ], 
       [ 
         [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
         [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
         [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
         [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12 ]
       ],
       [ 
         [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15], 
         [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
         [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4], 
         [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14 ]
       ], 
       [ 
         [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
         [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
         [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
         [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3 ]
       ],
       [ 
         [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11], 
         [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8], 
         [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
         [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13 ]
       ], 
       [ 
         [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
         [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
         [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
         [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12 ]
       ],
       [ 
         [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7], 
         [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
         [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
         [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11] 
       ]
   ]    
   
    perm = generate_permutation(block_size)
    inv_perm = generate_inv_permutation(block_size, perm)
    PC1 = generate_pc1_permutation(block_size)
    PC2 = generate_pc2_permutation(len(PC1))
    exp_perm = generate_expansion_permutation(len(PC2), half)
    half_perm = generate_half_permutation(half)

    enc_msg = [""]*num_rounds
    for i in range(0, len(bin_msg), block_size):
        rounds_msg = encrypt(bin_msg[i:i+block_size], perm, inv_perm, exp_perm, key, PC1, PC2, half_perm, s_boxes, num_rounds)
        for i in range(num_rounds):
            enc_msg[i] += rounds_msg[i]
    
    return enc_msg

def bin_hex(msg):
    '''It takes a string in binary form and convert 
    it into hexa decimal form'''
    hex = []
    for i in range(0, len(msg), 8):
        ascii_val = int(msg[i:i+8], 2)
        hex.append("%x"%ascii_val)
    return "".join(hex)

def init(msg, block_size, num_rounds, key):
    '''It just for calculating the half size of block
    and return the encrypted message'''
    print(msg, block_size, num_rounds)
    half = block_size//2
    return preprocess(msg, half, block_size, num_rounds, key)
    

if __name__ == "__main__":
    '''no use in the project just for checking'''
    half = 32
    block_size = half*2
    num_rounds = 16
    key = "".rjust(block_size, '0')
    enc_msg = preprocess("[%Ú:A", half, block_size, num_rounds, key)
    print(enc_msg)
    print(bin_txt(enc_msg))
    # one_bit_diff("aman")