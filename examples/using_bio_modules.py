'''
	This short program will count how many times the oligo sequences occurs in the fasta file.
'''

import sys
import my_bio_module as mb

if len(sys.argv) != 3:
	sys.exit("ERROR: the program should be run as follows (an example): ./using_bio_modules.py regions.fna 'gccat'!")
else:
	pass

with open (sys.argv[1], 'r') as fin:
	oligo = sys.argv[2]
	no_oligo = 0
	for line in fin:
		if not line.startswith('>'):
			reverse_complement = mb.rev_complement(line)
			no_oligo += mb.oligo_match(line, oligo)
			no_oligo += mb.oligo_match(reverse_complement, oligo)
	print(f"A total match of {no_oligo} is found for {oligo} in the sequences of file {sys.argv[1]}")
