from collections import Counter
import requests
import json


class crimeReport():
    def __init__(self,location,crimeType,date):
        self.location = location
        self.crimeType = crimeType
        self.date = date
        self.crimes = self.find_crimes()

    def find_crimes(self):
        crimeNoLocation = 'https://data.police.uk/api/crimes-no-location?category=all-crime&force=leicestershire&date=2017-03'
        payload = {'category':self.crimeType,
                   'location':self.location,
                   'date':self.date}
        response = requests.get(crimeNoLocation,payload)
        
        if response.status_code == 200:
            return response.json()
        else:
            return None
    
    def listReports(self):
        crime_list = []
        if self.crimes is not None:
            for crime in self.crimes:
                crime_list.append(crime['category'])
            return crime_list


searchReport = crimeReport('city-of-london','all-crime','2020-02')
print()
crimeReportFull = Counter(searchReport.listReports())
print("All crimes in London on February 2020 : {}".format(sum(crimeReportFull.values())))
