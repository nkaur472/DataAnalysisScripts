import requests
import csv
from collections import OrderedDict

url = r'http://prd.api.webcams.open511.gov.bc.ca/v1/webcams?format=json'
csv_path = r'...\sample.csv'

response = requests.get(url)
datastore = response.json()

exclude_dic = ['isOn','isNew','isOnDemand']
include_dic = ['links','highway','location','message','imageStats']
include_subdic = ['imageThumbnail','imageDisplay','replayTheDay','bchighwaycam','locationDescription','number','updatePeriodMean','updatePeriodStdDev','longitude','latitude']

# Headers are added on row index 0
row = 0

with open(csv_path, 'wb') as csv_file:
	csv_writer = csv.writer(csv_file,dialect='excel')
	for data in datastore['webcams']:
		keys = ''
		values = '' 
		for key,value in data.iteritems():
			if key in include_dic:
				for k,v in value.iteritems():
					if k in include_subdic:
						if keys == '':
							keys = (key+'_'+k)
						else:
							keys = keys+';'+(key+'_'+k)
						if values == '':
							values = str(v)
						else:
							values = values+';'+str(v)

			elif key not in exclude_dic:
				if keys == '':
					keys = key
				else:
					keys = keys+';'+key
				if values == '':
					values = str(value)
				else:
					values = values+';'+str(value)
		if row == 0:
			keys_split = keys.split(';')		
			csv_writer.writerow(keys_split)
		values_split = values.split(';')
		csv_writer.writerow(values_split) 
		row = row+1			
		 