#Megan Skrypek
#ms4985

import sys
from operator import itemgetter
import binascii

#handle user input
if len(sys.argv) != 5:
	print 'ERROR: not enough arguments'
	sys.exit()

try:
	n = int(sys.argv[1])
except:
	print 'ERROR: ngram length must be an integer'
	sys.exit()
try:
	slide = int(sys.argv[2])
except:
	print 'ERROR: sliding window length must be an integer'
	sys.exit()

infile = sys.argv[3]
outfile = sys.argv[4]

if slide > n:
	print 'ERROR: window cannot be larger than ngram length'
	sys.exit()

dict = {}
distinct = {}

#create dictionary with ngram frequencies
try:
	with open(infile, 'rb') as f:
		ngram = f.read(n)
		while ngram:
			try:
				dict[ngram] += 1
			except:
				dict[ngram] = 1
			old = ''
			i = slide
			while i<n:
				try:
					old += ngram[i]
				except:
					old += ''
				i += 1
			next = f.read(slide)
			ngram = old + next
			if len(ngram) < n:
				break
except:
	print 'ERROR: input file doesnt exist'
	sys.exit()

for ngram, freq in dict.items():
	if freq == 1:
		del dict[ngram]
		distinct[ngram] = 1

i=0
with open(outfile, 'wb') as f:
	for ngram, freq in sorted(dict.items(), key=itemgetter(1), reverse=True):
			if i < 20:
				f.write(binascii.hexlify(ngram) + ' ' + str(freq) + '\n')
			i += 1

		

