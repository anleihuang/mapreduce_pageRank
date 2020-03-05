#!/usr/bin/env python3

import sys

def _read_file(filename, seperator = "\t"):
    for line in filename:
        yield line.strip().split(seperator, 1)

def main(seperator = "\\t"):
    """
    MR Job #2 Mapper: The Next Page Rank Builder
    Description: To build the final page rank table
    inputKey: toTarget
    inputValue: newKeyPrProb
    outputKey: toTarget
    outputValue: newKeyPrProb
    """
    data = _read_file(sys.stdin, seperator = seperator)

    for words in data:
        prkeysub = words[0]
        prValuesub =  words[1]
        print("{KEY}{SEP}{VAL}".format(KEY = prkeysub, SEP = seperator, VAL = prValuesub))

if __name__ == "__main__":
    main()