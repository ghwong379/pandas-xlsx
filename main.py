import pandas as pd
import io
import requests
url="https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv"
s=requests.get(url).content
data = pd.read_csv(io.StringIO(s.decode('utf-8')))
#df = data[data['Country/Region'] == 'Mainland China'] 
#print(data.columns[1])
#print(data.shape)
print(data.info)

countries = data['Country/Region'].drop_duplicates()

for country in countries:
  print (country)

# comment