## Getting Started


* run_experiment.sh PATH_OF_QUERIES NUM_OF_RUNS PATH_OF_ENGINE APPROACH_OPTION 
  * APPROACH_OPTION: 1-ParallelMultiLeftJoin, 2-PhysicalOpsForLogicalAddOps (--ignoreParallelMultiLeftJoin), 3-naive (--ignoreParallelMultiLeftJoin --ignorePhysicalOpsForLogicalAddOps)

Example:
```
./run_experiment.sh ../queries/group1/ 2 ./HeFQUIN-0.0.1-SNAPSHOT.jar 1
```
