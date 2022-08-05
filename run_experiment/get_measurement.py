import sys
import json
import csv

def get_measurement(number_of_runs, number_of_queries, log_path='/Users/huali50/Downloads/multiwayjoin_experiments/log/'):
  for query_id in range(number_of_queries):
    query_name = 'query' + str(query_id+1)
    measurements = []
    with open('./query{id}.csv'.format(id=query_id+1), 'w', encoding='UTF8') as csv_file:
      writer = csv.writer(csv_file)
      writer.writerow(['query', 'num_of_run', 'overallQueryProcessingTime(ms)'])
      for run in range(number_of_runs):
        log_file = '{log_path}{query_name}-{run}.txt'.format(log_path=log_path, query_name=query_name, run=run+1)
        content = []
        with open(log_file) as f:
          content = f.readlines()
          #measurements.append(content[3].rstrip())
          #print(content[3].rstrip())
          writer.writerow([query_name, run+1, int(content[3].rstrip().split(' : ')[1])])
  return


if __name__ == "__main__":
  number_of_runs = int(sys.argv[1])
  number_of_queries = int(sys.argv[2])
  get_measurement(number_of_runs, number_of_queries)