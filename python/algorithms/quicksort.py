"""
This file contains a implementation of the 'Quicksort' algorithm.
"""
import sys
import random
import datetime

def quicksort(sequence):
    """ Performs quicksort on given sequence. 
        sequence = [list|tuple], the sequence to sort
        returns list, the sorted sequence """
    i = 0
    j = len(sequence) - 1
    if len(sequence) <= 1:
        return sequence
    pivot = sequence[1]
    while i < j:
        while i < len(sequence) and sequence[i] < pivot:
            i += 1
        while j >= 0 and sequence[j] > pivot:
            j -= 1
        if i < j:
            temp = sequence[i]
            sequence[i] = sequence[j]
            sequence[j] = temp
    return quicksort(sequence[:i]) + quicksort(sequence[i:])

if __name__ == '__main__':
    length = 1
    while length <= 1000000:
        sequence = [i for i in range(length)]
        random.shuffle(sequence)
        start = datetime.datetime.now()
        quicksort(sequence)
        #sorted(sequence)
        end = datetime.datetime.now()
        delta = end - start
        print('length:', length, 'time:', delta.total_seconds())
        length *= 2
