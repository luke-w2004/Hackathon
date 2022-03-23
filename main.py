import requests
start_date = input("Start Date (YYYY-MM-DD): ")
end_date = input("End Date (YYYY-MM-DD): ")
url = "https://api.nasa.gov/neo/rest/v1/feed?start_date="+start_date+"&end_date="+end_date+"&api_key="
f = open("keys.txt", "r")
key = f.readline()
f.close()
  
data = requests.get(f'{url}{key}').json() #fancy request code
#
totalavg = 0 #initialisation
try: #fancy validation
  print(data['http_error'])
except KeyError:
  totalelems = (data['element_count'])
  for name, info in data['near_earth_objects'].items():
    for i in info:
      #print(i['name']) #prints NEO name
      min = i['estimated_diameter']['meters']['estimated_diameter_min']
      max = i['estimated_diameter']['meters']['estimated_diameter_max']
      average = (min + max) / 2 #average stuff
      #print("The average size is: " + str(average) + "m") #prints average size of printed NEO 
      totalavg += average
  print("There are " + str(totalelems) + " NEOs within the specified period.")
  averageSize = totalavg / totalelems
  print("Average Size: " + str(averageSize) + "m")