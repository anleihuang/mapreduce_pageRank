#!/usr/bin/env python3

import sys
from itertools import groupby

def _read_from_mapper(premapout, seperator = "\t"):
    for line in premapout:
        yield line.strip().split(seperator, 1)


def main(seperator = "\\t"):
    """
    MR Job #1 Reducer: Transition Matrix Builder
    Description: To calculate the multiplication of the page rank matrix
                and the transition matrix
    inputKey#1: pr_key
    inputValue#1: pr_key prob
    inputKey#2: transition_matrix from key
    inputValue#2: transition_matrix toTarget key + probability
    outputKey: toTarget
    outputValue: sum(newKeyPrProb)
    """
    data = _read_from_mapper(sys.stdin, seperator = seperator)

    for key, group in groupby(data, lambda x: x[0]):
        try:
            # seprate the pr input and the transition_matrix input
            keyRelArr = []
            keyPrProb = 0.0
            for key, val in group:
                if "=" in val: # collect transition matrix input: webid1=0.5
                    keyRelArr.append(val)
                else: # update pr val with the pr input
                    keyPrProb = float(val)
            
            # multiplying
            for unitRel in keyRelArr:
                # outputKey: toTarget
                # outputValue: newKeyPrProb
                toTarget = unitRel.split("=")[0]
                relProb = float(unitRel.split("=")[1])
                newKeyPrProb = str(keyPrProb * relProb)
                print("{KEY}{SEP}{VAL}".format(KEY = toTarget, SEP = seperator, VAL = newKeyPrProb))
        except ValueError:
            pass

if __name__ == "__main__":
    main()