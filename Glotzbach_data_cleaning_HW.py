#Jason Glotzbach HW -- Data Cleaning with Pandas

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

flights_data = pd.read_csv('flights.csv')
#flights_data.head(10)

weather_data_pd = pd.read_csv('weather.csv')
weather_data_np = weather_data_pd.to_numpy()

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
ddelay_date = flights_data.groupby('date').agg(mean_dep_delay=('dep_delay', np.mean))
date_max_ddelay = ddelay_date['mean_dep_delay'].idxmax()
print("Question 5:")
print("the date with the largest average departure delay is ", date_max_ddelay)
print("\n")

#Question 6:
arrdelay_date = flights_data.groupby('date').agg(mean_arr_delay=('arr_delay', np.mean))
date_max_arrdelay = arrdelay_date['mean_arr_delay'].idxmax()
print("Question 6:")
print("the date with the largest average arrival delay is ", date_max_arrdelay)
print("\n")

#Question 7:
NYC_departure_flights2013 = flights_data.loc[(flights_data['origin'] == 'JFK') | (flights_data['origin'] == 'LGA') & (flights_data['year'] == 2013)]
NYC_departure_flights2013['speed'] = NYC_departure_flights2013['distance'] / NYC_departure_flights2013['air_time']
max_speed_index = NYC_departure_flights2013['speed'].idxmax()
fastest_flight = NYC_departure_flights2013.loc[max_speed_index,'tailnum']
print("Question 7:")
print("the NYC flight in 2013 with the fastest speed was tail number", fastest_flight)
print("\n")

#Question 8:
print("Question 8:")
nan_count_pre = weather_data_pd.isnull().sum().sum()
print("before cleaning, the weather data frame had ", nan_count_pre,'NaN values')
weather_data_pd = weather_data_pd.fillna(0)
nan_count_post = weather_data_pd.isnull().sum().sum()
print("after cleaning, the weather data frame had ", nan_count_post,'NaN values')
print("\n")

#Question 9:
feb_ob_count = weather_data_pd['month'].value_counts()[2]
print("Question 9:")
print("there were ", feb_ob_count,"observations in February")
print("\n")

#Question 10:
feb_data = weather_data_pd.loc[weather_data_pd['month'] == 2]
mean_feb_humidity = feb_data['humid'].mean()
print("Question 10:")
print("the average humidity in February was ", mean_feb_humidity)
print("\n")

#Question 11:
feb_data = weather_data_pd.loc[weather_data_pd['month'] == 2]
std_feb_humidity = feb_data['humid'].std()
print("Question 10:")
print("the standard deviation for humidity in February was ", std_feb_humidity)
print("\n")