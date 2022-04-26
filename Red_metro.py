import csv

def stations_info(archive):
    stations=list()
    with open(archive) as red_db:
        reader=csv.reader(red_db)
        next(reader)
        for row in reader:
            stations.append(row)
    return stations
   
print(stations_info('red.csv'))
