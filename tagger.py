import nltk
from nltk.corpus import brown
from nltk.probability import ConditionalProbDist, ConditionalFreqDist, ELEProbDist, FreqDist
dictionary = {'अघ': ['sin', 'fault', 'offense']}

#fdist = FreqDist(word.lower() for (word, tag) in brown.tagged_words(tagset='universal'))
#print(fdist.B())

cfdist = ConditionalFreqDist((word.lower(), tag) for (word, tag) in brown.tagged_words(tagset='universal'))
'''
print(cfdist.conditions())
print(cfdist['sin'].freq('DET'))
print(cfdist['sin'].freq('X'))
print(cfdist['sin'].freq('VERB'))
print(cfdist['sin'].freq('NOUN'))
print(cfdist['sin'].freq('ADJ'))
print(cfdist['sin'].freq('ADP'))
print(cfdist['sin'].freq('.'))
print(cfdist['sin'].freq('CONJ'))
print(cfdist['sin'].freq('PRT'))
print(cfdist['sin'].freq('PRON'))
print(cfdist['sin'].freq('NUM'))
print(cfdist['sin'].freq('ADV'))
words = ['offence']
cfdist.tabulate(conditions=words)
'''


initial_pos_seed = {}

for key, value in dictionary.items():
    table = {'DET': 0, 'X': 0, 'VERB': 0, 'NOUN': 0, 'ADJ': 0, 'ADP': 0, '.': 0, 'CONJ': 0, 'PRT': 0, 'PRON': 0, 'NUM': 0, 'ADV': 0}
    tags = ['DET', 'X', 'VERB', 'NOUN', 'ADJ', 'ADP', '.', 'CONJ', 'PRT', 'PRON', 'NUM', 'ADV']
    for word in value:
        #To do: Phrase handling
        '''
        if len(word.split(" ")) > 1:
            phrase = word.split(" ")
        '''
        for tag in tags:
            table[tag] += cfdist[word].freq(tag)
    for k in table.keys():
        table[k] = table[k] / len(value)
    initial_pos_seed[key] = table

print(initial_pos_seed)




#modal = ['the', 'at']
#cfdist.tabulate(samples=modal)
#cpd = ConditionalProbDist(cfdist, ELEProbDist, fdist.B())
#print(cpd['the'].max())
#print(cpd['the'].prob())