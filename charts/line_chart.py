import matplotlib.pyplot as plt
import numpy as np
from numpy import sqrt
#There are three approaches, so we have three lines in the chart
#=================================================================================
#Read output file which is a text file
def Read_and_extacrt_info_from_output_file(inputfile):
    file = open(inputfile, 'r')
    query_dict = dict()
    #Save the text file in a dictionary
    counter = 1 #to skip the first line of the text file
    for line in file.readlines():
        if counter != 1:
            query_id, num_run, overallRunTime = line.strip().split(',')
            if query_id.strip() in query_dict:
                query_dict[query_id.strip()].append((num_run.strip(), overallRunTime.strip()))
            else:
                query_dict[query_id.strip()] = [(num_run.strip(), overallRunTime.strip())]
        else:
            fname = line.rstrip().split(',')
        counter = counter + 1
    #=================================================================================
    data_for_chart = []
    data_for_chart_query_id = []
    data_for_chart_AverageProcessingTime = []
    #extract query_id and average_overall_query_processingTime
    for query in query_dict:
        num_of_run = 0
        average_OverallQueryProcessingTime = 0
        for i in query_dict[query]:
            num_of_run = i[0]
            average_OverallQueryProcessingTime = average_OverallQueryProcessingTime + int(i[1])
        averageProcessingTime = average_OverallQueryProcessingTime/int(num_of_run)
        data_for_chart.append((query, averageProcessingTime))
        data_for_chart_query_id.append(query)
        data_for_chart_AverageProcessingTime.append(averageProcessingTime)
    return data_for_chart_query_id, data_for_chart_AverageProcessingTime
#now the needed data is extracted and stored in data_for_chart (query id and its average processing time)
output1 = r"C:\\Users\\minab62\\PycharmProjects\\multywayJoin_chart\\output1.txt"
output2 = r"C:\\Users\\minab62\\PycharmProjects\\multywayJoin_chart\\output2.txt"
output3 = r"C:\\Users\\minab62\\PycharmProjects\\multywayJoin_chart\\output3.txt"

q1, t1 = Read_and_extacrt_info_from_output_file(output1)
q2, t2 = Read_and_extacrt_info_from_output_file(output2)
q3, t3 = Read_and_extacrt_info_from_output_file(output3)

plt.plot(q1, t1, label = "line 1", linestyle='solid')
plt.plot(q2, t2, label = "line 2",linestyle='dotted')
plt.plot(q3, t3, label = "line 2",linestyle='dashdot')

plt.xlabel('Query ID')
plt.ylabel('Average Overall Query Processing Time')
plt.legend()
plt.savefig('AverageProcessingTimePerQuery_ThreeApproaches.png', bbox_inches='tight')
plt.show()

#=================================================================================