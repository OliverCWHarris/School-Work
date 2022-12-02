amex=['34','37']
mastercard=['51','52','53','54','55']
visa=['4']
discover=['6011']

card=str(input('Enter your card number\n>'))
card_list=list(card)

if len(card_list)==15:

    amex_bits=card_list[0:2]
    amex_check=''.join(amex_bits)

    if amex_check in amex:
        print('Card',card,'is American Express')

elif len(card_list)==16:

    master_bits=card_list[0:2]
    master_check=''.join(master_bits)

    visa_bits=card_list[0]
    visa_check=''.join(visa_bits)

    discover_bits=card_list[0:4]
    discover_check=''.join(discover_bits)

    if master_check in mastercard:
        print('Card',card,'is Mastercard')

    elif visa_check in visa:
        print('Card',card,'is Visa')

    elif discover_check in discover:
        print('Card',card,'is Discover')
    
    else:
        print('Invalid card type or number')

'''
valid amex 344365782031837
valid mastercard 5419084384955488
valid visa 4562675006703228
valid discover 6011236224304596
'''