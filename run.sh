#!/bin/bash
set -e 

for ((i = 0; i < $1; i++)); do
	echo "#################################"
	echo "#### Number of iteration: $i ####"
	echo "#################################"

	$HADOOP_HOME/bin/hadoop jar /home/ubuntu/hadoop/hadoop-3.2.1/share/hadoop/tools/lib/hadoop-streaming-3.2.1.jar \
        -D mapreduce.job.name='job1-getSubPageRankProb' \
        -mapper CombinedPRandTransition.py \
        -reducer PageRankMultiTransitionBuildReducer.py \
        -input hdfs:///pageRank/transition/transition.txt \
        -input hdfs:///pageRank/pr_$i \
        -output hdfs:///pageRank/stage_$i  \
        -file /home/ubuntu/pageRank/src/*
	
	$HADOOP_HOME/bin/hadoop jar /home/ubuntu/hadoop/hadoop-3.2.1/share/hadoop/tools/lib/hadoop-streaming-3.2.1.jar \
        -D mapreduce.job.name='job2-getTotalPageRankProb' \
        -mapper PageRankFinalBuildMapper.py \
        -reducer PageRankFinalBuildReducer.py \
        -input hdfs:///pageRank/stage_$i \
        -output hdfs:///pageRank/pr_$(($i+1))  \
        -file /home/ubuntu/pageRank/src/*

done