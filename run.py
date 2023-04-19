import datetime
import time
import pandas as pd
import gazpacho


""" Get real time data from URL """

URL = "https://opendata-geohive.hub.arcgis.com/datasets/d8eb52d56273413b84b0187a4e9117be_0.csv?outSR=%7B%22latestWkid%22%3A3857%2C%22wkid%22%3A102100%7D"

Covid = "covid.csv"
data = gazpacho.get(URL)

data = data.split("\n")
today = str(datetime.date.today())
now = time.strftime("%H:%M", time.localtime())

with open(PATH + Covid, "a") as lf:
    for line in data[1:-1]:
        print(f"{today},{now},", file=lf, end="")
        print(line, file=lf)


"""  Creates dataframe Covid_df with the data stored in 
covid.csv file"""   


Covid_df1 = pd.read_csv(URL)

pd.set_option('display.max_columns', None)   ## To see all the columns of a dataframe

pd.set_option('display.max_columns', None)  ## To see all the rows of a dataframe

Covid_df=Covid_df1.copy()        ## Creates copy of dataframe

Covid_df = Covid_df.drop(['X','Y','Date','CommunityTransmission','CloseContact','TravelAbroad','FID','ClustersNotified','DeathsCumulative_DOD','ConfirmedCovidDeaths','TotalConfirmedCovidCases','TotalCovidDeaths'],axis=1)


Covid_df.StatisticsProfileDate = pd.to_datetime(Covid_df.StatisticsProfileDate).dt.date


""" Storedclean data into csv files"""

Covid_df.to_csv("Clean_data.csv")

Hospitalised_df=Covid_df[['StatisticsProfileDate','HospitalisedAged5','HospitalisedAged5to14','HospitalisedAged15to24','HospitalisedAged25to34','HospitalisedAged35to44','HospitalisedAged45to54','HospitalisedAged55to64','HospitalisedAged65to74','HospitalisedAged75to84','HospitalisedAged85up']].copy()
Hospitalised_df=Hospitalised_df.set_index('StatisticsProfileDate')


Hospitalised_df.head()
 

