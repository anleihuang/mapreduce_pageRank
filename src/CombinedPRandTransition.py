#! /usr/bin/env python3

import sys

def _read_file(filename, seperator = "\t"):
    for line in filename:
        line = line.strip().replace("\t", "\\t").split(seperator, 1)
        if not line or (len(line) < 2 and not line[0]):
            continue
        else:
            yield line

def main(seperator = "\\t"):
    """
    MR Job #1 Mapper: Transition Matrix Builder
    Description: To calculate the multiplication of the page rank matrix
                and the transition matrix
    inputfile: pr_0.txt, transition.txt
    outputKey#1: pr_key
    outputValue#1: pr_key prob
    outputKey#2: transition_matrix from key
    outputValue#2: transition_matrix toTarget key + probability
    """
    data = _read_file(sys.stdin, seperator = seperator)

    for words in data:
        # determine if input is transition matrix
        if words[1].split('.')[0] != "0": 
            matrixKey = words[0]
            matrixVals = words[1].split(',')
            for val in matrixVals:
                print("{KEY}{SEP}{VAL}".format(KEY = matrixKey, SEP = seperator, VAL = val + "=" + str(1/len(matrixVals))))
        else: # input is page rank (pr) matrix
            prkey0 = words[0]
            prValue0 =  words[1]
            print("{KEY}{SEP}{VAL}".format(KEY = prkey0, SEP = seperator, VAL = prValue0))



if __name__ == "__main__":
    main()