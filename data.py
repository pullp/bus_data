
import pandas as pandas
import datetime

trips = pandas.read_csv("trips.txt")

stop_times = pandas.read_csv("stop_times.txt")
stops = pandas.read_csv("stops.txt")


stop_position = stops.loc[:,['stop_id', 'stop_lon', 'stop_lat']]
route_trip = trips.loc[:,['route_id', 'trip_id']]
trip_stop_time = stop_times.loc[:, ['trip_id', 'arrival_time', 'stop_id']]

route_trip_stop_time = pandas.merge(route_trip, trip_stop_time, on = "trip_id")

final = pandas.merge(route_trip_stop_time, stop_position, on = "stop_id")


base_time = datetime.datetime(1900, 1, 1)


final['arrival_time'] = final['arrival_time'].apply(lambda time: (datetime.datetime(1900, 1, 1, int(time[:2])%24, int(time[3:5]), int(time[6:])) - base_time).total_seconds())


current_trip_id=''
current_route_id = ''

f = open('out.csv', 'w')
buf = ""
stop_count = 0

for i, row in v2.iterrows():
    if(current_trip_id != i[0]) :
        f.write(current_route_id + "," + str(stop_count) + '\n')
        f.write(buf + '\n')
        current_route_id = str(i[1])
        current_trip_id = i[0]
        stop_count = 0
        buf = ''
    buf += (str(i[2]) + "," + str(row['stop_lat']) + "," + str(row['stop_lon']) + "," + str(row['arrival_time']) + '\n')
    stop_count += 1

    
f.close()