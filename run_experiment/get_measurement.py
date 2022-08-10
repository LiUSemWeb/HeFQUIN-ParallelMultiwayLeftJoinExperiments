import sys
import csv
import os

def get_measurement(number_of_runs, query_path, log_path, approach_option):
  query_names = [os.path.basename(f).split('.')[0] for f in os.listdir(query_path) if f.endswith('.sparql')]
  for query_name in query_names:
    measurement_file = '{log_path}/{query}.csv'.format(log_path=log_path, query=query_name)
    headers = ['num_of_run', 'query', 'approach', 'overallQueryProcessingTime(ms)']
    file_exists = os.path.isfile(measurement_file)
    with open(measurement_file, 'a', encoding='UTF8') as csv_file:
      writer = csv.writer(csv_file, delimiter=',', lineterminator='\n')
      #writer.writerow(['query', 'num_of_run', 'overallQueryProcessingTime(ms)'])
      if not file_exists:
        writer.writerow(headers)
      for i in range(number_of_runs):
        log_file = '{log_path}/{query}-{run}.log'.format(log_path=log_path, query=query_name, run=i+1)
        with open(log_file) as f:
          content = f.read()
          queryProcStats = content[content.index('overallQueryProcessingTime'):content.index('planningTime')].rstrip()
          writer.writerow([i+1, query_name, approach_option, int(queryProcStats.split(' : ')[1])])
  return

if __name__ == "__main__":
  number_of_runs = int(sys.argv[1])
  query_path = str(sys.argv[2])
  log_path = str(sys.argv[3])
  approach_option = int(sys.argv[4])
  get_measurement(number_of_runs, query_path, log_path, approach_option)