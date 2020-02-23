""""This code is taken from The Programing Historian
by - William .J & Adam Crymble"""

wordstring = 'it was the best of times it was the wost of times'
wordstring += 'it was the age of wisdom it was the age of foolishness'

wordlist = wordstring.split()
#

# creating a fucntion to convert list wordfreq to dictionary
def wordlisttofrqdict(wordlist):
    wordfrq = [wordlist.count(w) for w in wordlist]
    return dict(list(zip(wordlist,wordfrq)))
print(wordlisttofrqdict(wordlist))
