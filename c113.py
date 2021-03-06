# -*- coding: utf-8 -*-
"""c113.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DM2CPIEciuwCMyG4P0S7Ar1Lt01aRw4k
"""

import plotly.express as px
import statistics
import pandas as pd

from google.colab import files
data_to_load=files.upload()

df=pd.read_csv("savings_data2.csv")
fig=px.scatter(df,y='quant_saved',color='female')
fig.show()

import csv
import plotly.graph_objects as pgo

with open("savings_data2.csv", newline='') as f:
  reader=csv.reader(f)
  data=list(reader)
data.pop(0)
total_entries=len(data)
total_people_given_reminder=0

for i in data:
  if int(i[3])==1:
    total_people_given_reminder+=1

fig=pgo.Figure(pgo.Bar(x=["reminder","notreminder"],y=[total_people_given_reminder,(total_entries-total_people_given_reminder)]))
fig.show()

allSavings=[]
for a in data:
  allSavings.append(float(a[0]))
print(f"Mean= {statistics.mean(allSavings)}")
print(f"Median= {statistics.median(allSavings)}")
print(f"Mode= {statistics.mode(allSavings)}")

reminded_savings=[]
not_reminded_savings=[]

for b in data:
  if int(b[3])==1:
    reminded_savings.append(float(data[0]))
  else:
    not_reminded_savings.append(float(data[0]))
print("Results for people who were reminded to save:")
print(f"Mean= {statistics.mean(reminded_savings)}")
print(f"Median= {statistics.median(reminded_savings)}")
print(f"Mode= {statistics.mode(reminded_savings)}")

print("Results for people who were not reminded to save:")
print(f"Mean= {statistics.mean(not_reminded_savings)}")
print(f"Median= {statistics.median(not_reminded_savings)}")
print(f"Mode= {statistics.mode(not_reminded_savings)}")

print(f"Stdev of all the data - {statistics.stdev(allSavings)}")
print(f"Stdev of reminded the data - {statistics.stdev(reminded_savings)}")
print(f"Stdev of not reminded the data - {statistics.stdev(not_reminded_savings)}")

import numpy as np

age = []
savings = []
for c in data:
  if float(c[5])!=0:
    age.append(float(c[5]))
    savings.append(float(c[0]))
correlation=np.corrcoef(age,savings)
print(f"Correlation= {correlation[0,1]}")

import plotly.figure_factory as ff
import seaborn as sns
import random

fig=ff.create_distplot([df["quant_saved"].tolist()],["savings"],show_hist=False)
fig.show()
sns.boxplot(data=df,x=df["quant_saved"])

q1=df["quant_saved"].quantile(0.25)
q3=df["quant_saved"].quantile(0.75)
iqr=q3-q1
print(f"q1-{q1}")
print(f"q3-{q3}")
print(f"iqr-{iqr}")

lower_whisker=q1-1.5*iqr
upper_whisker=q3+1.5*iqr
print(f"upper_whisk-{upper_whisker}")
print(f"lower_whisk-{lower_whisker}")

new_df=df[df["quant_saved"]<upper_whisker]
all_savings=new_df["quant_saved"].tolist()
print(f"mean={statistics.mean(all_savings)}")
print(f"stdev={statistics.stdev(all_savings)}")
print(f"median={statistics.median(all_savings)}")
print(f"mode={statistics.mode(all_savings)}")

fig=ff.create_distplot([new_df["quant_saved"].tolist()],["savings"],show_hist=False)
fig.show()

sampling_mean_list=[]
for i in range(1000):
  temp_list=[]
  for j in range(100):
    temp_list.append(random.choice(all_savings))
  sampling_mean_list.append(statistics.mean(temp_list))
mean_sampling=statistics.mean(sampling_mean_list)
fig=ff.create_distplot([sampling_mean_list],["savings"],show_hist=False)
fig.add_trace(pgo.Scatter(x=[mean_sampling,mean_sampling],y=[0,0.1],mode="lines",name="mean"))
fig.show()

print(f"mean={mean_sampling}")
print(f"stdev={statistics.stdev(sampling_mean_list)}")

temp_df=new_df[new_df.age!=0]
age = temp_df["age"].tolist()
savings = temp_df["quant_saved"].tolist()
correlation=np.corrcoef(age,savings)
print(f"Correlation= {correlation[0,1]}")

reminder_df=new_df.loc[new_df["rem_any"]==1]
not_reminder_df=new_df.loc[new_df["rem_any"]==0]
print(reminder_df.head())
print(not_reminder_df.head())
fig=ff.create_distplot([not_reminder_df["quant_saved"].tolist()],["savings"],show_hist=False)
fig.show()

not_reminder_savings=not_reminder_df["quant_saved"].tolist()
sampling_mean_list_not_reminder=[]

for i in range(1000):
  temp_list=[]
  for j in range(100):
    temp_list.append(random.choice(not_reminder_savings))
  sampling_mean_list_not_reminder.append(statistics.mean(temp_list))
mean_sampling_not_reminder=statistics.mean(sampling_mean_list_not_reminder)

stdev_sampling_not_reminder=statistics.stdev(sampling_mean_list_not_reminder)
print(f"mean-{mean_sampling_not_reminder}")
print(f"stdev-{stdev_sampling_not_reminder}")

fig=ff.create_distplot([sampling_mean_list_not_reminder],["savings"],show_hist=False)
fig.add_trace(pgo.Scatter(x=[mean_sampling,mean_sampling],y=[0,0.1],mode="lines",name="mean"))
fig.show()

first_stdev_start=mean_sampling_not_reminder-stdev_sampling_not_reminder
first_stdev_end=mean_sampling_not_reminder+stdev_sampling_not_reminder
print(f"first(start)-{first_stdev_start} and first(end) - {first_stdev_end}")

second_stdev_start=mean_sampling_not_reminder-(2*stdev_sampling_not_reminder)
second_stdev_end=mean_sampling_not_reminder+(2*stdev_sampling_not_reminder)
print(f"second(start)-{second_stdev_start} and second(end) - {second_stdev_end}")

third_stdev_start=mean_sampling_not_reminder-(3*stdev_sampling_not_reminder)
third_stdev_end=mean_sampling_not_reminder+(3*stdev_sampling_not_reminder)
print(f"third(start)-{third_stdev_start} and third(end) - {third_stdev_end}")

reminder_savings=reminder_df["quant_saved"].tolist()
sampling_mean_list_reminder=[]

for i in range(1000):
  temp_list=[]
  for j in range(100):
    temp_list.append(random.choice(reminder_savings))
  sampling_mean_list_reminder.append(statistics.mean(temp_list))
mean_sampling_reminder=statistics.mean(sampling_mean_list_reminder)

stdev_sampling_reminder=statistics.stdev(sampling_mean_list_reminder)
print(f"mean-{mean_sampling_reminder}")
print(f"stdev-{stdev_sampling_reminder}")

fig=ff.create_distplot([sampling_mean_list_reminder],["savings"],show_hist=False)
fig.add_trace(pgo.Scatter(x=[mean_sampling,mean_sampling],y=[0,0.1],mode="lines",name="mean"))
fig.show()

z_score=(mean_sampling_reminder-mean_sampling_not_reminder)/stdev_sampling_not_reminder
print(f"zscore is{z_score}")