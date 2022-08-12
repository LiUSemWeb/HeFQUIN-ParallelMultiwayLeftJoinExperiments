#!/bin/bash


declare approach_config
declare endpoints
declare dbpedia_endpoints

export queries_path=$1
export number_of_runs=$2
export engine=$3
export approach_option=$4

endpoints="--considerSPARQLEndpoint http://127.0.0.1:8890/sparql 
           --considerSPARQLEndpoint http://127.0.0.1:8891/sparql 
           --considerSPARQLEndpoint http://127.0.0.1:8892/sparql 
           --considerSPARQLEndpoint http://127.0.0.1:8893/sparql 
           --considerSPARQLEndpoint http://127.0.0.1:8894/sparql 
           --considerSPARQLEndpoint http://127.0.0.1:8895/sparql 
           --considerSPARQLEndpoint http://127.0.0.1:8896/sparql 
           --considerSPARQLEndpoint http://127.0.0.1:8897/sparql 
           --considerSPARQLEndpoint http://127.0.0.1:8898/sparql 
           --considerSPARQLEndpoint http://127.0.0.1:8899/sparql"
dbpedia_endpoints="--considerSPARQLEndpoint http://dbpedia.org/sparql 
                   --considerSPARQLEndpoint http://dbpedia.org/sparql"

if [[ $approach_option -eq 1 ]]
then
   approach_config=" "
   echo "Use tpOPTAdd (ParallelMultiLeftJoin)."
elif [[ $approach_option -eq 2 ]]
then
   approach_config="--ignoreParallelMultiLeftJoin"
   echo "Use tpAdd (PhysicalOpsForLogicalAddOps)."
elif [[ $approach_option -eq 3 ]]
then
   approach_config="--ignoreParallelMultiLeftJoin --ignorePhysicalOpsForLogicalAddOps"
   echo "Use naive approach."
else
   echo $approach_config
   echo "The approach option should be 1 (Using tpOPTAdd), 2 (Using tpAdd) or 3 (naive)"
   exit 1
fi

export log_path="./logs/"


export group_name=$(basename  $queries_path)
mkdir -p "${log_path}${group_name}"

for QUERY_FILE in "$queries_path"/*
do
  export file_name=$(basename ${QUERY_FILE})
  
  export query_name="${file_name%.*}"
  for run in $(seq 1 $number_of_runs)
  do
    echo "RUN ${query_name} for the ${run} time."
    export log_file_path=${log_path}${group_name}/${query_name}-${run}.log
    java -cp $engine se.liu.ida.hefquin.cli.RunQueryWithoutSrcSel --queryProcStats $approach_config --query ${QUERY_FILE} $endpoints  > $log_file_path 2>&1
  done 
done


python3 get_measurement.py $number_of_runs $queries_path ${log_path}${group_name} $approach_option
