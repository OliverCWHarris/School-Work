string=["apple", "banana", "cherry", "date"]
def filter_strings_containing_a(string):
    newstring=[]
    for i in range(0,len(string)):
        word=string[i]
        if 'a' in word:
            newstring.append(string[i])
    print(newstring)
filter_strings_containing_a(string)