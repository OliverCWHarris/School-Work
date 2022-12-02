def char_to_code(ascii_char):
    ascii_val=ord(ascii_char)
    return ascii_val

def code_to_char(ascii_val):
    ascii_code=chr(ascii_val)
    return ascii_code

while True:
    try:
        choice=int(input('1 for char to code, 2 for code to char\n>'))

        if choice==1:
            ascii_char=str(input('Enter and ASCII character\n>'))
            print(ascii_char,'in code is',char_to_code(ascii_char))
            break
        elif choice==2:
            ascii_val=int(input('Enter an ASCII value\n>'))
            print(ascii_val,'as a character is',code_to_char(ascii_val))
            break
    
    except ValueError:
        print('Please enter a valid choice')