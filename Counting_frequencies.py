""""This code is taken from The Programing Historian
by - William .J & Adam Crymble"""


# count-list-items

wordstring = 'it was the best of times it was the wost of times'
wordstring += 'it was the age of wisdom it was the age of foolishness'

wordlist = wordstring.split()

wordfreq = []
for w in wordlist:
    wordfreq.append(wordlist.count(w))
# print(wordfreq)

print("string\n" + wordstring + '\n')
print('list\n' + str(wordlist) + '\n')
print('frqquincies\n ' + str(wordfreq) + '\n')
print('pairs ' + str(list(zip(wordlist,wordfreq))))
