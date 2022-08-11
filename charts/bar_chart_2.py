import matplotlib.pyplot as plt
import numpy as np
from numpy import sqrt
#Read output file which is a text file
query1 = r"C:\Users\minab62\PycharmProjects\multywayJoin_chart\logs\group1\query1.csv"
query2 = r"C:\Users\minab62\PycharmProjects\multywayJoin_chart\logs\group1\query2.csv"
query3 = r"C:\Users\minab62\PycharmProjects\multywayJoin_chart\logs\group1\query3.csv"
query4 = r"C:\Users\minab62\PycharmProjects\multywayJoin_chart\logs\group1\query4.csv"

file1 = open(query1, 'r')
file2 = open(query2, 'r')
file3 = open(query3, 'r')
file4 = open(query4, 'r')
file = [file1, file2, file3, file4]
query_dict_approach1 = dict()
query_dict_approach2 = dict()
query_dict_approach3 = dict()
#Save the text file in a dictionary
for f in file:
    # to skip the first line of the text file
    counter = 1
    for line in f.readlines():
        if counter != 1:
            num_run, query_id, approach, overallRunTime = line.strip().split(',')
            if approach == '1':
                if query_id.strip() in query_dict_approach1:
                    query_dict_approach1[query_id.strip()].append((num_run.strip(), overallRunTime.strip()))
                else:
                    query_dict_approach1[query_id.strip()] = [(num_run.strip(), overallRunTime.strip())]
            if approach == '2':
                if query_id.strip() in query_dict_approach2:
                    query_dict_approach2[query_id.strip()].append((num_run.strip(), overallRunTime.strip()))
                else:
                    query_dict_approach2[query_id.strip()] = [(num_run.strip(), overallRunTime.strip())]
            if approach == '3':
                if query_id.strip() in query_dict_approach3:
                    query_dict_approach3[query_id.strip()].append((num_run.strip(), overallRunTime.strip()))
                else:
                    query_dict_approach3[query_id.strip()] = [(num_run.strip(), overallRunTime.strip())]
        else:
            fname = line.rstrip().split(',')
        counter = counter + 1

query_dict = [query_dict_approach1, query_dict_approach2, query_dict_approach3]
data_for_chart = []
data_for_chart_query_id = []
data_for_chart_AverageProcessingTime = []
#extract query_id and average_overall_query_processingTime
yerr_value = []
for qd in query_dict:
    yerr_value_temp = []
    data_for_chart_temp = []
    data_for_chart_query_id_temp = []
    data_for_chart_AverageProcessingTime_temp = []
    for query in qd:
        num_of_run = 0
        average_OverallQueryProcessingTime = 0
        for i in qd[query]:
            num_of_run = i[0]
            average_OverallQueryProcessingTime = average_OverallQueryProcessingTime + int(i[1])
        averageProcessingTime = average_OverallQueryProcessingTime/int(num_of_run)
        data_for_chart_temp.append((query, averageProcessingTime))
        data_for_chart_query_id_temp.append(query)
        data_for_chart_AverageProcessingTime_temp.append(averageProcessingTime)
        #computing standard deviation for each query id
        temp = 0
        for i in qd[query]:
            temp = temp + (abs(int(i[1])-averageProcessingTime))**2
        yerr_value_temp.append(sqrt(temp/int(num_of_run)))
    yerr_value.append(yerr_value_temp)
    data_for_chart.append(data_for_chart_temp)
    data_for_chart_query_id.append(data_for_chart_query_id_temp)
    data_for_chart_AverageProcessingTime.append(data_for_chart_AverageProcessingTime_temp)
#now the needed data is extracted and stored in data_for_chart (query id and its average processing time)
#=================================================================================
#Bar chart, each query has a bar in chart showing its average overall processing time
for i in range(3):
    labels = data_for_chart_query_id[i]
    x = np.arange(len(labels))  # the label locations
    width = 0.5  # the width of the bars
    fig, ax = plt.subplots()
    ax.grid(zorder=0)
    ax.set_axisbelow(True)
    rects1 = ax.bar(x, data_for_chart_AverageProcessingTime[i], width, label=None, color='darkslategray', yerr=yerr_value[i], ecolor='red')
    ax.set_ylabel('Average Overall Query Processing Time')
    plt.xlabel('Query ID')
    id = i+1
    plt.title(f'Average Overall Query Processing Time for Approach{id}, Group{id}')
    ax.set_xticks(x)
    ax.set_xticklabels(labels,rotation=0)
    ax.legend(frameon = False)
    fig.tight_layout()
    #plt.errorbar(x, data_for_chart_AverageProcessingTime, yerr, fmt='.', color='Red', elinewidth=2,capthick=10,errorevery=1, alpha=0.5, ms=4, capsize = 2)
    plt.savefig(f'AverageProcessingTimePerQuery_group1_approach{id}.png', bbox_inches='tight')
    plt.show()
#=================================================================================
