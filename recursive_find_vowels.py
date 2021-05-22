#iterative version
def vowelsIter(string):
    listVowels='aeiou'
    numbVowels=0
    for i in string:
        for j in listVowels:
            if i == j:
                numbVowels +=1
    return numbVowels

print(vowelsIter('educative'))

#recursive version
def vowelsRecu(string,n,list):
    if n==1 and 


string='educative'
n=len(string)
listVowels='aeiou'
print(vowelsRecu(string,n,listVowels))
