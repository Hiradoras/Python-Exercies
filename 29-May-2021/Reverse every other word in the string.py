'''
Reverse every other word in a given string, then return the string.
Throw away any leading or trailing whitespace, while ensuring there
is exactly one space between each word. Punctuation marks should be
treated as if they are a part of the word in this kata.
'''

def reverse_alternate(string):
    words = string.split()
    new_words = []
    for i in range(0,len(words)):
        if i % 2 == 0:
            new_words.append(words[i])
        else:
            word = words[i]
            new_words.append(word[::-1])
    return " ".join(new_words)

print(reverse_alternate("Did it work?"))

############# Or ###############

def shorter_reverse_alternative(string):
    return " ".join([element[::-1] if i % 2 else element for i,element in enumerate(string.split())])

print(shorter_reverse_alternative("Did it work?"))

### Same function but smarter and shorted with enumerate() method.