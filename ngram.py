#Megan Skrypek
#ms4985

import sys

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
except:
	print 'ERROR: input file doesnt exist'
	sys.exit()

for ngram in dict:
	print ngram, dict[ngram]

