import matplotlib.pyplot as plt
#There are three approaches, so we have three lines in the chart

def Read_and_extacrt_info_from_output_file(inputfile):
    file = open(inputfile, 'r')
    query_dict = dict()
    for line in file.readlines():
        num_run, query_id, approach, overallRunTime = line.strip().split(',')
        if query_id.strip() in query_dict:
            query_dict[query_id.strip()].append((num_run.strip(), overallRunTime.strip()))
        else:
            query_dict[query_id.strip()] = [(num_run.strip(), overallRunTime.strip())]
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


def Extarct_queries_for_a_approach(q1,q2,q3,q4):
    file1 = open(q1, 'r')
    file2 = open(q2, 'r')
    file3 = open(q3, 'r')
    file4 = open(q4, 'r')
    inputfiles = [file1, file2, file3, file4]
    inputfiles_list = []
    for file in inputfiles:
        list_temp = []
        for line in file.readlines():
            list_temp.append(line)
        inputfiles_list.append(list_temp)
    query_dict = []
    for i in range(3):
        outputfile = []
        for file in inputfiles_list:
            counter = 1
            for line in file:
                if counter != 1:
                    num_run, query_id, approach_id, overallRunTime = line.strip().split(',')
                    aID = int(approach_id) - 1
                    if aID == i:
                        outputfile.append(line)
                else:
                    fname = line.rstrip().split(',')
                counter = counter + 1
        query_dict.append(outputfile)

    fo1 = open("Approach1_group5.txt", "w")
    fo2 = open("Approach2_group5.txt", "w")
    fo3 = open("Approach3_group5.txt", "w")
    for line in query_dict[0]:
        fo1.write(line)
    fo1.close()

    for line in query_dict[1]:
        fo2.write(line)
    fo2.close()

    for line in query_dict[2]:
        fo3.write(line)
    fo3.close()


query1 = r"C:\Users\PycharmProjects\multywayJoin_chart\logs\group5\query1.csv"
query2 = r"C:\Users\PycharmProjects\multywayJoin_chart\logs\group5\query2.csv"
query3 = r"C:\Users\PycharmProjects\multywayJoin_chart\logs\group5\query3.csv"
query4 = r"C:\Users\PycharmProjects\multywayJoin_chart\logs\group5\query4.csv"

Extarct_queries_for_a_approach(query1, query2, query3, query4)
output1 = r"C:\\Users\\PycharmProjects\\multywayJoin_chart\\Approach1_group5.txt"
output2 = r"C:\\Users\\PycharmProjects\\multywayJoin_chart\\Approach2_group5.txt"
output3 = r"C:\\Users\\PycharmProjects\\multywayJoin_chart\\Approach3_group5.txt"

q1, t1 = Read_and_extacrt_info_from_output_file(output1)
q2, t2 = Read_and_extacrt_info_from_output_file(output2)
q3, t3 = Read_and_extacrt_info_from_output_file(output3)

plt.plot(q1, t1, label = "Approach 1", linestyle='solid', linewidth=3)
plt.plot(q2, t2, label = "Approach 2",linestyle='dotted', linewidth=3)
plt.plot(q3, t3, label = "Approach 3",linestyle='dashdot', linewidth=3)

plt.grid(zorder=0, alpha=0.3)
plt.xlabel('Query ID')
plt.ylabel('Average Overall Query Processing Time')
plt.title('Average Overall Query Processing Time, Group 5')
#plt.legend(loc='upper right')
plt.legend()
plt.savefig('AverageProcessingTimePerQuery_3approches_G5.png', bbox_inches='tight')
plt.show()
