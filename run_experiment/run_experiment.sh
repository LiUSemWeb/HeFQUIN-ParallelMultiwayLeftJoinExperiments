#!/bin/bash

#HeFQUIN="/Users/huali50/Downloads/HeFQUIN-main/target/HeFQUIN-0.0.1-SNAPSHOT.jar"
#query_path="/Users/huali50/Downloads/multiwayjoin_experiments/queries/"
log_path="/Users/huali50/Downloads/multiwayjoin_experiments/log/"

#number_of_runs=2

#java -cp $HeFQUIN se.liu.ida.hefquin.cli.RunQueryWithoutSrcSel --query $query --considerSPARQLEndpoint http://10.253.227.81:9999/bigdata/sparql
#java -cp /Users/huali50/Downloads/HeFQUIN-main/target/HeFQUIN-0.0.1-SNAPSHOT.jar se.liu.ida.hefquin.cli.RunQueryWithoutSrcSel --query /Users/huali50/Downloads/multiwayjoin_experiments/queries/query1.rq --considerSPARQLEndpoint http://10.253.227.81:9999/bigdata/sparql

#args=$#                          # number of command line args
#for (( i=1; i<=$args; i+=1 ))    # loop from 1 to N (where N is number of args)
#do
#  echo "HEREI"
#    echo $i
#done
declare endpoints
export query_num=$1
echo $query_num
export number_of_runs=$2
echo $number_of_runs
export federation_num=$3
export engine=$4
export queries_path=$5
#export logs_path=$6
export endpoint=$6

for fed in $(seq 1 $federation_num)
do
  let ep=$fed+5
  #echo ${!ep}
  endpoints+="--considerSPARQLEndpoint "
  endpoints+=${!ep}
  if [ $fed -lt $federation_num ]
  then
      endpoints+=" "
  fi
done

echo $endpoints
#echo $query_num

for run in $(seq 1 $number_of_runs)
do
  for query_id in $(seq 1 $query_num)
  do
    #echo ${query_path}query${query_id}.rq
    export log_file_path=${log_path}query${query_id}-${run}.txt
    #java -cp $HeFQUIN se.liu.ida.hefquin.cli.RunQueryWithoutSrcSel --query ${query_path}query${query_id}.rq  --considerSPARQLEndpoint http://10.253.227.81:9999/bigdata/sparql > $log_file_path
    #java -cp $HeFQUIN se.liu.ida.hefquin.cli.RunQueryWithoutSrcSel --query ${query_path}query${query_id}.rq  --considerSPARQLEndpoint $endpoint > $log_file_path
    #java -cp $HeFQUIN se.liu.ida.hefquin.cli.RunQueryWithoutSrcSel --query ${query_path}query${query_id}.rq  --considerSPARQLEndpoint $endpoint > $log_file_path
    #java -cp $engine se.liu.ida.hefquin.cli.RunQueryWithoutSrcSel --query ${queries_path}query${query_id}.rq  --considerSPARQLEndpoint $endpoints > $log_file_path
    java -cp $engine se.liu.ida.hefquin.cli.RunQueryWithoutSrcSel --query ${queries_path}query${query_id}.rq  $endpoints > $log_file_path
  done
done
python get_measurement.py $number_of_runs $query_num



