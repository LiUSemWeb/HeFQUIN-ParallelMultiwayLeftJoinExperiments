## Getting Started


* run_experiment.sh NUMBER_OF_QUERIES NUM_OF_RUNS NUM_OF_FEDERATIONS PATH_OF_ENGINE PATH_OF_QUERIES APPROACH_OPTION ENDPOINTS

* ./run_experiment.sh 4 2 2 /PATH/HeFQUIN-0.0.1-SNAPSHOT.jar /PATH/group1/ APPROACH_OPTION FEDERATION_1_ENDPOINT FEDERATION_2_ENDPOINT


Example:
```
./run_experiment.sh 4 2 5 ../HeFQUIN-0.0.1-SNAPSHOT.jar ../queries/group1/ http://127.0.0.1:8890/sparql http://127.0.0.1:8891/sparql http://127.0.0.1:8892/sparql http://127.0.0.1:8893/sparql http://127.0.0.1:8894/sparql
```
