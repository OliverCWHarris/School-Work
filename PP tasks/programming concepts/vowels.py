word=str(input("Enter a word: "))
new_word=str

vowels=["a","e","i","o","u"]

for x in word:
    if x in vowels:
        new_word=word.replace(x,"")
print(word)
print(new_word)