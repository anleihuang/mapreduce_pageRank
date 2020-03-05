## Introduction
[PageRank](https://en.wikipedia.org/wiki/PageRank) is an algorithm to rank websites in a searching engine. The ranking logic is based on the number of a website redirect to it from other websites (quantity), and the imporatance of the other websites are that direct to this specific website (quality). The relation of the websites form directed praphs. The concept translate to the input file formats are (1) a page rank initial probability matrix (an evenly distributed vector) (2) transition matrix (represent the relation of the directed graph).

In the project, in order to avoid edge cases such as dead ends or an infinite loop, the iteration method is introduced. The number of loops are passed through arguments.

This Hadoop MapReduce program is written in Python 3.7. Since this project is essentially matrix multiplication which is resource consuming, the process is broken down to two MapReduce jobs.

## Architecture
### 1. MapReduce Job # 1
- Read in initial page rank matrix file (pr_0.txt) and the post-processed transition matrix file
- Multiply page rank matrix amd transition matrix on a unit basis
<img src="https://github.com/anleihuang/mapreduce_pageRank/blob/master/docs/pr_MR1.png"  width="400" height="300">

### 2. MapReduce Job # 2
- Sum up the new probability for the to-target website. This output result is the new input for the next iteration
<img src="https://github.com/anleihuang/mapreduce_pageRank/blob/master/docs/pr_MR2.png"  width="400" height="300">

## Implementation
1. Download the git repo
2. Set up the environmental variables in ./bashrc
```
export HADOOP_HOME=//the path to where your hadoop is
```
3. Execute `bash run.sh N` on the terminal, where N is the number of iteration you would like to execute
* if you cannot run the run.sh file, make sure the execution permission is set correctly through `chmod +x run.sh`

## Result Snapshot
The below is a snapshot of the page rank probability for the 5th iteration. The key represents website ID, and the value is the probability.
<img src="https://github.com/anleihuang/mapreduce_pageRank/blob/master/docs/result.png"  width="400" height="300">

## Local Testing
A few commands are useful for debugging while developing the code

```
# make sure the python files have execution permission
chomd + x ./src/*

cat ./inputs/* | ./src/CombinedPRandTransition.py

cat ./inputs/* | ./src/CombinedPRandTransition.py | sort -k1,1 | ./src/PageRankMultiTransitionBuildReducer.py
```

## Environment Setup

### Hadoop Cluster
Set up a hadoop cluster with one name node and three data node in AWS
1. Hadoop Name Node: 1 x t2.large AWS EC2
2. Hadoop Data Node: 3 x t2.medium AWS EC2


## Prerequisites
- java 8
- python 3.7
- Hadoop 3.2.1

## Challenges
The project requires mappers to read in two different files. Unlike Java which has built-in MultipleInputs so it's simpler to build a mapper associate to one kind of file, Python is not able to seperate different input files for different mappers. The workaround implemented here is reading in all files and determining which file is which at the mapper stage.
