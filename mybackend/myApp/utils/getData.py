from myApp.models import *

def getAllHydroData():
    return HydroData.objects.all()

def min_max_scaler(data, min_max_values):
    return (data - min_max_values[0]) / (min_max_values[1] - min_max_values[0]) * 100

def calculate_values(data, min_max_values, month_data, day, attribute):
    min_max_values[attribute][0] = min(min_max_values[attribute][0], getattr(data, attribute))
    min_max_values[attribute][1] = max(min_max_values[attribute][1], getattr(data, attribute))
    month_data[attribute][day][0][data.water_quality - 1] += getattr(data, attribute)

def getHydroData():
    hydro_data = list(getAllHydroData())    
    attributes = ['temperature', 'ph', 'dissolved_oxygen', 'conductivity', 'turbidity', 'permanganate_index', 'ammonia_nitrogen', 'total_nitrogen', 'total_phosphorus']
    min_max_values = {attribute: [float('inf'), float('-inf')] for attribute in attributes}
    April_data = {attribute: {} for attribute in attributes}
    May_data = {attribute: {} for attribute in attributes}
    records = {'April': {}, 'May': {}}

    for data in hydro_data:
        day = str(data.date.day)
        month = 'April' if data.date.month == 4 else 'May'
        month_data = April_data if data.date.month == 4 else May_data
        if day not in records[month]:
            records[month][day] = [0]*5
        records[month][day][data.water_quality - 1] += 1
        for attribute in attributes:
            if day not in month_data[attribute]:
                month_data[attribute][day] = [[0] * 5, [0] * 5]
            calculate_values(data, min_max_values, month_data, day, attribute)

    for month_data in [April_data, May_data]:
        month = 'April' if month_data == April_data else 'May'
        for attribute in attributes:
            for day in month_data[attribute]:
                for i in range(5):
                    if month_data[attribute][day][0][i] != 0:
                        month_data[attribute][day][0][i] /= records[month][day][i]
                        month_data[attribute][day][1][i] = min_max_scaler(month_data[attribute][day][0][i], min_max_values[attribute])

    return April_data, May_data, records

def getHydroDataList():
    hydro_data = list(getAllHydroData())
    res = []
    for data in hydro_data:
        res.append([data.date.strftime('%Y-%m-%d'), data.ph, data.dissolved_oxygen, data.temperature, data.total_nitrogen])
    return res

def getAllFishData():
    return Fish.objects.all()

def getFishData():
    fish_data = list(getAllFishData())
    species_stats = {}
    for data in fish_data:
        if data.species not in species_stats:
            species_stats[data.species] = {'count': 0, 'total_weight': 0, 'total_length': 0, 'total_width': 0, 'total_height': 0}
        species_stats[data.species]['count'] += 1
        species_stats[data.species]['total_weight'] += data.weight
        species_stats[data.species]['total_length'] += data.length
        species_stats[data.species]['total_width'] += data.width
        species_stats[data.species]['total_height'] += data.height

    species_stats_list = {'species_count': [], 'average_weight': [], 'average_length': [], 'average_width': [], 'average_height': []}
    for species in species_stats:
        species_stats_list['species_count'].append({'name': species, 'value': species_stats[species]['count']})
        species_stats_list['average_weight'].append(species_stats[species]['total_weight'] / species_stats[species]['count'])
        species_stats_list['average_length'].append(species_stats[species]['total_length'] / species_stats[species]['count'])
        species_stats_list['average_width'].append(species_stats[species]['total_width'] / species_stats[species]['count'])
        species_stats_list['average_height'].append(species_stats[species]['total_height'] / species_stats[species]['count'])
        
    return species_stats_list

def getScore():
    hydro_data = list(getAllHydroData())    
    attributes = ['ph', 'dissolved_oxygen', 'permanganate_index', 'ammonia_nitrogen', 'total_nitrogen', 'total_phosphorus']
    April_data, May_data = {}, {}
    records = {'April': {}, 'May': {}}

    for data in hydro_data:
        day = str(data.date.day)
        month = 'April' if data.date.month == 4 else 'May'
        month_data = April_data if data.date.month == 4 else May_data
        if day not in records[month]:
            records[month][day] = 0
            month_data[day] = {}
        records[month][day] += 1
        for attribute in attributes:
            if attribute not in month_data[day]:
                month_data[day][attribute] = 0
            month_data[day][attribute] += getattr(data, attribute)

    for month_data in [April_data, May_data]:
        month = 'April' if month_data == April_data else 'May'
        for day in month_data:
            for attribute in month_data[day]:
                month_data[day][attribute] /= records[month][day]

    # print(April_data)
    scores = {'April': {}, 'May': {}}
    for month_data in [April_data, May_data]:
        month = 'April' if month_data == April_data else 'May'
        for day in month_data:
            scores[month][day] = 20
            if month_data[day]['dissolved_oxygen'] >= 7.5 and month_data[day]['permanganate_index'] <= 2 \
                and month_data[day]['ammonia_nitrogen'] <= 0.15 and month_data[day]['total_nitrogen'] <= 0.2 \
                    and month_data[day]['total_phosphorus'] <= 0.02:
                scores[month][day] = 80 + 4 * (month_data[day]['dissolved_oxygen'] - 7.5) + 4 * (2 - month_data[day]['permanganate_index']) \
                    + 4 * (0.15 - month_data[day]['ammonia_nitrogen']) + 4 * (0.2 - month_data[day]['total_nitrogen']) + 4 * (0.02 - month_data[day]['total_phosphorus'])
            elif month_data[day]['dissolved_oxygen'] >= 6 and month_data[day]['permanganate_index'] <= 4 \
                and month_data[day]['ammonia_nitrogen'] <= 0.5 and month_data[day]['total_nitrogen'] <= 0.5 \
                    and month_data[day]['total_phosphorus'] <= 0.1:
                scores[month][day] = 60 + 4 * (month_data[day]['dissolved_oxygen'] - 6) + 4 * (4 - month_data[day]['permanganate_index']) \
                    + 4 * (0.5 - month_data[day]['ammonia_nitrogen']) + 4 * (0.5 - month_data[day]['total_nitrogen']) + 4 * (0.1 - month_data[day]['total_phosphorus'])
            elif month_data[day]['dissolved_oxygen'] >= 5 and month_data[day]['permanganate_index'] <= 6 \
                and month_data[day]['ammonia_nitrogen'] <= 1 and month_data[day]['total_nitrogen'] <= 1 \
                    and month_data[day]['total_phosphorus'] <= 0.2:
                scores[month][day] = 40 + 4 * (month_data[day]['dissolved_oxygen'] - 5) + 4 * (6 - month_data[day]['permanganate_index']) \
                    + 4 * (1 - month_data[day]['ammonia_nitrogen']) + 4 * (1 - month_data[day]['total_nitrogen']) + 4 * (0.2 - month_data[day]['total_phosphorus'])
            elif month_data[day]['dissolved_oxygen'] >= 3 and month_data[day]['permanganate_index'] <= 10 \
                and month_data[day]['ammonia_nitrogen'] <= 1.5 and month_data[day]['total_nitrogen'] <= 1.5 \
                    and month_data[day]['total_phosphorus'] <= 0.3:
                scores[month][day] = 20 + 4 * (month_data[day]['dissolved_oxygen'] - 3) + 4 * (10 - month_data[day]['permanganate_index']) \
                    + 4 * (1.5 - month_data[day]['ammonia_nitrogen']) + 4 * (1.5 - month_data[day]['total_nitrogen']) + 4 * (0.3 - month_data[day]['total_phosphorus'])
            else:
                scores[month][day] = 0 + 4 * (month_data[day]['dissolved_oxygen'] - 2) + 4 * (15 - month_data[day]['permanganate_index']) \
                    + 4 * (2 - month_data[day]['ammonia_nitrogen']) + 4 * (2 - month_data[day]['total_nitrogen']) + 4 * (0.4 - month_data[day]['total_phosphorus'])            
                
    return scores

def get_all_fish_data():
    fish_data = list(getAllFishData())
    res, columns = [], ['species', 'weight', 'length', 'width', 'height']
    for data in fish_data:
        tmp = {}
        for column in columns:
            tmp[column] = getattr(data, column.lower())
        res.append(tmp)
    return res
