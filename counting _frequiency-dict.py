""""This code is taken from The Programing Historian
by - William .J & Adam Crymble"""

wordstring = 'it was the best of times it was the wost of times'
wordstring += 'it was the age of wisdom it was the age of foolishness'

wordlist = wordstring.split()
#

# creating a fucntion to convert list wordfreq to dictionary
freqdict = {}
def wordlisttofrqdict(wordlist):
    wordfrq = [wordlist.count(w) for w in wordlist]
    freqdict.update(list(zip(wordlist,wordfrq)))
    return freqdict
print(wordlisttofrqdict(wordlist))
# print(freqdict)

# Sort a dictionary of word-frequency pairs in
# order of descending frequency.

def sortFreqDict(freqdict):
    aux = [(freqdict[key], key) for key in freqdict]
    aux.sort()
    aux.reverse()
    return aux
print(sortFreqDict(freqdict))
