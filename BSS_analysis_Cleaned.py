import os
import pandas as pd
import geopandas as gpd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
sns.set()
matplotlib.use('TkAgg')

# Set folder
os.chdir("SET FOLDER")

# Read data
bss_stations2016_fp = "\BSS_stations_2016_EUREF_HELSINKI_only.gpkg"
bss_stations2017_fp = "\Data\BSS_stations_2017_EUREF_HELSINKI_only.gpkg"
bss_stations2018_fp = "\BSS_stations_2018_EUREF_HELSINKI_only.gpkg"
bss_stations2019_fp = "\BSS_stations_2019_EUREF_HELSINKI_only.gpkg"
bss_stations2020_fp = "\BSS_stations_2020_EUREF_HELSINKI_only.gpkg"
bss_stations2021_fp = "\BSS_stations_2021_EUREF_HELSINKI_only.gpkg"
bss_stations2018_fp_csv = "\BSS_stations_2018_EUREF_HELSINKI_only.csv"
bss_stations2019_fp_csv = "\BSS_stations_2019_EUREF_HELSINKI_only.csv"
bss_stations2021_fp_csv = "\BSS_stations_2021_EUREF_HELSINKI_only.csv"

tripDF2016_fp = "\processed2016\BSS2016_Full_season_Cleaned.csv"
tripDF2017_fp = "\processed2017\BSS2017_Full_season_Cleaned.csv"
tripDF2018_fp = "\processed2018\BSS2018_Full_season_Cleaned.csv"
tripDF2019_fp = "\processed2019\BSS2019_Full_season_Cleaned.csv"
tripDF2020_fp = "\processed2020\BSS2020_Full_season_Cleaned.csv"
tripDF2021_fp = "\processed2021\BSS2021_Full_season_Cleaned.csv"

bss_stations2016 = gpd.read_file(bss_stations2016_fp)
bss_stations2017 = gpd.read_file(bss_stations2017_fp)
bss_stations2018 = gpd.read_file(bss_stations2018_fp)
bss_stations2019 = gpd.read_file(bss_stations2019_fp)
bss_stations2021 = gpd.read_file(bss_stations2021_fp)

bss_stations2018_csv = pd.read_csv(bss_stations2018_fp_csv, encoding='latin-1',  sep=',')
bss_stations2019_csv = pd.read_csv(bss_stations2019_fp_csv, encoding='latin-1',  sep=',')
bss_stations2021_csv = pd.read_csv(bss_stations2021_fp_csv, encoding='latin-1',  sep=',')

bss_tripDF_2016 = pd.read_csv(tripDF2016_fp, sep=";")
bss_tripDF_2017 = pd.read_csv(tripDF2017_fp)
bss_tripDF_2018 = pd.read_csv(tripDF2018_fp)
bss_tripDF_2019 = pd.read_csv(tripDF2019_fp)
bss_tripDF_2020 = pd.read_csv(tripDF2020_fp)
bss_tripDF_2021 = pd.read_csv(tripDF2021_fp)

# Convert departure and return fields to datetime type
bss_tripDF_2016['D_year'] = 2016
bss_tripDF_2016['Departure'] = pd.to_datetime(dict(year=bss_tripDF_2016.D_year, month=bss_tripDF_2016.D_month, day=bss_tripDF_2016.D_day, hour=bss_tripDF_2016.D_hour, minute=bss_tripDF_2016.D_min))
bss_tripDF_2017['departure_time'] = pd.to_datetime(bss_tripDF_2017['departure_time'], infer_datetime_format=True, format='%m%d%Y %H%M%S')
bss_tripDF_2018['Departure'] = pd.to_datetime(bss_tripDF_2018['Departure'], infer_datetime_format=True, format='%m%d%Y %H%M%S')
bss_tripDF_2019['Departure'] = pd.to_datetime(bss_tripDF_2019['Departure'], infer_datetime_format=True, format='%m%d%Y %H%M%S')
bss_tripDF_2020['Departure'] = pd.to_datetime(bss_tripDF_2020['Departure'], infer_datetime_format=True, format='%m%d%Y %H%M%S')
bss_tripDF_2021['Departure'] = pd.to_datetime(bss_tripDF_2021['Departure'], infer_datetime_format=True, format='%m%d%Y %H%M%S')

bss_tripDF_2016['Return'] = pd.to_datetime(dict(year=bss_tripDF_2016.D_year, month=bss_tripDF_2016.R_month, day=bss_tripDF_2016.R_day, hour=bss_tripDF_2016.R_hour, minute=bss_tripDF_2016.R_min))
bss_tripDF_2017['return_time'] = pd.to_datetime(bss_tripDF_2017['return_time'], infer_datetime_format=True, format='%m%d%Y %H%M%S')
bss_tripDF_2018['Return'] = pd.to_datetime(bss_tripDF_2018['Return'], infer_datetime_format=True, format='%m%d%Y %H%M%S')
bss_tripDF_2019['Return'] = pd.to_datetime(bss_tripDF_2019['Return'], infer_datetime_format=True, format='%m%d%Y %H%M%S')
bss_tripDF_2020['Return'] = pd.to_datetime(bss_tripDF_2020['Return'], infer_datetime_format=True, format='%m%d%Y %H%M%S')
bss_tripDF_2021['Return'] = pd.to_datetime(bss_tripDF_2021['Return'], infer_datetime_format=True, format='%m%d%Y %H%M%S')

# Add leading zeros to postal codes to avoid errors
bss_stations2018["No__Runnin"] = bss_stations2018["No__Runnin"].astype('int')
bss_stations2018["No__Runnin"] = bss_stations2018["No__Runnin"].astype(str).apply(lambda x: str("00"+ x) if (len(x) == 1) else (str("0"+ x) if (len(x) == 2) else (str(x))))

bss_stations2018_csv["No__Runnin"] = bss_stations2018_csv["No__Runnin"].astype(str).apply(lambda x: str("00"+ x) if (len(x) == 1) else (str("0"+ x) if (len(x) == 2) else (str(x))))
bss_stations2019_csv["ID"] = bss_stations2019_csv["ID"].astype(str).apply(lambda x: str("00"+ x) if (len(x) == 1) else (str("0"+ x) if (len(x) == 2) else (str(x))))
bss_stations2021_csv["ID"] = bss_stations2021_csv["ID"].astype(str).apply(lambda x: str("00"+ x) if (len(x) == 1) else (str("0"+ x) if (len(x) == 2) else (str(x))))

bss_tripDF_2018["departure_station1"] = bss_tripDF_2018["departure_station1"].astype(str).apply(lambda x: str("00"+ x) if (len(x) == 1) else (str("0"+ x) if (len(x) == 2) else (str(x))))
bss_tripDF_2019["Departure station id"] = bss_tripDF_2019["Departure station id"].astype(str).apply(lambda x: str("00"+ x) if (len(x) == 1) else (str("0"+ x) if (len(x) == 2) else (str(x))))
bss_tripDF_2020["Departure station id"] = bss_tripDF_2020["Departure station id"].astype(str).apply(lambda x: str("00"+ x) if (len(x) == 1) else (str("0"+ x) if (len(x) == 2) else (str(x))))
bss_tripDF_2021["Departure station id"] = bss_tripDF_2021["Departure station id"].astype(str).apply(lambda x: str("00"+ x) if (len(x) == 1) else (str("0"+ x) if (len(x) == 2) else (str(x))))

bss_tripDF_2018["return_station1"] = bss_tripDF_2018["return_station1"].astype(str).apply(lambda x: str("00"+ x) if (len(x) == 1) else (str("0"+ x) if (len(x) == 2) else (str(x))))
bss_tripDF_2019["Return station id"] = bss_tripDF_2019["Return station id"].astype(str).apply(lambda x: str("00"+ x) if (len(x) == 1) else (str("0"+ x) if (len(x) == 2) else (str(x))))
bss_tripDF_2020["Return station id"] = bss_tripDF_2020["Return station id"].astype(str).apply(lambda x: str("00"+ x) if (len(x) == 1) else (str("0"+ x) if (len(x) == 2) else (str(x))))
bss_tripDF_2021["Return station id"] = bss_tripDF_2021["Return station id"].astype(str).apply(lambda x: str("00"+ x) if (len(x) == 1) else (str("0"+ x) if (len(x) == 2) else (str(x))))

# Join departure and return station info to trip dataframes by year
bss_tripDF_2018 = bss_tripDF_2018.merge(bss_stations2018, how='left', left_on="departure_station1", right_on="No__Runnin")
bss_tripDF_2018 = bss_tripDF_2018.merge(bss_stations2018, how='left', left_on="return_station1", right_on="No__Runnin")
bss_tripDF_2019 = bss_tripDF_2019.merge(bss_stations2019, how='left', left_on="Departure station id", right_on="ID")
bss_tripDF_2019 = bss_tripDF_2019.merge(bss_stations2019, how='left', left_on="Return station id", right_on="ID")
bss_tripDF_2020 = bss_tripDF_2020.merge(bss_stations2019, how='left', left_on="Departure station id", right_on="ID")
bss_tripDF_2020 = bss_tripDF_2020.merge(bss_stations2019, how='left', left_on="Return station id", right_on="ID")
bss_tripDF_2021 = bss_tripDF_2021.merge(bss_stations2021,how='left', left_on="Departure station id", right_on="ID")
bss_tripDF_2021 = bss_tripDF_2021.merge(bss_stations2021, how='left', left_on="Return station id", right_on="ID")

bss_tripDF_2018 = bss_tripDF_2018.merge(bss_stations2018_csv, how='left', left_on="departure_station1", right_on="No__Runnin")
bss_tripDF_2018 = bss_tripDF_2018.merge(bss_stations2018_csv, how='left', left_on="return_station1", right_on="No__Runnin")
bss_tripDF_2019 = bss_tripDF_2019.merge(bss_stations2019_csv, how='left', left_on="Departure station id", right_on="ID")
bss_tripDF_2019 = bss_tripDF_2019.merge(bss_stations2019_csv, how='left', left_on="Return station id", right_on="ID")
bss_tripDF_2020 = bss_tripDF_2020.merge(bss_stations2019_csv, how='left', left_on="Departure station id", right_on="ID")
bss_tripDF_2020 = bss_tripDF_2020.merge(bss_stations2019_csv, how='left', left_on="Return station id", right_on="ID")
bss_tripDF_2021 = bss_tripDF_2021.merge(bss_stations2021_csv, how='left', left_on="Departure station id", right_on="ID")
bss_tripDF_2021 = bss_tripDF_2021.merge(bss_stations2021_csv, how='left', left_on="Return station id", right_on="ID")

# Exclude trips that took place only in Espoo (Trips in Espoo started in 2018)
bss_tripDF_2018_Helsinki = bss_tripDF_2018.dropna(subset=['No__Runnin_x', 'No__Runnin_y'], thresh=1)
bss_tripDF_2019_Helsinki = bss_tripDF_2019.loc[(bss_tripDF_2019["Dep_City"]!= "Espoo") | (bss_tripDF_2019["Ret_City"] != "Espoo")]
bss_tripDF_2020_Helsinki = bss_tripDF_2020.loc[(bss_tripDF_2020["Dep_City"]!= "Espoo") | (bss_tripDF_2020["Ret_City"] != "Espoo")]
bss_tripDF_2021_Helsinki = bss_tripDF_2021.loc[(bss_tripDF_2021["Dep_City"]!= "Espoo") | (bss_tripDF_2021["Ret_City"] != "Espoo")]

# Calculate Trip/bike/day (TDB) indicator for Helsinki trips in 2019-2020
bss_tripDF_2019_Helsinki_June_Oct = bss_tripDF_2019_Helsinki.loc[bss_tripDF_2019_Helsinki["Month"].isin([6,7,8,9,10])]
bss_tripDF_2020_Helsinki_May = bss_tripDF_2020_Helsinki.loc[bss_tripDF_2020_Helsinki["Month"].isin([5])]
bss_tripDF_2019_2020_Helsinki = pd.concat([bss_tripDF_2019_Helsinki_June_Oct,bss_tripDF_2020_Helsinki_May])

# Analyse the share of trips inside/outside the urban core of Helsinki (pre-calculated to the data in QGIS)
urbanCoreTrips2021 = bss_tripDF_2021_Helsinki.loc[(bss_tripDF_2021_Helsinki["urbanCore_x"] ==1) & (bss_tripDF_2021_Helsinki["urbanCore_y"] ==1)]
urbanCoreDeparture2021 = bss_tripDF_2021_Helsinki.loc[(bss_tripDF_2021_Helsinki["urbanCore_x"] ==1)]
urbanCoreTrips2021_PT = urbanCoreTrips2021.loc[(urbanCoreTrips2021["pt_100m_x"] ==1) | (urbanCoreTrips2021["pt_100m_y"] ==1)]
len(urbanCoreTrips2021.index)
len(urbanCoreDeparture2021.index)
len(urbanCoreTrips2021_PT.index)

outsideUrbanCoreTrips2021 = bss_tripDF_2021_Helsinki.loc[(bss_tripDF_2021_Helsinki["urbanCore_x"] ==0) & (bss_tripDF_2021_Helsinki["urbanCore_y"] ==0)]
outsideUrbanCoreDeparture2021 = bss_tripDF_2021_Helsinki.loc[(bss_tripDF_2021_Helsinki["urbanCore_x"] ==0)]
outsideUrbanCoreTrips2021_PT = outsideUrbanCoreTrips2021.loc[(outsideUrbanCoreTrips2021["pt_100m_x"] ==1) | (outsideUrbanCoreTrips2021["pt_100m_y"] ==1)]
len(outsideUrbanCoreTrips2021.index)
len(outsideUrbanCoreDeparture2021.index)
len(outsideUrbanCoreTrips2021_PT.index)

#****************************************
#       VISUALIZATION
##***************************************

# Create the graph showing  evclution of BSS trips in Helsinki
tripsByDay_2016= bss_tripDF_2016['Departure'].groupby(by=bss_tripDF_2016['Departure'].dt.date).count()
tripsByDay_2017= bss_tripDF_2017['departure_time'].groupby(by=bss_tripDF_2017['departure_time'].dt.date).count()
tripsByDay_2018= bss_tripDF_2018['Departure'].groupby(by=bss_tripDF_2018['Departure'].dt.date).count()
tripsByDay_2019= bss_tripDF_2019['Departure'].groupby(by=bss_tripDF_2019['Departure'].dt.date).count()
tripsByDay_2020= bss_tripDF_2020['Departure'].groupby(by=bss_tripDF_2020['Departure'].dt.date).count()
tripsByDay_2021= bss_tripDF_2021['Departure'].groupby(by=bss_tripDF_2021['Departure'].dt.date).count()

dfs =[tripsByDay_2016,tripsByDay_2017,tripsByDay_2018,tripsByDay_2019,tripsByDay_2020,tripsByDay_2021]
tripsbyDay_2016_21 = pd.concat(dfs)

tripsbyDay_2016_21.plot(marker='o', alpha=0.5, linestyle='None', markersize=4, color='b')
plt.vlines(x=["2017-01-01","2019-01-01", "2021-01-01"], ymin=0, ymax=25000, colors='black', ls='--', lw=2.0)

plt.text("2016-09-25", 26000, '1$^{st}$ expansion \nin Helsinki', fontsize = 24)
plt.text("2018-08-25", 26000, '2$^{nd}$ expansion \nin Helsinki', fontsize = 24)
plt.text("2020-09-25", 26000, '3$^{rd}$ expansion \nin Helsinki', fontsize = 24)
plt.xticks(fontsize=24)
plt.yticks(fontsize=24)
plt.xlabel('Year', fontsize=30,labelpad= 15)
plt.ylabel('Daily trip count', fontsize=30,labelpad=15)


