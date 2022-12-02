letter_num={
    'a':0,
    'b':1,
    'c':2,
    'd':3,
    'e':4,
    'f':5,
    'g':6,
    'h':7,
    'i':8,
    'j':9,
    'k':10,
    'l':11,
    'm':12,
    'n':13,
    'o':14,
    'p':15,
    'q':16,
    'r':17,
    's':18,
    't':19,
    'u':20,
    'v':21,
    'w':22,
    'x':23,
    'y':24,
    'z':25,
}

num_letter={
    0:'a',
    1:'b',
    2:'c',
    3:'d',
    4:'e',
    5:'f',
    6:'g',
    7:'h',
    8:'i',
    9:'j',
    10:'k',
    11:'l',
    12:'m',
    13:'n',
    14:'o',
    15:'p',
    16:'q',
    17:'r',
    18:'s',
    19:'t',
    20:'u',
    21:'v',
    22:'w',
    23:'x',
    24:'y',
    25:'z',
}

decoded_str=[]

def decode(inpute,b,nota):
    Cn=(letter_num[inpute])
    inter_step=Cn-b
    inter_step=inter_step*nota
    Pn=inter_step%26
    output=(num_letter[Pn])
    decoded_str.append(output)
    return output

input_str=str(input('Enter entire encoded string\n>'))
b=int(input('Enter value of b\n>'))
nota=int(input('Enter value of nota\n>'))
count=1

try:
    for x in range (0,len(input_str)):
        count_str=count
        print('Enter letter number',count_str,'of encoded string')
        inpute=str(input('Enter here:'))
        printer=decode(inpute,b,nota)
        print(printer)
        count=count+1
    print(input_str,'decoded is',''.join(decoded_str))
except ValueError:
    print('done goof')