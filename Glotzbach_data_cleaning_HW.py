import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

flights_data = pd.read_csv('flights.csv')
#flights_data.head(10)

#weather_data_pd = pd.read_csv('weather.csv')
#weather_data_np = weather_data_pd.to_numpy()

#print(flights_data.columns)

#Question 1:
q1_flights = len(flights_data[(flights_data['origin']=='JFK') & (flights_data['dest']=='SLC')])
print("Question 1:")
print("flights from JFK-SLC =",q1_flights)
print("\n")

#Question 2:
SLC_flights = flights_data.loc[flights_data['dest'] == 'SLC']
q2_airlines = SLC_flights['carrier'].nunique()
print("Question 2:")
print("airlines that fly to SLC =", q2_airlines)
print("\n")

#Question 3:
RDU_flights = flights_data.loc[flights_data['dest'] == 'RDU']
q3_avgdelay = RDU_flights['arr_delay'].mean()
print("Question 3:")
print("average arrival delay for RDU flights =", q3_avgdelay)
print("\n")

#Question 4:
SEA_flights = flights_data.loc[flights_data['dest'] == 'SEA']
NYCtoSEA = SEA_flights.loc[(SEA_flights['origin'] == 'JFK') | (SEA_flights['origin'] == 'LGA')]
NYCtoSEA_prop = len(NYCtoSEA) / len(SEA_flights)
print("Question 4:")
print("proportion of SEA flights from NYC =", NYCtoSEA_prop)
print("\n")

#Question 5:
flights_data['date'] = pd.to_datetime(flights_data[['year', 'month', 'day']])
flights_data['date'] = pd.to_datetime(flights_data['date'], format='%Y/%m/%d')
flights_sorted = flights_data.sort_values(by='dep_delay',ascending=False)
flights_sorted.head(1)