#iterative version
def vowelsIter(string):
    listVowels='aeiou'
    numbVowels=0
    for i in string:
        for j in listVowels:
            if i == j:
                numbVowels +=1
    return numbVowels

#print(vowelsIter('educative'))

#recursive version
def vowelsRecu(string):
    if not string:
            return 0
    return (1 if string[0] in 'aeiouAEIOU' else 0) + vowelsRecu(string[1:])

string='educative'
print(vowelsRecu(string))
