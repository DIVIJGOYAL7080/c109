import random
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go
dice=[]
for i in range(0,1000):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    dice.append(dice1+dice2)
print(dice)
#calculating the mean and the standard deviation
mean=sum(dice)/len(dice)
standarddeviation=statistics.stdev(dice)
median=statistics.median(dice)
mode=statistics.mode(dice)
#finding first standard deviation and end values
firststandarddeviationstart,firstdeviationend=mean-standarddeviation,mean+standarddeviation
secondstandarddeviationstart,secondstandarddeviationend=mean-(2*standarddeviation),mean+(2*standarddeviation)
thirdstandarddeviationstart,thirdstandarddeviationend=mean-(3*standarddeviation),mean+(3*standarddeviation)
print("mean= ",mean)
print("standarddeviation= ",standarddeviation)
print("median= ",median)
print("mode= ",mode)
fig=ff.create_distplot([dice],["result"],show_hist=True)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[firststandarddeviationstart, firststandarddeviationstart], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[firstdeviationend, firstdeviationend], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[secondstandarddeviationstart, secondstandarddeviationstart], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[secondstandarddeviationend, secondstandarddeviationend], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))

fig.show()
#printing the findings
list_of_data_within_1_std_deviation = [result for result in dice if result > firststandarddeviationstart and result < firstdeviationend]
list_of_data_within_2_std_deviation = [result for result in dice if result > secondstandarddeviationstart and result < secondstandarddeviationend]
list_of_data_within_3_std_deviation = [result for result in dice if result > thirdstandarddeviationstart and result < thirdstandarddeviationend]
print("{}% of data lies within 1 standard deviation".format(len(list_of_data_within_1_std_deviation)*100.0/len(dice)))
print("{}% of data lies within 2 standard deviation".format(len(list_of_data_within_2_std_deviation)*100.0/len(dice)))
print("{}% of data lies within 3 standard deviation".format(len(list_of_data_within_3_std_deviation)*100.0/len(dice)))

