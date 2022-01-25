import plotly.figure_factory as ff 
import random 
import pandas as pd 
import csv
import statistics

df = pd.read_csv('studentsperformance.csv')
studentsperformance = df["reading score"].tolist()
studentperformancemean = statistics.mean(studentperformance)
studentperformancemedian = statistics.median(studentperformance)
studentperformancemode = statistics.mode(studentperformance)
studentperformancestandardDeiviation = statistics.stdev(studentperformance)
print('mean, median and mode of height is {},{} and {}'.format(studentsperformancemean,studentsperformancemedian,studentsperformancemode))

studentperformancefirst_stdevstart,studentperformancefirst_stdev_end = studentperformancemean-studentperformancestandardDiviation,studentperformancemean+studentperformancestandardDiviation
studentperformancesecond_stdevstart,studentperformancesecond_stdevend = studentperformancemean - (2*studentperformancestandardDiviation),studentperformancemean+(2*studentperformancestandardDiviation)
studentperformancethirdstdevstart, studentperformancethirdstdevend = studentperformancemean - (3*studentperformancestandardDiviation),studentperformancemean+(3*studentperformancestandardDiviation)

studentperformanceList_1stdev = [result for result in studentperformance if result>studentperformancefirst_stdevstart and result<studentperformancefirst_stdev_end]
studentperformanceList_2stdev = [result for result in studentperformance if result>studentperformancesecond_stdevstart and result<studentperformancesecond_stdevend]
studentperformanceList_3stdev = [result for result in studentperformance if result>studentperformancethirdstdevstart and result<studentperformancethirdstdevend]

print("{}% of data for studentperformance lies within 1 standard deviation".format(len(studentperformanceList_1stdev)*100.0/len(studentperformance)))
print("{}% of data for studentperformance lies within 2 standard deviation".format(len(studentperformanceList_2stdev)*100.0/len(studentperformance)))
print("{}% of data for studentperformance lies within 3i standard deviation".format(len(studentperformanceList_3stdev)*100.0/len(studentperformance)))

