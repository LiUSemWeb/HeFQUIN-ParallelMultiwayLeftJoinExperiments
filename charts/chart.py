import matplotlib.pyplot as plt
import numpy as np
from numpy import sqrt
#=================================================================================
#Read output file which is a text file
txt_file = r"output.txt"
file = open(txt_file, 'r')
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
yerr = []
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
    #============================
    #computing standard deviation for each query id
    temp = 0
    for i in query_dict[query]:
        temp = temp + (abs(int(i[1])-averageProcessingTime))**2
    yerr.append(sqrt(temp/int(num_of_run)))
#now the needed data is extracted and stored in data_for_chart (query id and its average processing time)
#=================================================================================
#Bar chart, each query has a bar in chart showing its average overall processing time
labels = data_for_chart_query_id
x = np.arange(len(labels))  # the label locations
width = 0.5  # the width of the bars
fig, ax = plt.subplots()
ax.grid(zorder=0)
ax.set_axisbelow(True)
rects1 = ax.bar(x, data_for_chart_AverageProcessingTime, width, label=None, color='darkslategray')
ax.set_ylabel('Average Overall Query Processing Time')
plt.xlabel('Query ID')
ax.set_xticks(x)
ax.set_xticklabels(labels,rotation=0)
ax.legend(frameon = False)
fig.tight_layout()
plt.errorbar(x, data_for_chart_AverageProcessingTime, yerr, fmt='.', color='Red', elinewidth=2,capthick=10,errorevery=1, alpha=0.5, ms=4, capsize = 2)
plt.savefig('AverageProcessingTimePerQuery.png', bbox_inches='tight')
plt.show()
#=================================================================================
