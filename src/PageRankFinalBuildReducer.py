#!/usr/bin/env python3

import sys
from itertools import groupby

def _read_from_mapper(premapout, seperator = "\t"):
    for line in premapout:
        yield line.strip().split(seperator, 1)


def main(seperator = "\\t"):
    """
    MR Job #2 Reducer: The Next Page Rank Matrix Builder
    Description: To build the final page rank table
    inputKey: toTarget
    inputValue: newKeyPrProb
    outputKey: toTarget
    outputValue: sum(newKeyPrProb)
    """
    data = _read_from_mapper(sys.stdin, seperator = seperator)

    for key, group in groupby(data, lambda x: x[0]):
        try:
            totalProb = 0.0
            for key, prob in group:
                totalProb += float(prob)
            print("{KEY}{SEP}{VAL}".format(KEY = key, SEP = seperator, VAL = str(totalProb)))
        except ValueError:
            pass


if __name__ == "__main__":
    main()