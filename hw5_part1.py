"""
File:         hw5_part1.py
Author:       Vu Nguyen
Date:         10/16/2020
Section:      31
E-mail:       vnguye12@umbc.edu
Description:
"""
import sys
from random import choice, seed

if len(sys.argv) >= 2:
    seed(sys.argv[1])

# These are the constants
STOP_PARAM = 'stop'
SEQ_PARAM = 'seq'
NUCLEOTIDES = ['A', 'T', 'C', 'G']
START = ['ATG']
STOP = ['TAA', 'TGA', 'TAG']
CODON_LENGTH = 3


def extract_genes(sequence):
    temporary_codon = ''
    temp_stop = ''
    new_sequence_list = []

    # This loop create a new sequence list
    for index in range(0, len(sequence), CODON_LENGTH):
        temporary_codon += sequence[index:index + CODON_LENGTH]

        # This if statement check for the STOP codon.
        if (temporary_codon in STOP and new_sequence_list) and not temp_stop:
            temp_stop += temporary_codon
            new_sequence_list.append(temp_stop)
            temporary_codon = ''

        # This elif check for the start codon.
        elif (temporary_codon in START and not temp_stop) or (not temp_stop and new_sequence_list):
            new_sequence_list.append(temporary_codon)
            temporary_codon = ''
        else:
            temporary_codon = ''

    list_of_genes = []
    codon_string = ''

    if temp_stop:
        # This loop extract the genes out of the sequence list.
        for index_codon in range(len(new_sequence_list)):
            if new_sequence_list[index_codon] in START:
                codon_string = ''.join(new_sequence_list[index_codon:])
                list_of_genes.append(codon_string)

    return list_of_genes


if __name__ == '__main__':
    length_or_stop = input("How many codons do you want to create? (stop to end, seq to create your own sequence) ")
    while length_or_stop.lower() != STOP_PARAM:
        try:
            if length_or_stop.lower() == SEQ_PARAM:
                the_sequence = input('Enter your own sequence: ').upper()
                if len(the_sequence) % 3 != 0:
                    raise ValueError('The length of the string must be divisible by 3')
                if any(x not in NUCLEOTIDES for x in the_sequence):
                    raise ValueError('The sequence must contain only A, T, C, G')
            else:
                the_sequence = ''.join([choice(NUCLEOTIDES) for _ in range(3 * int(length_or_stop))])
            print(the_sequence)
            print(extract_genes(the_sequence))
        except ValueError:
            print('You entered a non-STOP non-integer, try again. ')
        length_or_stop = input("How many codons do you want to create? (stop to end, seq to create your own sequence) ")












